"""
 ******************************************************************************
 *
 * File Name          : lavazza_cfds_input_key_handler.py
 * File description   : Key press simulator and controller service
 * Version            : 1.0
 * Date               : August 10 2020
 *
 * Copyright (C) mieuPro Systems, 2020
 *
 ******************************************************************************
 """

from time import sleep

# RPi.GPIO library used to accessing GPIO pins
import RPi.GPIO as GPIO

import lavazza_cfds_mb_io_handler_variable
from lavazza_cfds_mb_io_handler_macros import *

import lavazza_cfds_lcd_output_reader

# mb_io_handler_system_resources are used for the inter process communication.
mb_io_handler_system_resources = None
# milk_product_keys holds the GPIO pin number of the Milk products which are all configured in the machine.
milk_product_keys = []


# Wait function for the _lcd_display_event which gives key press simulation status by using the lcd string change
def wait_for_lcd_display_event(wait_time):
    try:
        # lcd_display_event is used to notify the lcd_string change to the Input key handler.
        # Input key handler simulate the key press and then wait for lcd_string change to
        # ensure the success of that simulation. It could wait maximum for the wait_time.
        # Code will getting out of this blocking statement, when the lcd_string changes or max wait_time expired.
        logging.info("Input_Key_Handler : Waiting for the lcd_display_event")
        mb_io_handler_system_resources["lcd_display_event"].wait(wait_time)

        # Here we are checking whether the lcd_string changes or the max wait_time getting expired.
        # isSet function call returns True if the event is set, otherwise it will returns False
        if mb_io_handler_system_resources["lcd_display_event"].isSet():
            logging.info("Input_Key_Handler : lcd_display_event occurred")
            return SUCCESS

        # In case of failure in the key press simulation or the motherboard didn't accept the key press at that time,
        # there won't be any changes in the lcd_string. We just log this event to our log file
        else:
            logging.warning("Input_Key_Handler : Please checking for the hardware connection failure"
                            "or lcd_output_reader may stopped... there is no change in the lcd_data")
            return FAILURE

    except Exception as error:
        logging.exception("Input_Key_Handler : wait_for_lcd_display_event : {}".format(error))
        return FAILURE

    finally:
        # We should clear the event after that particular event occurs. Otherwise, wait will not be a blocking call.
        mb_io_handler_system_resources["lcd_display_event"].clear()
        logging.info("Input_Key_Handler : lcd_display_event cleared")


# Safety function to reset all product and function to low state.
def reset_gpio_pins():
    try:
        logging.info("Input_Key_Handler : reset_gpio_pins function started")

        # Set all the product keys to low state.
        for key in PRODUCT_KEYS:
            GPIO.output(key, GPIO.LOW)

        # # Set all the function keys to low state.
        for key in FUNCTION_KEYS:
            GPIO.output(key, GPIO.LOW)

        logging.info("Input_Key_Handler : reset_gpio_pins function finished")
        return SUCCESS

    except Exception as error:
        logging.exception("Input_Key_Handler : reset_gpio_pins : {}".format(error))
        return FAILURE


# Cleaning is used for machine cleaning simulation.
def cleaning(desired_string, no_of_string_change, simulation_wait_time):
    try:
        logging.info("Input_Key_Handler : cleaning function started {} , {}, {}".format(
            desired_string, no_of_string_change, simulation_wait_time))
        # Set the Rinse key to HIGH for the cleaning simulation.
        GPIO.output(FUNCTION_KEY4, GPIO.HIGH)

        # We need to wait for the no_of_string_changes as per which cleaning the user wants.
        # i.e Milk unit cleaning takes two string changes.
        for i in range(no_of_string_change):
            wait_for_lcd_display_event(simulation_wait_time)
            logging.debug("Input_Key_Handler : cleaning data {} - {}".format(i, lavazza_cfds_mb_io_handler_variable.lcd_data))

        # We could confirm the simulation status by checking the current lcd data.
        if lavazza_cfds_mb_io_handler_variable.lcd_data == desired_string:
            logging.info("Input_Key_Handler : Getting the {} successfully".format(desired_string))
            return SUCCESS
        else:
            raise Exception("Something went wrong getting {} string".format(desired_string))

    except Exception as error:
        logging.exception("Input_Key_Handler : cleaning : {}".format(error))
        return FAILURE

    finally:
        # We should set the Rinse key to LOW state once the simulation finished.
        GPIO.output(FUNCTION_KEY4, GPIO.LOW)
        logging.info("Input_Key_Handler : Cleaning key successfully set to LOW state")


