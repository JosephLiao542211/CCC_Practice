a = int(input())
for i in range(0,a):
    word = input()
    if len(word) > 10:
        print(word[0],len(word)-2,word[-1],sep="")
    else:
        print(word)
