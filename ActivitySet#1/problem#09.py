# Lists

filename = "mbox-short.txt"
count = 0
total = 0
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
  	print("file is not found")

for line in fh:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	else:
		count = count+1
		x = line.find(":")
		y = float(line[x+1:])
		total = total + y
		
avg = total/count            
print("Average spam confidence:",avg)

