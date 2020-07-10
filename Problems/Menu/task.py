pizza = 'Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy'
salad = 'Caesar salad, Green salad, Tuna salad, Fruit salad'
soup = 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'
food = input()

if food == 'pizza':
    print(pizza)
elif food == 'salad':
    print(salad)
elif food == 'soup':
    print(soup)
else:
    print("Sorry, we don't have it in the menu")
