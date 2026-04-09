print(' === EXPONENCIADOR === ')

base = int(input("Insira a base: "))
expoente = int(input("Insira o expoente: "))
i = 1
resultado = 1
if expoente >= 0:
    while i <= expoente:
        resultado *= base
        i += 1
    print(resultado)