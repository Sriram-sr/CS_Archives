import json
import re 
from getpass import getpass
from Json_handler import Basic_Functions
import Json_handler
import logging
import queue
import threading
import random

class Online_Bank:
    def __init__(self,User_Dict,Associated_Account_Numbers_List):
            self.User_Dict = User_Dict
            # print(self.User_Dict)
            self.Associated_Account_Numbers = Associated_Account_Numbers_List

    def Deposit_Module(self):
        try :
            logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,\
                    format = '%(asctime)s-%(levelname)s- DEPOSIT_HISTORY -%(message)s')
            self.Ac_no = input("\nEnter your Account Number: ")
            if self.Ac_no not in self.Associated_Account_Numbers :
                print("\nEnter a Valid Account Number")
            self.Password = getpass("\nEnter your password: ")
            self.Amount = int(input("\nEnter the amount you want to deposit: "))
            for user in self.User_Dict:
                user_dict = self.User_Dict[user]
                for details in user_dict.values():
                    if self.Ac_no == details :
                        self.user = user
            self.Current_Balance = self.User_Dict[self.user]["Bank_Balance"]
            self.User_Name = self.User_Dict[self.user]["Cus_Name"]
            print("\nSuccessfully Credited your amount ")
            User_Instance.Deposit_Function()
            logging.info(" AC_NO : {},{} Credited Amount of {}".format(self.Ac_no,self.User_Name,self.Amount))
        except : 
            pass

    def Withdrawal_Module(self):
        try :
            logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,\
                    format = '%(asctime)s-%(levelname)s- WITHDRAW_HISTORY -%(message)s')
            self.Ac_no = input("\nEnter your Account Number: ")
            self.Password = getpass("\nEnter your password: ")
            self.Amount = int(input("\nEnter the amount you need to withdraw: "))
            for user in self.User_Dict:
                user_dict = self.User_Dict[user]
                for details in user_dict.values():
                    if self.Ac_no == details :
                        self.user = user
            user_balance = self.User_Dict[self.user]["Bank_Balance"]
            User_name = self.User_Dict[self.user]["Cus_Name"]
            if user_balance - self.Amount < 0 :
                print("\nYou have Insufficient Balance in your account")
                logging.error("{},{} tried debitting amount with insufficient balance".format(self.Ac_no,User_name))
            else:
                self.Amount_Withdrawn = self.Amount
                self.Remaining_Balance = user_balance - self.Amount
                print("\nAmount Withdrawn successfully")
            User_Instance.Withdraw_Function()
            User_Balance_Ask = input("\nDo you want to display the Balance ?(y/n) : ")
            if User_Balance_Ask == 'y' :
                print("\nRemaining Balance : {}".format(self.Remaining_Balance))
            else:
                pass
            logging.info(" AC_NO : {},{} Debited Amount of {}".format(self.Ac_no,User_name,self.Amount)) 
        
        except :
             pass

    def UPI_Module(self):
        try :
            logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,\
                    format = '%(asctime)s-%(levelname)s- UPI_TRANSFER -%(message)s')
            print("\nWelcome to UPI Payments Bank\n")
            self.UPI_User_Num = input("\nEnter your Mobile Number : ")
            if self.UPI_User_Num :
                mob_valid = re.search("[6789]\d{9}",self.UPI_User_Num)
                if mob_valid :
                    self.UPI_User_Num = self.UPI_User_Num
                else:
                    print("\nEnter valid Mobile Number ")    
                self.UPI_or_Mob = input("\nEnter UPI_id or mobile number you want to send money : ")
                if self.UPI_or_Mob :
                    self.Mob_number = 0
                    self.UPI_Id = 0
                    mob_valid = re.search("[6789]\d{9}",self.UPI_or_Mob)
                    if mob_valid :
                        self.Mob_number = self.UPI_or_Mob
                    UPI_valid = re.search("[a-z0-9]{1,15}@[a-z0-9]{1,15}",self.UPI_or_Mob)
                    if UPI_valid:
                        self.UPI_Id = self.UPI_or_Mob
                    if ( self.Mob_number == 0 and self.UPI_Id ==0 ):
                        print("\nEnter valid UPI ID or Mobile number\n")
                    for user in self.User_Dict:
                        user = self.User_Dict[user]
                        for details in user.values():
                            if ( self.Mob_number == details ) or ( self.UPI_Id == details ) :
                                self.user = user
                            if self.UPI_User_Num == details :
                                self.UPI_User = user
                    self.sender = self.User_Dict[self.UPI_User]["Cus_Name"] 
                    self.sender_AC_No = self.User_Dict[self.UPI_User]["Ac_No"]
                    self.send_recipient = self.User_Dict[self.user]["Cus_Name"]
                    self.Ac_num_to_transfer = self.User_Dict[self.user]["Ac_No"]
                    print("\nCustomer name : {}".format(self.send_recipient))
                    self.Amount_To_Send = int(input("\nEnter the amount you want to transfer : "))
                    if self.Amount_To_Send :
                        self.UPI_Pin_Check = int(getpass("\nEnter your four digit UPI PIN to continue : "))
                        if self.UPI_Pin_Check :
                            if self.User_Dict[self.UPI_User]["UPI_Pin"] == self.UPI_Pin_Check :
                                print("\nSuccessfully Sent Money")
                                User_Instance.UPI_Function()
                                Transaction_Id = "AX10105"+str(random.randrange(5000,6000))
                                print(f"\nYour Transaction ID : {Transaction_Id}")
                                logging.info("{} AC_No: {} sent amount of {} to {} AC_No: {} TxnId : {}"\
                                        .format(self.UPI_User_Num,self.sender_AC_No,self.Amount_To_Send\
                                        ,self.Mob_number,self.Ac_num_to_transfer,Transaction_Id))
                            else :
                                print("\nEnter the Correct UPI PIN ")
                                logging.error("{} Tried sending money with wrong UPI_PIN".format(self.UPI_User_Num))
                        UPI_Queue.put(self.UPI_User_Num)
                        UPI_Queue.put(self.Mob_number)
                        UPI_Queue.put(self.Amount_To_Send)
                        UPI_Queue.put(Transaction_Id)
                        UPI_Event.set()

        except:
            pass
