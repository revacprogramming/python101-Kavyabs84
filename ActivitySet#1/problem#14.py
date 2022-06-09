# Using Web Services
# https://www.py4e.com/lessons/servces
import re
a=input("Enter the file name: ")
b=open(a)
c=re.findall("[0-9]+", b.read())
sum=sum([int(i) for i in c])
print(sum)