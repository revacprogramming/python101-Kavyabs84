# Regular Expressions
# https://www.py4e.com/lessons/regex
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print("file doesn't exist")
    
count = dict()
lst = list()

for line in handle:
    if not line.startswith("From:"):
        continue
    else:
        line=line.split()
        lst.append(line[1])
    
for words in lst:
    count[words] = count.get(words,0) + 1

bigcount = None
bigword = None

for word,value in count.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = word
        
print(bigword,bigcount)