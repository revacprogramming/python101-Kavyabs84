
def add(a,b):
    z=  a+b
    return z
def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number:"))
    c = add(a,b)
    return c
s=main()
print("sum of two given number is",s)