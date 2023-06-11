import re
from Json_handler import Basic_Functions 
import logging

class Add_New_User(Basic_Functions):
    def __init__(self):
        logging.basicConfig(filename = 'Test_log_Bank_Server.log',level = logging.DEBUG,format = '%(asctime)s-%(levelname)s- NEW_ACCOUNT -%(message)s')
    def Get_Bio_Data(self):
        print()
        try:
            Welcome_Text = "Welcome to Adding New Account to Online Bank "
            print(Welcome_Text.center(100))
            self.First_Name = input("\nEnter your first Name.First Name should start with Capital letter and should not exceed 10 characters : ")
            Fname_Check = re.search("[A-Z][a-z]{2,10}",self.First_Name)
            if Fname_Check :
                self.First_Name = self.First_Name
            else : 
                print("\nPlease enter Valid First Name")
            self.Last_Name = input("\nEnter your Last Name.Last Name should start with Capital letter should not exceed 10 characters : ")
            Lname_Check = re.search("[A-Z][a-z]{2,10}",self.Last_Name)
            if Lname_Check :
                self.Last_Name = self.Last_Name 
            else :
                print("\nPlease enter Valid Last Name")
            self.Age = int(input("\nEnter your Age : "))
            self.Email = input("\nEnter your Email ID : ")
            Email_Check = re.search("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9-\-]+)\.([a-zA-Z]{2,5})$",self.Email)
            if Email_Check :
                self.Email = self.Email
            else :
                print("\nEnter a Valid Email")
            self.Mobile_Number = input("\nEnter your Mobile Number : ")
            mob_valid = re.search("[6789]\d{9}",self.Mobile_Number)
            if mob_valid :
                self.Mobile_Number = self.Mobile_Number
            else :
                print("\nEnter Valid mobile number")
            self.First_Deposit = int(input("\nEnter the amount you want to credit in your account : "))
            print("\nYou have successfully created Account")
       
        except :
            print("\nEnter the credentials correctly")

    def Update_Details(self):
        try :
            User_Credentials = Basic_Functions.Read_File("User_Credentials.json")
            User = User_Credentials["User"]
            New_User = {}
            New_User["Ac_No"] = str(User_Credentials["Account_Number"])
            New_User["First_Name"] = self.First_Name 
            New_User["Last_Name"] = self.Last_Name
            New_User["Cus_Name"] = self.First_Name + " " + self.Last_Name
            New_User["Age"] = self.Age
            New_User["Email"] = self.Email
            New_User["Mob_Num"] = self.Mobile_Number
            New_User["Bank_Balance"] = self.First_Deposit
            New_User["UPI_Id"] = self.First_Name + self.Last_Name + "@" + "ybl" + str(User_Credentials["UPI_Num"])
            New_User["UPI_Pin"] = User_Credentials["UPI_Pin"]
            Main_Database = Basic_Functions.Read_File("server_entries.json")
            Main_Database["User_"+str(User)] = New_User
            User_Credentials = {key : value+1 for key,value in User_Credentials.items()}
            Basic_Functions.Write_File("User_Credentials.json",User_Credentials)
            Basic_Functions.Write_File("server_entries.json",Main_Database)
            logging.info(" New Account created AC_No : {},{}".format(New_User["Ac_No"],New_User["Cus_Name"]))
        
        except :
            print("\nEnter the credentials correctly")

Add_Instance = Add_New_User()
Add_Instance.Get_Bio_Data()
Add_Instance.Update_Details()