class Customer(Online_Bank,Basic_Functions):
    def __init__(self,Json_File_Name):
        self.Json_File_Name = Json_File_Name
        User_Dict = Basic_Functions.Read_File(self.Json_File_Name)
        Associated_Account_Numbers_List = [User_Dict[User][details] for User in User_Dict for details in\
                User_Dict[User] if details == 'Ac_No']
        Online_Bank.__init__(self,User_Dict,Associated_Account_Numbers_List)


    def Deposit_Function(self):
        try :
            self.User_Dict[self.user]["Bank_Balance"] += self.Amount
            Basic_Functions.Write_File(self.Json_File_Name,self.User_Dict)
        except Exception as error:
            print("\nEnter the credentials correctly")
            
    def Withdraw_Function(self):
        try :
            if self.Remaining_Balance :
                self.User_Dict[self.user]["Bank_Balance"] = self.Remaining_Balance
                Basic_Functions.Write_File(self.Json_File_Name,self.User_Dict)
        except :
            print("\nEnter the credentials correctly")

    def UPI_Function(self):
        try :
            for user in self.User_Dict:
                user_dict = self.User_Dict[user]
                for details in user_dict.values():
                    if self.Ac_num_to_transfer == details :
                        self.user = user
                    if self.UPI_User == details :
                        self.UPI_User_username = user

            self.User_Dict[self.UPI_User]["Bank_Balance"] -= self.Amount_To_Send            
            self.User_Dict[self.user]["Bank_Balance"] += self.Amount_To_Send 
            Basic_Functions.Write_File(self.Json_File_Name,self.User_Dict)
        except :
            print("\nEnter the credentials correctly")

UPI_Event = threading.Event()
UPI_Queue = queue.Queue()

