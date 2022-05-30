# Tuples
fname = input("Enter file name: ")
    
try:    
    fh = open(fname)
except:
    print("file not exist")

count = 0

for line in fh:
    
	if line.startswith("From "):
		words = line.split()
		count = count+1
		print(words[1])
	else:
		continue
                 

print("There were", count, "lines in the file with From as the first word")
