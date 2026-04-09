print(" === CALCULADOR DE MÉDIA === ")

rodadas = 10
soma = 0

while rodadas > 0:
    soma += float(input(f"[Rodada {rodadas}] Insira um valor: "))
    rodadas -= 1

print(f'A soma dos valores é: {soma}')