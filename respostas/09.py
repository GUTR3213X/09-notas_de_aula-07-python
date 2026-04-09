print(" === SOMADOR DE NÚMEROS === ")

rodadas = 5
soma = 0

while rodadas > 0:
    soma += int(input(f"[Rodada {rodadas}] Insira um valor: "))
    rodadas -= 1

print(f'A soma dos valores é: {soma}')