# It's a common function to enable and disable the particular key
def toggle_key_state(key, state):
    try:
        logging.info("Input_Key_Handler : toggle_key_state for {} and state {}".format(key, state))
        if state == ENABLE:
            # Set the key to HIGH state to ENABLE
            GPIO.output(key, GPIO.HIGH)
            # Given small sleep time between the successive key press for the safety
            sleep(KEY_PRESS_PAUSE_TIME)
        elif state == DISABLE:
            # Set the key to LOW state to DISABLE
            GPIO.output(key, GPIO.LOW)
            # Given small sleep time between the successive key press for the safety
            sleep(KEY_PRESS_PAUSE_TIME)
        logging.info("Input_Key_Handler : toggle_key_state function finished")
        return SUCCESS

    except Exception as error:
        logging.exception("Input_Key_Handler : toggle_key_state : {}".format(error))
        return FAILURE


# key press simulation for combination of two buttons i.e count reading, foamer on or off, etc.
def combined_key_press_simulation(key1, key2, wait_time):
    try:
        logging.info("Input_Key_Handler : combined_key_press_simulation for {} and {}".format(key1, key2))
        # Set key1 pin to HIGH state first
        GPIO.output(key1, GPIO.HIGH)
        # Given some time before simulate the key2 key press
        sleep(COMBINED_KEY_PRESS_PAUSE_TIME)
        # Set key2 pin to HIGH state
        GPIO.output(key2, GPIO.HIGH)
        # Wait sometime to change the lcd_data to ensure that our key press simulation success.
        # MAX_WAIT_TIME_FOR_COMBINED_KEY_PRESS tells that how long we can wait for the lcd_data change.
        # In case of any error, lcd_data won't be changed. So, this function needs to be
        # return immediately after max wait time.
        key_press_simulation_status = wait_for_lcd_display_event(wait_time)
        # We should set key2 pin to LOW state first.
        # Because, the second key can be product key or function key and the first key definitely the function key.
        # Otherwise, in case of the second key is the product key means, it's simulation also will occur.
        GPIO.output(key2, GPIO.LOW)
        # Given some time before set key1 pin to LOW state
        sleep(COMBINED_KEY_PRESS_PAUSE_TIME)
        # set key1 pin to LOW state
        GPIO.output(key1, GPIO.LOW)

        logging.info("Input_Key_Handler : combined_key_press_simulation finished")

        return key_press_simulation_status

    except Exception as error:
        logging.exception("Input_Key_Handler : combined_key_press_simulation : {}".format(error))
        # In case error we should set the key1 and key2 to LOW state.
        GPIO.output(key2, GPIO.LOW)
        GPIO.output(key1, GPIO.LOW)
        return FAILURE


