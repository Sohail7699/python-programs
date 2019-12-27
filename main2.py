import operations2
success=False

while success==False:
    try:
        a = input('Enter a value for a:: ')
        b = input('Enter a value for b:: ')
        o = input('Enter a operation(+,-,*,/):: ')
        if o=='+':
            print('Sum= ',operations2.add(a,b))
        elif o=='-':
            print('Difference= ',operations2.subtract(a,b))
        elif o=='*':
            print('Product= ',operations2.multiply(a, b))
        elif o=='/':
            print('Result of division= ',operations2.divide(a,b))
        else:
            print('The given operation is invalid. Please enter again.')
        success=True
    except:
        pass

    d = input('Do you wish to continue(Y/N)?')
    if d=='Y':
        success=False