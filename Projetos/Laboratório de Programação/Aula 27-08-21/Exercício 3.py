meses=["janeiro", "fevereiro","março" , "abril", "maio", "junho",
       "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]


def mes_extenso(escrita_mes, extenso, mese):
    escrita_mes = meses[mese - 1]
    return escrita_mes


dia = int(input("Dia do Nascimento: "))
mes = int(input("Mês do Nascimento: "))
ano = int(input("Ano do Nascimento: "))
print(mes_extenso(mes))