def UPI_Transaction_History():
    try :
        Main_Database = Json_handler.Basic_Functions.Read_File("server_entries.json")
        show_list = []
        UPI_Event.wait()
        for get_data in range(4):
            show_list.append(UPI_Queue.get())
        Sender_Number = show_list[0]
        Receiver_Number = show_list[1]
        Amount = show_list[2]
        Txn_Id = show_list[3]
        for user in Main_Database :
            user_dict = Main_Database[user]
            for details in user_dict.values():
                if Sender_Number == details :
                    Send_User = user
                if Receiver_Number == details :
                    Receive_User = user
        Sender_Ac_No = Main_Database[Send_User]["Ac_No"]
        Receiver_Ac_No = Main_Database[Receive_User]["Ac_No"]
        logging.info("{} AC_No : {} Received Amount of {} from {} AC_No : {} TxnId : {}".\
                format(Receiver_Number,Receiver_Ac_No,Amount,Sender_Number,Sender_Ac_No,Txn_Id))

    except :
        print("\nEnter the credentials correctly")

User_Instance = Customer("server_entries.json")
UPI_Transfer_Process = threading.Thread(target = User_Instance.UPI_Module)
UPI_Receiver_Process = threading.Thread(target = UPI_Transaction_History)

def View_Transaction_History():
    try :
        Mobile_Number = input("\nEnter your mobile number : ")
        with open("Test_log_Bank_Server.log","r") as log_file :
            log_list = (log_file.read()).split("\n")
        for log in log_list :
            #if (Mobile_Number and "UPI_TRANSFER") in log and ("ERROR" not in log) :
            if Mobile_Number in log and "UPI_TRANSFER" in log and "ERROR" not in log :
                start_index = log.find("UPI_TRANSFER")
                print(log[start_index:])
    except :
        print("\nEnter the credentials correctly")

def Balance_Check():
    Json_handler.Feature_Instance.Check_Bank_Balance()

def Mini_Statement():
    Json_handler.Feature_Instance.Check_Mini_Statement()

No_Of_Tries = 3

while No_Of_Tries > 0 :
    Password_Check = getpass("\nEnter Password to Enter : ")
    print()
    if Password_Check == "1234":
        while True :
            print()
            Txt_To_Display = "Welcome to Online Banking Service"
            Nxt_txt_to_display = """1) CASH_WITHDRAWAL
2) CASH_DEPOSIT
3) UPI_MONEY_TRANSFER
4) NEW_ACCOUNT_CREATE
5) BALANCE_ENQUIRY
6) MINI_STATEMENT
7) VIEW_UPI_TRANSACTION_HISTORY
                   """
            print(Nxt_txt_to_display)                              
    
            try :
                User_Option = int(input("\nWhat have you got to do. Select an option : "))
            except ValueError :
                print("\nEnter a Valid Input")
                continue
            
            if User_Option == 1 :
                User_Instance.Withdrawal_Module()
            elif User_Option == 2 :
                User_Instance.Deposit_Module()
            elif User_Option == 3 :
                UPI_Transfer_Process.start()
                UPI_Receiver_Process.start()
                break
            elif User_Option == 4 :
                print("\n*****Only Admin Can Add New Users*****")
                User_Check = getpass("\nEnter Password : ")
                if User_Check == 'admin' :
                    from New_User_Addition import Add_New_User
                else :
                    print("\nEnter the Correct Password")
            elif User_Option == 5 :
                Balance_Check()
            elif User_Option == 6 :
                Mini_Statement()
            elif User_Option == 7 :
                View_Transaction_History()
            elif User_Option > 7  or User_Option < 1:
                print("\nEnter a valid option")
                continue


            User_Continuation = int(input("\nDo You want to continue Banking.Press 1 to continue .0 to terminate : "))
            if User_Continuation == 1 :
                continue
            elif User_Continuation == 0 :
                print()
                Exit_txt = "Thanks for Banking with Us"
                print(Exit_txt.center(100))
                No_Of_Tries = -1
                break 
    else :
        if No_Of_Tries == 1:
            break
        print("\nEnter the correct password and try again")
    No_Of_Tries -= 1    

