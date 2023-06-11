import socket
client = socket.socket()
client.connect(('192.168.1.22',5005))


def Withdraw_Module():
    client.send((input("\nEnter your Account Number: ")).encode())
    client.send((input("\nEnter the amount you need to withdraw: ").encode()))
    try :
        Insufficient_msg = client.recv(1024).decode()
        print(Insufficient_msg)
    except :
        pass
    Balance_Show = input("\nDo you want to show the balance?(y/n) ")
    if Balance_Show == 'y' :
        client.send("Show_Balance".encode())
        print(client.recv(1024).decode())
    else :
        client.send("No Balance Show".encode())


def Deposit_Module():
    client.send((input("\nEnter your Account Number: ")).encode())
    client.send((input("\nEnter the amount you want to deposit: ")).encode())
    print(client.recv(1024).decode())

Services_Offered = """1.CASH_WITHDRAWAL
2.CASH_DEPOSIT"""

while True :
    print(Services_Offered)
    User_Option = int(input("\nEnter your choice: "))
    client.send(str(User_Option).encode())
    if User_Option == 1 :
        Withdraw_Module()
    elif User_Option == 2 :
        Deposit_Module()
    User_Opinion = int(input("\nDo you want to continue.Enter 2 to continue.0 to terminate :"))
    if User_Opinion == 0 :
        break

'''           
            for users in self.User_Dict:
                user = self.User_Dict[users]
                for details in user.values():
                    if self.Ac_no == details :
                        self.user_name = users
            user_balance = self.User_Dict[self.user_name]["Bank_Balance"]
            User_name = self.User_Dict[self.user_name]["Cus_Name"]
            if user_balance - self.Amount < 0 :
                print("\nYou have Insufficient Balance in your account")
                logging.error("{},{} tried debitting amount with insufficient balance".format(self.Ac_no,User_name))
            else:
                self.Amount_Withdrawn = self.Amount
                self.Remaining_Balance = user_balance - self.Amount
            print("\nAmount Withdrawn successfully")
            User_Balance_Ask = input("\nDo you want to display the Balance ?(y/n) : ")
            if User_Balance_Ask == 'y' :
                print("\nRemaining Balance : {}".format(self.Remaining_Balance))
            else:
                pass
            logging.info(" AC_NO : {},{} Debited Amount of {}".format(self.Ac_no,User_name,self.Amount))

        except :
            pass
'''
