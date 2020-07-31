number = input()
numbers = []
while number != '.':
    numbers.append(float(number))
    number = input()
print(min(numbers))
