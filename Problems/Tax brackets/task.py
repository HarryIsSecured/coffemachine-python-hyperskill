income = int(input())
percent = 0
calculated_tax = 0

if income < 15528:
    percent = 0
    calculated_tax = round(income / 100 * percent)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
elif income < 42708:
    percent = 15
    calculated_tax = round(income / 100 * percent)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
elif income < 132407:
    percent = 25
    calculated_tax = round(income / 100 * percent)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
else:
    percent = 28
    calculated_tax = round(income / 100 * percent)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
