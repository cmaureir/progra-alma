km_por_milla = 1.609344
cm_por_pulgada = 2.54

def miles_to_km(mi):
    return mi * km_por_milla

def km_to_miles(km):
    return km / km_por_milla

def inch_to_cm(p):
    return p * cm_por_pulgada

def cm_to_inches(cm):
    return cm / cm_por_pulgada

if __name__ == '__main__':
    print 'Choose the conversion'
    print '1) miles to kilometers'
    print '2) kilometers a miles'
    print '3) inch to centimeters'
    print '4) centimeters to inch'
    opcion = int(raw_input('> '))

    if opcion == 1:
        x = float(raw_input('Enter miles: '))
        print x, 'miles =', miles_to_km(x), 'km'
    elif opcion == 2:
        x = float(raw_input('Enter kilometers: '))
        print x, 'km =', km_to_miles(x), 'miles'
    elif opcion == 3:
        x = float(raw_input('Enter inchs: '))
        print x, 'in =', inch_to_cm(x), 'cm'
    elif opcion == 4:
        x = float(raw_input('Enter centimeters: '))
        print x, 'cm =', cm_to_inches(x), 'in'
    else:
        print 'Wrong option'
