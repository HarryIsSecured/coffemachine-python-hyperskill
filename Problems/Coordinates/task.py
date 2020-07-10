x = float(input())
y = float(input())
z = 0.0

if (x > z) & (y > z):
    print('I')
elif (x < z) & (y > z):
    print('II')
elif (x < z) & (y < z):
    print('III')
else:
    print('IV')
