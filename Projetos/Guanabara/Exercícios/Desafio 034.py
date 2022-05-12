# leia um salário e calcule o aumento. se o salário for 1250 ou mais, o aumento é de 10%. menos que isso, 15%

aumento = 0

salario = float(input("Digite um salário: "))

if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15

print(f"O aumento de seu salário foi de R${salario:.1f} para R${aumento:.1f}!")
