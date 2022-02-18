user = int(input())
even = user%2
check = user/2
if user > 0:
    if check != 1:
        if even == 0:
            print('yes')
        else:
            print("no")
    else:
        print("no")
else: print('no')