# key press simulation for the function keys
def function_key_press_simulation(key, string_change_confirmation_status):
    try:
        logging.info("Input_Key_Handler : function_key_press_simulation for {}".format(key))
        # Set HIGH state on that particular GPIO pin to simulate key press
        GPIO.output(key, GPIO.HIGH)
        # Given some time for the effect of key press simulation
        sleep(KEY_PRESS_PAUSE_TIME)
        # Set that GPIO pin to LOW state after the key simulation finished.
        # Here, we are not wait for the lcd_string to change before set that GPIO pin to LOW state.
        # Because, function keys can be used for the combined key press.
        # So, if we wait for lcd_string change after set that GPIO pin to HIGH, motherboard think it is long press.
        # So, we need to set that GPIO pin to LOW state, before going to check the lcd_string change
        GPIO.output(key, GPIO.LOW)

        # string_change_confirmation_status is used to know whether the caller expect the key simulation status or not.
        # If caller wants the key simulation status we need to wait for the lcd_display_event.
        if string_change_confirmation_status:
            # Wait sometime to change the lcd_data to ensure that our key press simulation success.
            # MAX_WAIT_TIME_FOR_SINGLE_KEY_PRESS tells that how long we can wait for the lcd_data change.
            # In case of any error, lcd_data won't change.
            # So, this function need to be return immediately after the max wait time.
            # This wait time also given some time between the successive key press.
            key_press_simulation_status = wait_for_lcd_display_event(MAX_SHORT_KEY_PRESS_SIMULATION_WAIT_TIME)

        # If caller has no interest in the key simulation status, then no need to wait for the lcd_display_event.
        else:
            key_press_simulation_status = SUCCESS

        logging.info("Input_Key_Handler : function_key_press_simulation finished")
        return key_press_simulation_status

    except Exception as error:
        logging.exception("Input_Key_Handler : function_key_press_simulation : {}".format(error))
        # In case error we should set the key to LOW state.
        GPIO.output(key, GPIO.LOW)
        return FAILURE


# key press simulation for the product keys.
def product_key_press_simulation(key, string_change_confirmation_status):
    try:
        logging.info("Input_Key_Handler : product_key_press_simulation for {}".format(key))
        # set HIGH state on that particular GPIO pin to simulate key press
        GPIO.output(key, GPIO.HIGH)
        sleep(KEY_PRESS_PAUSE_TIME)

        # string_change_confirmation_status is used to know whether the caller expect the key simulation status or not.
        # If the caller wants to know the key simulation status, then we need to wait for the lcd_display_event.
        if string_change_confirmation_status:
            # Wait sometime to change the lcd_data to ensure that our key press simulation success.
            # If it is milk product key, in case of foamer off state  dispensation won't happen.
            # In such case lcd_string change takes some 0.5 seconds extra other than the success case.
            # MAX_WAIT_TIME_FOR_SINGLE_KEY_PRESS tells that how long we can wait for the lcd_data change.
            # In case of any error, lcd_data won't change.
            # So, this function needs to be return immediately after the max wait time.
            key_press_simulation_status = wait_for_lcd_display_event(MAX_SHORT_KEY_PRESS_SIMULATION_WAIT_TIME)

        # If caller has no interest in the key simulation status, then no need to wait for the lcd_display_event.
        else:
            key_press_simulation_status = SUCCESS

        # set that GPIO pin to LOW state after the key simulation finished
        GPIO.output(key, GPIO.LOW)

        logging.info("Input_Key_Handler : product_key_press_simulation finished")

        return key_press_simulation_status

    except Exception as error:
        logging.exception("Input_Key_Handler : product_key_press_simulation : {}".format(error))
        # In case error we should set the key to LOW state.
        GPIO.output(key, GPIO.LOW)
        return FAILURE


