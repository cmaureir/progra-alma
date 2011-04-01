n = int(raw_input('Enter n: '))
is_prime = True
for d in range(2, n):
    if n % d == 0:
        is_prime = False
    if is_prime:
        print n, 'is prime'
    else:
        print n, 'is not prime'
