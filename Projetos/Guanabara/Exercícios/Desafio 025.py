# Ler um nome e dizer se ele tem "Silva"

nome = input("Digite um nome: ").title()
if "Silva" in nome:
    print("Tem 'Silva' no nome!")
else:
    print("Não tem 'Silva' no nome!")
