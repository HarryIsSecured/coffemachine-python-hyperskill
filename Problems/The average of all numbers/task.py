# put your python code here
a = int(input())
b = int(input()) + 1
counter = 0
mean = 0

for i in range(a, b):
    if i % 3 == 0:
        counter += 1
        mean += i
print(mean / counter)
