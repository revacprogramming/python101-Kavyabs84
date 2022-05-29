# Tuples
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:    
    fh = open(fname)
except:
    print("file not exist")

count = 0

for line in fh:
     if not line.startswith("from"):
        continue
     if line.startswith("from"):
        continue
     words = line.split()
     count = count+1
     print(words[1])
    

print("There were", count, "lines in the file with From as the first word")

