arr = []
x = 0
y= 0
for i in range(5):
    a = list(map(int, input().split()))
    arr.append(a)

for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            x= i
            y=j

print(abs((y-2))+abs((x-2)))

