kitty = 'a 0'
cat = ''
num = 0
while kitty != 'MEOW':
    cafe, number = kitty.split()
    number = int(number)
    if num < number:
        cat = cafe
        num = number
    kitty = input()

print(cat)
