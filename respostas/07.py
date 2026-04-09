print(" === CONTA-SOMA PROFIOSSIONAL ===")

limite = int(input("Digite um número: "))

if limite >= 0:
    x = 1
    soma = 0

    while x <= limite:
        soma += x
        x += 1

    print(soma)
else:
    print('Você precisa inserir um número inteiro')