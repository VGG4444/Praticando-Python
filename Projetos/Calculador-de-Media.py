mediaValor = float(6.0)
continua = False
resultado = 0
recuperacao = False

print('Bem vindo ao Calculador de Média! \n'
      'A média atual está definida para 6. Deseja alterá-la?')
respostaAlt = str(input("(SIM ou NÃO) ").upper())
while continua is False:
    if respostaAlt == 'SIM':
        mediaValor = int(input('Qual a nova média? '))
        continua = True
    elif respostaAlt == 'NÃO':
        continua = True
    else:
        continua = False
        respostaAlt = str(input('Digite uma resposta válida! ').upper())
if continua is True:
    print('Digite "SAIR" para parar o programa.\n'
          'Dica: Use "." ao invés de "," para números reais!')
while continua is True:
    print(f'-------------------------------------------------------------------')
    aluno = (str(input('Nome do aluno: ').title()))
    if aluno == "Victor Gabriel Soares":
        print("Hmmm esse aí tá aprovado direto, sem problemas.")
        input("Tchau! ")
        break
    if aluno == "Vitor Gabriel Soares":
        print("Ao menos escreva 'Victor' com C  :(")
        input("Tchau! ")
        break
    if aluno == 'Sair':
        print('Obrigado por usar o programa de Calculador de Média!\n'
              'Criado por Victor Gabriel Soares.')
        input("Tchau! ")
        break
    nota1 = (float(input('Primeira nota: ')))
    nota2 = (float(input('Segunda nota: ')))
    soma = nota1+nota2
    media = soma/2
    print(f'-------------------------------------------------------------------')
    if media < mediaValor:
        resultado = 'em recuperação'
        recuperacao = True
    if media >= mediaValor:
        resultado = 'aprovado'
    print(f'{aluno} teve média {media} e está {resultado}! (Média {mediaValor})\n'
          f'Suas notas foram {nota1} e {nota2}')
    if recuperacao is True:
        print(f'O aluno {aluno} precisou de mais {(mediaValor-media):.2f} em sua média '
              f'({((mediaValor-media)*2):.2f} pontos em uma das notas).\n'
              f'{aluno} precisa de {(mediaValor*2)-media} na recuperação semestral.')
        if (mediaValor*2)-media > 10:
            print(f"{aluno} está na recuperação final! :(")
