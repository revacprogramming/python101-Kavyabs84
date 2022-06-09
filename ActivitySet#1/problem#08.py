text = "X-DSPAM-Confidence:0.8475 "
a = text.find('0')
b = text.find('a:')
value = text[a:b]
x=float(value)
print(x)