# technician_key_press_simulation_handler is for Technician and Admin.
def technician_key_press_simulation_handler(input_key_data):
    try:
        logging.info("Input_Key_Handler : technician_key_press_simulation_handler function started")

        # Get key and state from the caller input key data.
        key = input_key_data["key"]
        state = input_key_data["state"]

        # If caller wants press the PRODUCT_KEY, call the product_key_press_simulation to simulate
        # the key press of that particular product key given by the caller.
        if key in PRODUCT_KEYS:
            # We are giving the long key press functionality and the normal key press functionality to the Technicians.
            # For that we need to check the state of the key.
            # If it is None we should provide the normal key press simulation.
            if state is None:
                key_simulation_status = product_key_press_simulation(key, string_change_confirmation_status=False)
            # If the state of the key is true or false, then we should provide the long key press simulation.
            else:
                key_simulation_status = toggle_key_state(key, state)

        # If caller wants press the FUNCTION_KEY, call the function_key_press_simulation to simulate
        # the key press of that particular function key given by the caller.
        elif key in FUNCTION_KEYS:
            # We are giving the long key press functionality and the normal key press functionality to the Technicians.
            # For that we need to check the state of the key.
            # If it is None we should provide the normal key press simulation.
            if state is None:
                key_simulation_status = function_key_press_simulation(key, string_change_confirmation_status=False)
            # If the state of the key is true or false, then we should provide the long key press simulation.
            else:
                key_simulation_status = toggle_key_state(key, state)

        # FOAMER is used to turn on or off the foamer in the coffee vending machine.
        # Machine requires at least one milk product to be configured for foamer on/off functionality.
        elif key == FOAMER:
            if milk_product_keys:
                key_simulation_status = combined_key_press_simulation(FUNCTION_KEY2, milk_product_keys[0],
                                                                      MAX_SHORT_KEY_PRESS_SIMULATION_WAIT_TIME)
            else:
                logging.warning("Input_Key_Handler : Milk products are not configured")
                key_simulation_status = FAILURE

        # COUNT_READING is used to get into the count reading mode without using service card.
        elif key == COUNT_READING:
            key_simulation_status = combined_key_press_simulation(COUNT_READING_KEYS[0], COUNT_READING_KEYS[1],
                                                                  MAX_LONG_KEY_PRESS_SIMULATION_WAIT_TIME)

        # RESET_OR_CONFIG_BACK_MODE is used to reset the supplies of the product to 0 or
        # used to backward traversing in the configuration menu.
        # Here state is used to tell whether they want to enable or disable this functionality.
        elif key == RESET_OR_CONFIG_BACK_MODE:
            key_simulation_status = toggle_key_state(FUNCTION_KEY3, state)

        # COFFEE_UNIT_CLEANING_ID is used for the coffee unit cleaning simulation.
        elif key == COFFEE_UNIT_CLEANING_ID:
            key_simulation_status = cleaning(COFFEE_UNIT_CLEANING, NO_OF_KEY_SIMULATION_FOR_COFFEE_UNIT_CLEANING,
                                             MAX_LONG_KEY_PRESS_SIMULATION_WAIT_TIME)

        # MILK_UNIT_CLEANING_ID is used for the milk unit cleaning simulation.
        elif key == MILK_UNIT_CLEANING_ID:
            key_simulation_status = cleaning(MILK_UNIT_CLEANING, NO_OF_KEY_SIMULATION_FOR_MILK_UNIT_CLEANING,
                                             MAX_LONG_KEY_PRESS_SIMULATION_WAIT_TIME)

        # COFFEE_AND_MILK_UNIT_CLEANING_ID is used for the both coffee and milk unit cleaning simulation.
        elif key == COFFEE_AND_MILK_UNIT_CLEANING_ID:
            key_simulation_status = cleaning(COFFEE_AND_MILK_UNIT_CLEANING, NO_OF_KEY_SIMULATION_FOR_COFFEE_AND_MILK_UNIT_CLEANING,
                                             MAX_LONG_KEY_PRESS_SIMULATION_WAIT_TIME)

        # EXCESS_MILK_CLEANING_WATER_REMOVAL is used for removing excess of water at the milk cleaning.
        elif key == EXCESS_MILK_CLEANING_WATER_REMOVAL:
            key_simulation_status = toggle_key_state(milk_product_keys[0], state)

        # GPIO_RESET is used to reset all the products and functions key to LOW state.
        elif key == GPIO_RESET:
            key_simulation_status = reset_gpio_pins()

        # We should handle the Invalid requests too.
        else:
            logging.warning("Input_Key_Handler : Invalid request")
            key_simulation_status = FAILURE

        return key_simulation_status

    except Exception as error:
        logging.exception("Input_Key_Handler : technician_key_press_simulation_handler : {}".format(error))
        return FAILURE


