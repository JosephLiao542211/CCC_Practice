n,k = map(int, input().split())
a = list(map(int, input().split()))
num = a[k-1]
count = 0
for loop in a:
    if loop>= num and loop>0:
        count+=1
print(count)