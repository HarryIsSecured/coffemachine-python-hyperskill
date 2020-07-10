x = int(input())
y = int(input())

if x == 8:
    if y == 8:
        print(3)
    elif y == 1:
        print(3)
    else:
        print(5)
elif x == 1:
    if y == 8:
        print(3)
    elif y == 1:
        print(3)
    else:
        print(5)
elif y == 8:
    if x == 8:
        print(3)
    elif x == 1:
        print(3)
    else:
        print(5)
elif y == 1:
    if x == 8:
        print(3)
    elif x == 1:
        print(3)
    else:
        print(5)
else:
    print(8)
