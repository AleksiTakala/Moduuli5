import random
import math
Maara = []
maara = int(input('Anna noppien lukumäärä '))
for maara in range(maara):
    Maara.append(random.randint(1,6))
    summa = sum(Maara)

print("Noppien yhteinen summa ", summa)

