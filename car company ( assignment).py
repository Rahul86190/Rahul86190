#multi level inheritence

#made a vehicle class ( model, year)
#       car (fuel type, mailage)
#       e-car ( battery capacity, charging capacity)


print("WELCOME TO RAHUL'S NATION CAR COMPANY")
print("NOW Available car models are : Lamborgini , Ferrari , Thar \n\n") 
c=int(input("Press 1 for Lamborgini \nPress 2 for Ferrari \nPress 3 for Thar\n\n"))
m=['Lamborgini','Ferrari', 'Thar' ]
class vehicle:
    def model(self):
        if c==1:
            print("Choosed Car model is : ", m[0])
        elif c==2:
            print("Choosed Car model is : ", m[1])
        elif c==3:
            print("Choosed Car model is : " , m[2])
        else:
            print("please choose write available option")
            
          
    def year(self):
       
        if c==1: 
            print("Latest Lamborgani is  = 2023 LAMBORGINI Urus white color model \n")
            
        elif c==2:
            print("Latest Ferrari model is = Ferrari SF90 2022 plug-in hydric car in black color model\n")
        elif c==3:
            print("Latest Thar model is =  THAR Napoli nevy blue color model\n")
        
            
class car(vehicle):
    def fuel(self):
        if c==1:
            print("Available in diesel-fuel mode \n")
        elif c==2:
            print("Available in electric and diesel mode \n")
        elif c==3:
            print("Availabe in petrol mode and diesel mode \n")
    def mailage(self):
        if c==1:
            print("Mileage is 7.69kmpl (kilometers per litre) \n")
        elif c==2:
            print("Mileage is 16.39kmpl (kilometers per litre) in electric mode and 8.77kmpl in diesel mode \n ")
        elif c==3:
            print("Mileage is 9.0kmpl (kilometers per litre) in petrol mode and 15.2 in diesel mode \n")

class e_car(car):
    def battery(self):
        if c==1:
            print("Battery capacity is 3.8kwh (kilowatt hour)")
            print("Engine size : 3996 cc\n")
        if c==2:
            print("Battery capacity is 7.5kwh (kilowatt hour) for electric mode and 3.45kwh for diesel mode ")
            print("Engine size : 2990 cc\n")
        if c==3:
             print("Battery capacity is 6.5kwh (kilowatt hour) for petrol mode and 4.32kwh for diesel mode ")
             print("Engine size : 2184 cc\n")
    def char_capacity(self):
        if c==1:
            print("65W Ultra Fast Type-C Charger Use For lamborgini battery \n")
        elif c==2:
            print("Charging : on-board charger 3.5kW for electric mode \n")
        elif c==3:
            print("Available in 35AH  battery charging capacity \n")
    def price(self):
        if c==1:
            print("Price is : ₹4.18 Cr ( on road price) ")
            print("Available With 3 year warrenty (unlimited kms) \n")
            print("Book Now And Enjoy Other Best Offers ")
        elif c==2:
            print("Price is : ₹8.86 Cr (on road price) ")
            print("Available With 3 year warrenty (unlimited kms) \n")
            print("Book Now And Enjoy Other Best Offers ")
        elif c==3:
            print("Price is : ₹16.77 lakh (on road price )")
            print("Available With 2 Year warrenty ( per 100000 kms ) \n")
            print("Book Now And Enjoy Other Best Offers ")
e=e_car()
e.model()
e.year()
e.fuel()
e.mailage()
e.battery()
e.char_capacity()
e.price()
z=car() 
z.year()#proved that it is multi level inheritence

