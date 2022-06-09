# Network Programming
# https://www.py4e.com/lessons/network
filename = input("Enter filename:")
filename = "mbox-short.txt"
handle = open(filename)
d = dict()
lst = list()

for line in handle:
    if line.startswith("From "):
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1
    else:
            continue
            
for key,Value in  d.items():
    lst.append((key,Value))

lst.sort()
    
for key,Value in lst[:]:
    print(key,Value)