casos = int(input())
cont = int(0)
while (cont < casos):
    numero = int(input())
    if (numero > 0):
        if (numero%2 == 0):
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif (numero < 0):
        if (numero%2 == 0):
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    else:
        print("NULL")
    cont = cont + 1