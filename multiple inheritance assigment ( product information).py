#multiple inheritance
#product ( name , price)
#discount( percentage of discount)
#order( final price , warrenty)


print("WELCOME TO MAHA UPYOGI BHANDAR")
print("THANK YOU FOR CHOOSING US\n\n")
print("OUR Available best products are : oppo a83 , infinix g10 pro , Noise burds\n")
l = ['Oppo a83' , 'Infinix g10 pro' , 'Noise s100 burds' ]
p=int(input("Enter 1 to choose oppo a83 mobile phone \nEnter 2 to choose infinix g10 pro phone \nEnter 3 to choose noise company earbuds\n "))

class product():
    def name(self):
        if p==1:
            print("You choose : " , l[0])
        elif p==2:
            print("You choose : ", l[1])
        elif p==3:
            print("You choose : " , l[2])
        else:
            print("Please choose write option")
    def price(self):
        if p==1:
            print("It's price is : ₹19000 \nAdd 1 year warrenty card rate :₹1000 \nSIM with Fixed 3 month data ( 2GB per day) price is : ₹800\n")
        elif p==2:
            print("It's price is : ₹16000\nAdd 2 year warrenty card price : ₹1000 \nSIM with fixed 9 month Regular data (2 gb per day price) :₹1000\n")
        elif p==3:
            print("It's price is : ₹800 with 2 year warrwnty\n")
class discount():
    def p_discount(self):
        if p==1:
            print("Because of the MAHA SELL 25% discount on final price\n")
        elif p==2:
            print("Because of the MAHA SELL 20% discount on final price\n")
        elif p==3:
            print("Because of the MAHA SELL 50% discount on final price\n")
class order (product,discount):
    def finalprice(self):
        if p==1:
            print("So The Final Selling Price Of Oppo a83 Mobile Phone is : ₹15,600 rupees only" )
        elif p==2:
            print("So The Final Selling Price Of infinix g10 pro mobile phone is : ₹14,400 rupees only")
        elif p==3:
            print("So The Final Selling Price Of Noise s100 Earburds is : ₹400 rupees only")
    def warrenty(self):
        if p==1:
            print("Available with 1 Year warrenty ")
        if p==2:
            print("Available with 2 Year warrenty ")
        if p==3:
            print("Available with 2 Year warrenty ")
        
    
        

q=order()
q.name()
q.price()
q.p_discount()
q.warrenty()
q.finalprice()
        

