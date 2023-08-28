list1 = []
luku = 1
while luku != "":
    luku = input('Anna luku ')
    list1.append(luku)

list1d = sorted(list1, reverse = True)
print(list1d[:5])
