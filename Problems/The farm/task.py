money = int(input())
chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
counter = 0

if money >= sheep:
    counter = int(money / sheep)
    print(str(counter) + ' sheep')
elif money >= cow:
    counter = int(money / cow)
    if counter <= 1:
        print(str(counter) + ' cow')
    else:
        print(str(counter) + ' cows')
elif money >= pig:
    counter = int(money / pig)
    if counter <= 1:
        print(str(counter) + ' pig')
    else:
        print(str(counter) + ' pigs')
elif money >= goat:
    counter = int(money / goat)
    if counter <= 1:
        print(str(counter) + ' goat')
    else:
        print(str(counter) + ' goats')
elif money >= chicken:
    counter = int(money / chicken)
    if counter <= 1:
        print(str(counter) + ' chicken')
    else:
        print(str(counter) + ' chickens')
else:
    print('None')
