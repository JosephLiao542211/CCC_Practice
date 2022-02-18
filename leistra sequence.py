import random
a = 5743183901534820710161992
counter = 0
for i in range(40):
    if a%(9+i) == 0:
        if (9+i)%2 == 0:
            print(9+i)
            counter+=1
print(counter)