# user_key_press_simulation_handler is for the Users and Mobile app.
def user_key_press_simulation_handler(input_key_data):
    try:
        logging.info("Input_Key_Handler : user_key_press_simulation_handler function started")

        key = input_key_data["key"]

        # We should not allow the user key simulation at the time of MACHINE_NOT_READY_STATE and
        # service card inserted state.
        if lavazza_cfds_mb_io_handler_variable.machine_state == MACHINE_NOT_READY_STATE or \
                lavazza_cfds_mb_io_handler_variable.service_card_state:
            logging.warning("Input_Key_Handler : Machine is not ready for the Dispensation")
            key_simulation_status = MACHINE_NOT_READY_STATE

        # We can allow the product key press simulation when the machine is in the USER_KEY_SIMULATION_ALLOWED_STATES.
        elif lavazza_cfds_mb_io_handler_variable.machine_state in USER_KEY_SIMULATION_ALLOWED_STATES and key in PRODUCT_KEYS:
            if product_key_press_simulation(key, string_change_confirmation_status=True) == SUCCESS:
                if lavazza_cfds_mb_io_handler_variable.machine_state in USER_KEY_SIMULATION_WORKING_STATES:
                    key_simulation_status = lavazza_cfds_mb_io_handler_variable.machine_state

                else:
                    logging.warning("Input_Key_Handler : Invalid result")
                    key_simulation_status = FAILURE
            else:
                key_simulation_status = FAILURE

        # We can allow the product key press simulation when the machine is in the DISPENSING_STATE.
        # It is used to stop the current dispensation in the middle.
        elif lavazza_cfds_mb_io_handler_variable.machine_state == DISPENSING_STATE and key in PRODUCT_KEYS:
            if product_key_press_simulation(key, string_change_confirmation_status=True) == SUCCESS:
                key_simulation_status = READY_TO_DISPENSE_STATE
            else:
                key_simulation_status = FAILURE

        # We should handle Invalid requests too.
        else:
            logging.warning("Input_Key_Handler : Key simulation not allowed")
            key_simulation_status = FAILURE

        return key_simulation_status

    except Exception as error:
        logging.exception("Input_Key_Handler : user_key_press_simulation_handler : {}".format(error))
        return FAILURE


