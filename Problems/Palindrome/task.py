word = input()
backwards = ''
# backwards = word[::-1]

for i in reversed(word):
    backwards += i

if word == backwards:
    print('Palindrome')
else:
    print('Not palindrome')
