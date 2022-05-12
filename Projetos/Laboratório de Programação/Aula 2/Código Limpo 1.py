nome = 0
contador = 0

while True:
    nome = input("Digite o número de entrada: ").capitalize()
    if nome == "Sair":
        break
    questao1 = input("Qual a alternativa da questão 1? ").lower()
    questao2 = input("Qual a alternativa da questão 2? ").lower()
    questao3 = input("Qual a alternativa da questão 3? ").lower()
    questao4 = input("Qual a alternativa da questão 4? ").lower()
    if questao1 != "a":
        print("(1) Resposta Errada! Alternativa 'A'")
    else:
        print("(1) Resposta Correta!")
    if questao2 != "b":
        print("(2) Resposta Errada! Alternativa 'B'")
    else:
        print("(2) Resposta Correta!")
    if questao3 != "c":
        print("(3) Resposta Errada! Alternativa 'C'")
    else:
        print("(3) Resposta Correta!")
    if questao4 != "d":
        print("(4) Resposta Errada! Alternativa 'D'")
    else:
        print("(4) Resposta Correta!")
