# x = input("Enter your string: ")
x = "kajak"

b = int(1/2 * len(x) + 1)
for i in range(b):
    print(i)
    if x[i] == x[-i-1]: print('this is a palindrome')
    else: print("this is a not palindrome")



# jeżeli jeden z outputów jest nieprawidłowy to cały tekst nie jest palindromem
