# złożoność liniowa - O(n)
# złożoność logarytmiczna O(logn)

tab = []
left = 0
right = 100
szukana = 31
def zloz(szukana):
    while left <= right:
        s = (left+right) // 2
        if tab[s] == szukana:
            print(s)

        elif szukana > tab[s]:
            left = s+1
        else:
            right = s-1
    return 1

