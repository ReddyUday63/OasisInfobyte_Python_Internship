import time

class Commit_Rollback:
    def __init__(self):
        self.l=[]
        self.temp=[]
    def add_details(self):
        name=input("ENTER NAME OF YOUR WORK:")
        details=input("Enter Details:")
        time=input('Enter Date and time:')
        self.l.append([name,details,time])
        self.temp.append([name,details,time])
        print("DETAILS ADDED SUCCESSFULLYY..")
    def commit(self):
        if(len(self.temp)==0):
            print("ALL CHANGES ARE ALREADY COMMITED/SAVED...")
            print("NO DATA TO DISPLAY")
            print("ADD YOUR NEW WORK DETAILS NOW...")
        elif len(self.l):
            print("Data Saved Successfully...")
            print("Here is your schedule/Details....")
            for i in range(len(self.l)):
                print(i+1,'NAME'.center(20),"DETAILS".center(30),"TIME OF THE WORK".center(20))
                print()
                print(" ",self.l[i][0].center(20),self.l[i][1].center(30),self.l[i][2].center(20))
                print("--------------------------------------------------------------------------------------------")
        else:
            print("NO DATA TO DISPLAY")
  
        self.temp.clear()
    def rollback(self):
        if(len(self.temp)):
            self.l.pop()
            self.temp.pop()
            k=input("ROLL BACK DONE SUCCESSFULLY..If YOU WANT TO VIEW IT Type 'DISPLAY':")
            if k.upper()=="DISPLAY":
                if len(self.l):
                    for i in range(len(self.l)):
                        print(i+1,'NAME'.center(20),"DETAILS".center(30),"TIME OF THE WORK".center(20))
                        print()
                        print(" ",self.l[i][0].center(20),self.l[i][1].center(30),self.l[i][2].center(20))
                        print("--------------------------------------------------------------------------------------------")
                else:
                    print("NO DATA TO DISPLAY")
            else:
                print("You entered wrong! May be spelling Mistake!")
                
        else:
            print('THERE ARE NO PREVIOUS WORK DETAILS/CHANGES YOU MADE TO ROLLBACK..PLEASE ADD WORK DETAILS FIRST!!')
    def display(self):
        if len(self.l):
            for i in range(len(self.l)):
                print(i+1,'NAME'.center(20),"DETAILS".center(30),"TIME OF THE WORK".center(20))
                print()
                print(" ",self.l[i][0].center(20),self.l[i][1].center(30),self.l[i][2].center(20))
                print("--------------------------------------------------------------------------------------------")
        else:
            print("NO DATA TO DISPLAY")

ob=Commit_Rollback()       
            
def main():
    while True:
        print("1. ADD DETAILS OF YOUR WORK")
        print("2. COMMIT/SAVE ALL YOUR DETAILS OF YOUR WORK")
        print("3. ROLLBACK DETAILS OF YOUR WORK")
        print("4. DISPLAY ALL EXISTING DETAILS OF YOUR WORK")
        print('5. EXIT')
        ch=int(input('enter any choice(1-5):'))
        if(ch==1):
            ob.add_details()
        if(ch==2):
            ob.commit()
        if(ch==3):
            ob.rollback()
        if ch==4:
            ob.display()
        if ch==5:
            print("THANK YOU.....You are Exiting Commit and Rollback-MINI PROJECT by Uday!!!")
            time.sleep(1)
            break
if __name__=="__main__":
    main()