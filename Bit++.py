a = int(input())
start = 0

for i in range(0,a):
    b = input()
    if b[1]== '+':
        start +=1
    else:
        start-=1
print(start)