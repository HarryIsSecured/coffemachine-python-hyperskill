# put your python code here
first_num = float(input())
second_num = float(input())
operation = input()

if operation == '+':
    print(first_num + second_num)
elif operation == '-':
    print(first_num - second_num)
elif operation == '/':
    if second_num == 0:
        print('Division by 0!')
    else:
        print(first_num / second_num)
elif operation == '*':
    print(first_num * second_num)
elif operation == 'mod':
    if second_num == 0:
        print('Division by 0!')
    else:
        print(first_num % second_num)
elif operation == 'pow':
    print(first_num ** second_num)
elif operation == 'div':
    if second_num == 0:
        print('Division by 0!')
    else:
        print(first_num // second_num)
