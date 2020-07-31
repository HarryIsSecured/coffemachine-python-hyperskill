# Write your code here
# print('Starting to make a coffee')
# print('Grinding coffee beans')
# print('Boiling water')
# print('Mixing boiled water with crushed coffee beans')
# print('Pouring coffee into the cup')
# print('Pouring some milk into the cup')
# print('Coffee is ready!')

min_water = int(200)
min_milk = int(50)
min_coffee = int(15)

# print('Write how many cups of coffee you will need:')
# number_of_coffees = int(input())
# print('For ' + str(number_of_coffees) + ' cups of coffee you will need:')
# print(str(number_of_coffees * water_for_coffee) + ' ml of water')
# print(str(number_of_coffees * milk_for_coffee) + ' ml of milk')
# print(str(number_of_coffees * coffee_beans) + ' g of coffee beans')

# print('Write how many ml of water the coffee machine has:')
# machine_water = int(input())
# print('Write how many ml of milk the coffee machine has:')
# machine_milk = int(input())
# print('Write how many grams of coffee beans the coffee machine has:')
# machine_coffee = int(input())
# print('Write how many cups of coffee you will need:')
# n_coffees = int(input())

# water = machine_water // min_water
# milk = machine_milk // min_milk
# coffee = machine_coffee // min_coffee
# coffees = min(water, milk, coffee)

# if coffees == n_coffees:
#    print('Yes, I can make that amount of coffee')
# elif coffees > n_coffees:
#    more_coffee = coffees - n_coffees
#    print('Yes, I can make that amount of coffee (and even '
#          + str(more_coffee)
#          + ' more than that)')
# else:
#    print('No, I can only make '
#           + str(coffees)
#          + ' cups of coffee')

m_water = 400
m_milk = 540
m_coffee = 120
m_cups = 9
m_money = 550


def main():
    print('Write action (buy, fill, take, remaining, exit')
    action = input()

    while True:
        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'remaining':
            remaining()
        elif action == 'exit':
            return
        else:
            print('Write action (buy, fill, take, remaining, exit')
        action = input()


def buy():
    global m_water, m_milk, m_coffee, m_cups, m_money
    print('What do you want to buy? "1" - espresso, "2" - latte, "3" - cappuccino '
          'or type "back" to go back:')
    purchase = input()
    if purchase == '1':
        water = 250
        milk = 0
        coffee = 16
        cups = 1
        price = 4
        make(water, milk, coffee, cups, price)
    elif purchase == '2':
        water = 350
        milk = 75
        coffee = 20
        cups = 1
        price = 7
        make(water, milk, coffee, cups, price)
    elif purchase == '3':
        water = 200
        milk = 100
        coffee = 12
        cups = 1
        price = 6
        make(water, milk, coffee, cups, price)
    elif purchase == 'back':
        return
    else:
        print('Sorry, that is not a valid option. '
              'Taking you back to the menu.')
        return


def make(water, milk, coffee, cups, price):
    global m_water, m_milk, m_coffee, m_cups, m_money
    if m_water >= water and m_coffee >= coffee and m_cups >= cups:
        print('I have enough resources, making you a coffee!')
        m_water -= water
        m_milk -= milk
        m_coffee -= coffee
        m_cups -= cups
        m_money += price
    else:
        print('Sorry, not enough ingredients for this product')


def fill():
    global m_water, m_milk, m_coffee, m_cups
    print('Write how many ml of water do you want to add:')
    m_water += int(input())
    print('Write how many ml of milk do you want to add:')
    m_milk += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    m_coffee += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    m_cups += int(input())


def take():
    global m_money
    print(f'I gave you ${m_money}')
    m_money = 0


def remaining():
    print('The coffee machine has:')
    print(f'{m_water} of water')
    print(f'{m_milk} of milk')
    print(f'{m_coffee} of coffee beans')
    print(f'{m_cups} of disposable cups')
    print(f'${m_money} of money')


main()
