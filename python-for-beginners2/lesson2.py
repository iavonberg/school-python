x = 2
y = 7
z = 10

if x > y:
    print(x, 'is greater than', y)

if x < y:
    print(x, 'is less than', y)

if x == y:
    print(x, 'is the same as', y)

if x < int('2'):
    print(x, "is less than 2")

if x <= y:
    print(x, 'is less than or equal to', y)

if z > y > x < z > y:
    print(z, 'is greater than', y, 'is greater than', x)

if x < y: 
    print(x, 'is less than', y)
if x > y:
    print(x, 'is greater than', y)
else:
    print(x, 'is not less than', y)

a = 3
b = 7
c = 10

if a > b or a < c:
    print('something here was the case')
elif a < c:
    print(a, 'is less than', c)
elif b < c:
    print(b, 'is less than', c)
else:
    print('nothing was the case')
