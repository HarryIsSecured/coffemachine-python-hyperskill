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

print('Write how many ml of water the coffee machine has:')
machine_water = int(input())
print('Write how many ml of milk the coffee machine has:')
machine_milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
machine_coffee = int(input())
print('Write how many cups of coffee you will need:')
n_coffees = int(input())

water = machine_water // min_water
milk = machine_milk // min_milk
coffee = machine_coffee // min_coffee
coffees = min(water, milk, coffee)

if coffees == n_coffees:
    print('Yes, I can make that amount of coffee')
elif coffees > n_coffees:
    more_coffee = coffees - n_coffees
    print('Yes, I can make that amount of coffee (and even '
          + str(more_coffee)
          + ' more than that)' )
else:
    print('No, I can only make '
          + str(coffees)
          + ' cups of coffee')
