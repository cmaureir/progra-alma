a = float(raw_input('Enter a: '))
b = float(raw_input('Enter b: '))
c = float(raw_input('Enter c: '))

discriminante = b ** 2 - 4 * a * c
if discriminante < 0:
    print 'The equation does not have real solutions'
elif discriminante == 0:
    x = -b / (2 * a)
    print 'The unique solution is x =', x
else:
    x1 = (-b - (discriminante ** 0.5)) / (2 * a)
    x2 = (-b + (discriminante ** 0.5)) / (2 * a)
    print 'The real solution are:'
    print 'x1 =', x1
    print 'x2 =', x2

raw_input()
