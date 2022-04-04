import textwrap

import wikipedia as wk
import wikipedia.exceptions


def releated(txtToSearch):
    print('Related Searches: ')
    for i in range(len(wk.search(txtToSearch)) - 1):
        print(wk.search(txtToSearch)[i + 1])
    print('\n')


txtToSearch = input()
releated(txtToSearch)

g = open(r'C:\Users\janek\Desktop\test.txt', 'w')

try:
    text = wk.summary(txtToSearch)
    text = textwrap.fill(text, width=160)
    text = text.replace('. ', '.\n')
    print(text)
    g.write(text)
except wikipedia.exceptions.PageError:
    print('Try something else')
except UnicodeEncodeError:
    print('Unicode Error')
