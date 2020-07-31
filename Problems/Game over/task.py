scores = input().split()
# put your python code here
score = 0
lives = 3
for i in scores:
    if lives == 0:
        break
    if i == 'I':
        lives -= 1
    else:
        score += 1

if lives == 0:
    print('Game over')
else:
    print('You won')
print(score)
