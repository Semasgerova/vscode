try:
    a=float(input("Birinci ededi daxil edin: "))
    b=float(input("Ikinci ededi daxil edin: "))
    print("Emeliyyatlar: + - * /")
    c=input("Operatoru daxil edin: ")
    if c== '+':
        print('{} + {} ='.format(a,b),a+b)
    elif c== '-':
        print('{} - {} ='.format(a,b),a-b)
    elif c== '*':
        print('{} * {} ='.format(a,b),a*b)
    elif c== '/':
        print('{} / {} ='.format(a,b),a/b)
except ZeroDivisionError:
        print("0 bolmek olmaz!!!")
except ValueError:
        print("Reqem daxil edin!!!")