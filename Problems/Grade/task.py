grade = int(input())
max_grade = int(input())
percentage = float((grade / max_grade) * 100)

if percentage < 60:
    print('F')
elif percentage < 70:
    print('D')
elif percentage < 80:
    print('C')
elif percentage < 90:
    print('B')
else:
    print('A')
