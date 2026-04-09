soma = 0
entrada = 1
while entrada < 0:
    entrada = int(input('Insira um número (que não seja negativo): '))
    if entrada >= 1: # Podia ser 0, mas não quis
        soma += entrada
print('Você digitou um número negativo. Fim.')
print(f'A soma dos valores é {soma}')