# Lists

filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fln = open(fname)
count=0
total=0

for line in fln:
    if not  line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count=count+1
        z=line.find('0')
        y=float(line[z:])
        total=total+y
asc=total/count             
        
print("Average spam confidence:",asc)