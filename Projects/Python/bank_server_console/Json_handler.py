import os
import json
class Basic_Functions:
    def __init__(self):
        pass

    def Read_File(filepath):
        try :
            if os.path.isfile(filepath):
                with open(filepath,"r") as file:
                    file_txt = file.read()
                    Read_Content = json.loads(file_txt)
        except Exception as error:
            print(error)
        return Read_Content

    def Write_File(filepath,content):
        try:
            if os.path.isfile(filepath):
                with open(filepath,"w") as file:
                    file.write(json.dumps(content,indent = 4,separators = ',:'))
                    return 'Success'
        except Exception as error :
            print("Unsuccessful")
        return 'Failure'


class Added_Features(Basic_Functions):
    def Check_Bank_Balance(self):
        try :
            Mob_Number = input("\nEnter Your Mobile number associated with UPI Bank : ")
            Main_Database = Basic_Functions.Read_File("server_entries.json")
            for users in Main_Database :
                user = Main_Database[users]
                for data in user.values() :
                    if data == Mob_Number :
                        User = users
        
            Bank_Balance = Main_Database[User]["Bank_Balance"] 
            Customer_Name = Main_Database[User]["Cus_Name"]
            print(f"\nCustomer Name : {Customer_Name}")
            print(f"\nAvailable Bank Balance : {Bank_Balance}")

        except :
            print("\nEnter the credentials correctly")

    def Check_Mini_Statement(self):
        try :
            AC_NUM = input("\nEnter Your Account Number : ")
            print()
            Main_Database = Basic_Functions.Read_File("server_entries.json")
            for users in Main_Database :
                user = Main_Database[users]
                for data in user.values() :
                    if data == AC_NUM :
                        User = users
            with open("Test_log_Bank_Server.log","r") as log_file :
                log_content = log_file.read()
            log_list = log_content.split("\n")
            User_log_list = []
            for user_statement in log_list :
                if AC_NUM in user_statement :
                    User_log_list.append(user_statement)
            for all_entries in User_log_list :
                if "INFO" in all_entries :
                    idx = all_entries.find("INFO")
                    only_needed_data = all_entries[idx+6 :]
                    print(only_needed_data)
        except :
            print("\nEnter the credentials correctly")

Feature_Instance = Added_Features()
#Feature_Instance.Check_Mini_Statement()
