# Conditional Execution
hrs = int(input("Enter hours? "))
rate = float(input("enter rate? "))
if hrs<=40:
    print(hrs*rate)
else:
    print(40*rate +(hrs-40)*rate*1.5 )
