min = 256
text = str(input("Input your text: "))

for i in text:
    szukana = ord(i)
    if szukana < min:
        min = szukana

print(min)