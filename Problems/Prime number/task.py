num = int(input())
prime = False
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
        else:
            prime = True

if prime is True:
    print('This number is prime')
else:
    print('This number is not prime')
