km_to_mile = 1.609344
cm_to_inch = 2.54

def miles_to_km(mi):
    return mi * km_to_mile

def km_to_miles(km):
    return km / km_to_mile

def inch_to_cm(p):
    return p * cm_to_inch

def cm_to_inches(cm):
    return cm / cm_to_inch

if __name__ == '__main__':
    print 'Choose the conversion'
    print '1) miles to kilometers'
    print '2) kilometers a miles'
    print '3) inch to centimeters'
    print '4) centimeters to inch'
    option = int(raw_input('> '))

    if option == 1:
        x = float(raw_input('Enter miles: '))
        print x, 'miles =', miles_to_km(x), 'km'
    elif option == 2:
        x = float(raw_input('Enter kilometers: '))
        print x, 'km =', km_to_miles(x), 'miles'
    elif option == 3:
        x = float(raw_input('Enter inchs: '))
        print x, 'in =', inch_to_cm(x), 'cm'
    elif option == 4:
        x = float(raw_input('Enter centimeters: '))
        print x, 'cm =', cm_to_inches(x), 'in'
    else:
        print 'Wrong option'
