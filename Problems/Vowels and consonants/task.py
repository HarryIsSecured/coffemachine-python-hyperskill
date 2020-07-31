words = input()
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
vowels = 'aeiouAEIOU'
for i in words:
    if i in vowels:
        print('vowel')
    elif i in consonants:
        print('consonant')
    else:
        break