# Handler for the key press simulation requested by the other services
def key_press_input_queue_handler(input_key_data):
    try:
        # Checking for the key disable status.
        # If Keypad is not disabled then key simulation will not work.
        if DEVICE_TYPE == PANTRY_TYPE:
            keypad_status = lavazza_cfds_lcd_output_reader.iot_board_handler(KEYPAD_STATUS_CMD)
            logging.info("Input_Key_Handler : Keypad status before Key press simulation : {}".format(keypad_status))
            try:
                if keypad_status.split(",")[1].strip() == '1':
                    logging.info("Input_Key_Handler : Keypad is in Enabled state")
                    keypad_status = lavazza_cfds_lcd_output_reader.iot_board_handler(DISABLE_KEYPAD_CMD)
                    logging.info("Input_Key_Handler : Keypad status : {}".format(keypad_status))
                    if keypad_status.split(",")[1].strip() == '1':
                        logging.warning("Input_Key_Handler : IOT board is not disable the Keypad")
                        return FAILURE
                else:
                    logging.info("Input_Key_Handler : Keypad is in Disabled state")
            except Exception as error:
                logging.exception("Input_Key_Handler : keypad_status error : {}".format(error))

        # key_simulation_state indicates that current simulation is done by the Input key handler.
        # Input Key Handler can get the lcd data change notification only if this variable enabled.
        lavazza_cfds_mb_io_handler_variable.key_simulation_state = ENABLE
        logging.info("Input_Key_Handler : Input key simulation started")

        # key_simulation_caller is used to send the dispense completion status to the Mobile app
        # from the Lcd_Output_Reader.
        lavazza_cfds_mb_io_handler_variable.key_simulation_caller = input_key_data["caller"]

        # Key press simulation for the GUI Users and Mobile App Users.
        if input_key_data["caller"] == USER_CALLER_ID or input_key_data["caller"] == MOBILE_APP_ID:
            key_simulation_status = user_key_press_simulation_handler(input_key_data)

        # Key press simulation for the Admin and Technician
        else:
            key_simulation_status = technician_key_press_simulation_handler(input_key_data)

        # We should change the key_simulation_caller value to None once the key simulation finished.
        # Because, if the key press coming from the mechanical key pad, then lcd output reader think that it is coming
        # the Input Key Handler. This may leads to the mal functionality in the Application.
        # But, if the machine is in the DISPENSING_STATE due to the Input Key Handler, we should not change the value.
        # Because, this value is essential for sending dispense completion status to the Mobile App server.
        if lavazza_cfds_mb_io_handler_variable.machine_state != DISPENSING_STATE:
            lavazza_cfds_mb_io_handler_variable.key_simulation_caller = None

        # We should disable the key_simulation_state once we done with the key simulation.
        # Otherwise lcd output reader gives the lcd data change notification unnecessarily.
        # It will lead to the problem with our inter process communication.
        lavazza_cfds_mb_io_handler_variable.key_simulation_state = DISABLE
        # For the safety purpose we should clear the lcd_display_event.
        mb_io_handler_system_resources["lcd_display_event"].clear()

        logging.info("Input_Key_Handler : key_simulation_status - {}".format(key_simulation_status))

        # We are giving the key_simulation_status only to the GUI Users and Mobile App Users.
        #  Because, key_simulation_status is no need for the Admin and Technicians.
        if input_key_data["caller"] == USER_CALLER_ID or input_key_data["caller"] == MOBILE_APP_ID:
            return key_simulation_status

    except Exception as error:
        logging.exception("Input_Key_Handler : key_press_input_queue_handler : {}".format(error))


# set the milk product key for the foamer on/off functionality
def set_milk_product_keys():
    global milk_product_keys
    try:
        # Get milk products from provisioned_product_details
        for product in device_info["provisioned_product_details"]:
            if product["milk_based_product"]:
                logging.debug("Input_Key_Handler : milk_product : {}".format(product))
                # Set the milk_product_keys
                milk_product_keys.append(PRODUCT_KEYS[product["product_no"] - 1])

        if milk_product_keys:
            logging.debug("Input_Key_Handler : milk_product_keys : {}".format(milk_product_keys))
        else:
            logging.warning("Input_Key_Handler : Milk products are not configured")

    except Exception as error:
        logging.exception("Input_Key_Handler : set_milk_product_keys : {}".format(error))


def init_input_key_handler(system_resources):
    try:
        global mb_io_handler_system_resources

        # Get the mb_io_handler_system_resources for the inter process communication
        mb_io_handler_system_resources = system_resources
        logging.debug("Input_Key_Handler : mb_io_handler_system_resources - {}".format(mb_io_handler_system_resources))

        keypad_status = lavazza_cfds_lcd_output_reader.iot_board_handler(KEYPAD_STATUS_CMD)
        logging.debug("Input_Key_Handler : Default keypad_status - {}".format(keypad_status))

        # We should disable the mechanical key pad for Retro-fit type.
        if DEVICE_TYPE != PANTRY_TYPE:
            keypad_status = lavazza_cfds_lcd_output_reader.iot_board_handler(DISABLE_KEYPAD_CMD)
        # We should enable the mechanical key pad for Pantry type.
        else:
            keypad_status = lavazza_cfds_lcd_output_reader.iot_board_handler(ENABLE_KEYPAD_CMD)

        logging.debug("Input_Key_Handler : Initial Keypad_status - {}".format(keypad_status))

        set_milk_product_keys()
        logging.info("Input_Key_Handler : Milk_product_key set successfully")

        return SUCCESS

    except Exception as error:
        logging.exception("Input_Key_Handler : init_input_key_handler : {}".format(error))
        return FAILURE

