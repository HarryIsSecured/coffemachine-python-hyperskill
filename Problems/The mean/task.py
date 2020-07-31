num = input()
total = 0
counter = 0
while num != '.':
    total += int(num)
    counter += 1
    num = input()
print(total / counter)
