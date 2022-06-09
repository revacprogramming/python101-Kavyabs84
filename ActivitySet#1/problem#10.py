# Dictionaries
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words_split = line.split()
    for word in words_split:
        if word not in lst:
            lst.append(word)

     
lst.sort()
print(lst)
