word = input()
output = ''
for i in word:
    if i.islower():
        output += i
    else:
        output += f'_{i.lower()}'
print(output)
