# tylko male litery
# nowa zmienna
# funkcje ord() i chr()
# for n in text


def szyfr(text, key):
    finalText = ''
    modulo = key % 26
    for i in text:

        if ord(i) == ord(' '):
            finalText += ' '
            continue

        if (ord(i) + modulo > ord('z')) or (ord(i) + modulo > ord('Z') and ord(i) < ord('a')):
            finalText += chr(ord(i) + modulo - 26)

        else:
            finalText += chr(ord(i) + modulo)

    return finalText


print('Write only english characters')
text = str(input('Write Your Text: '))
key = int(input('Set Your Key: '))

print(szyfr(text, key))
