# Ler o nome de uma cidade e dizer se ela começa com "Santo" ou não

cidade = input("Digite o nome de uma cidade: ").title()
cidadeS = cidade.split()
if 'Santo' in cidadeS[0]:
    print("Sua cidade começa com 'Santo'!")
else:
    print("Sua cidade não começa com 'Santo'!")
