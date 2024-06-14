import time

l = []
k=3
amount=50000

def main():
    login()

def login():
    global l,amount,k
    acc_no = input("Please Enter Your Account Number:")
    pin = input("Please Enter Your ATM Pin:")
    if acc_no not in [i[0] for i in l] :
        l.append([acc_no, pin])
        print(f"Your Account ({acc_no}) not exists in our database\nJust registered your account in our database Successfully..")
        print('Now login with your newly registered Details...')
        login()
    else:
        for i in range(len(l)):                
            if l[i][0] == acc_no:
                if l[i][1] == pin:
                    print(f"Your Account ({acc_no}) Logged in Successfully")
                    while True:
                        print("1. DEPOSIT AMOUNT".ljust(30))
                        print("2. WITHDRAW AMOUNT".ljust(30))
                        print("3. CHECK YOUR BALANCE".ljust(30))
                        print("4. LOGOUT".ljust(30))
                        print()
                        ch = int(input(f"Enter Your Choice (1-4) 😊  :"))
                        if ch == 1:
                            d = int(input("Enter the amount you need to deposit:"))
                            time.sleep(0.5)
                            print(f"AMOUNT {d} deposited SUCCESSFULLY into your account ({acc_no})!!!")
                            time.sleep(1)
                            amount += d
                        elif ch == 2:
                            d = int(input("Enter the amount you need to Withdraw:"))
                            time.sleep(0.5)
                            print(f"AMOUNT {d} SUCCESSFULLY WITHDRAWN from your account ({acc_no})!!!")
                            time.sleep(1)
                            amount -= d
                        elif ch == 3:
                            time.sleep(0.5)
                            print(f"Balance of Account {acc_no} is {amount}")
                            time.sleep(1)
                        elif ch == 4:
                            print("LOGGING OUT....\nPlease Wait..")
                            time.sleep(1)
                            print('LOGGED OUT SUCCESSFULLY.....')
                            break
                        else:
                            print(f"Invalid choice. Please enter a number between 1 and 6.\nTRY AGAIN BRO")
                else:
                    print('You Entered Wrong Pin!!\nTry again!!')
                    time.sleep(1)
                    k-=1
                    if(k>0):
                        print(f'YOU HAVE {k} Tries left for login....')
                        login()
                    else:
                        print("(0/3)--You ran out of login chances...")
                        print("SORRY...")
                        time.sleep(1)
                        print("LOGGING OUT....")
                        time.sleep(1)
                        print('LOGGED OUT SUCCESSFULLY.....')
                        break
            else:
                pass

if __name__ == "__main__":
    print("WELCOME TO ATM INTERFACE".center(100,"-"))    
    print("Login to your account First!!".center(100,"-"))
    main()
