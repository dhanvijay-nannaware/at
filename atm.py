card=input("select your card 1.ATM,2.credit card")
Balance=200000
if card=="1" or "2":
#    print("credit card")
    language=input("choose your language 1.english")
    if language=="1":
        # print("english")
        pin = int(input("enter the pin : 1234"))
        if pin == 1234:
            print("your pin is correct:")
            transaction=input("choose your transaction 1.withdrawal,2.balance enquiry")
            if transaction=="1":
                money=int(input("enter your money:"))
                if money>0 or money<200000:
                    if money%100==0:
                        print("Please collect your amount:rupees",money)
                        print("your total balance :rupees",Balance - money) 
                        reciept= input("you want reciept : please enter 1.yes ,2.no")
                        if reciept=="1":
                            print("card is credit card ,","your total balance",Balance)
                        else:
                            print("no")
            elif transaction == "2":
                    print("your balance is :rupees",Balance)
                    money=int(input("enter your money:"))
                    if money>0 or money<200000:
                        if money%100==0:
                            print("Please collect your amount:rupees",money)
                            print("your total balance :rupees",Balance - money) 
                            reciept= input("you want reciept : please enter 1.yes ,2.no")
                            if reciept=="1":
                               print("card is credit card ,","your total balance",Balance)
                            else:
                               print("no")
                        else:
                            print("enter valid amount:")
                    else:
                        print("enter correct amount:")         
            else:
                print("your moneys process is sucessfull,and safe your money:")
        else:
           print("enter correct pin:")
    else:
       print("it is only one language:")
else:
     print("invalid card:")
        



