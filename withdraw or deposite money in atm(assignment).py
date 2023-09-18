code = 9925 #code need to login
def quit():
    print("have a nice day sir\ma'am")

def banks():
         c=int(input("enter your ATM code "))
         if c==code:
             print("hello RAHUL ... your balance is 5000 ")
             a=int(input("Enter 1 to Withdraw and enter 2 for Deposite money "))
             if a==1:
                  def withdraw():
                       m=int(input("Enter money to withdraw"))
                       if m>5000:
                           print("Please withdraw money below your available balance ")
                           z=int(input("Enter 1 to try again and any other option to quit "))
                           if z==1:
                                 banks()
                           else:
                                 print("quiting...................")
                                 
                       else:
                           print("Withdrawing is in process....")
                           print("Collect your money from below box.....")
                           print("Now left money in account is", 5000-m)
                  withdraw()
                  t=int(input("Enter 1 for further transitions or choose any other option for quit"))
                  if t==1:
                     banks()
                  else:
                     print("quiting...................")
                     quit()
                            
                        
             else:
                 if a==2:
                  
                  def deposite():
                       m=int(input("enter money to deposite"))
                       
                       print("deposite of money is in process")
                       print("now total money in account is", 5000+m)
                  deposite()

                 else :
                  print("please choose between 1 and 2 .........")

         else :
             print("wrong code")
             z=int(input("enter 1 to try again and any other option to quit"))
             if z==1:
                 banks()
             else:
                 print("quiting...................")
                 quit()
                 
                 
banks()