# put your python code here
n = int(input())
k = 0
total = n
while total != 0:
    k += pow(n, 2)
    n = int(input())
    total += n
else:
    k += pow(n, 2)
    print(k)
