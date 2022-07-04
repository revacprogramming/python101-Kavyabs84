class car:
    def __init__(self,year,company,model,speed,price):
        self.year=year
        self.company=company
        self.model=model
        self.speed=speed
        self.price=price
    def display_car_details(self):
        print(self.year,"\t",self.company,"\t",self.model,"\t",self.speed,"\t",self.price)
carobject=[]
n=int(input("How many car details you want to enter"))
for i in range(n):
    year=int(input("Enter Manufacturing year\n"))
    company=input("Enter Manufacturing Company\n")
    model=input("Enter Model\n")
    speed=float(input("Enter the speed\n"))
    price=float(input("Enter the price of Car\n"))
    carobject.append(car(year,company,model,speed,price))
print("Car Details are\n")
for obj in carobject:
    obj.display_car_details()