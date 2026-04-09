print(" === CONTADOR PROFIOSSIONAL ===")

limite = int(input("Digite um número: "))

if limite >= 0:
    x = 1

    while x <= limite:
        print(x)
        x += 1
else:
    print('Você precisa inserir um número inteiro')