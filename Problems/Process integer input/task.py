# put your python code here
num = int(input())
while num < 101:
    if num <= 9:
        num = int(input())
    elif num < 101:
        print(num)
        num = int(input())
    else:
        break
