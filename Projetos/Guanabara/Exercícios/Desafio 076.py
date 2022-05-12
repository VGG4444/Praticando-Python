# fazer uma tabulação de preços de mercado com uma tupla só

tabela = ('Queijo', 3, 'Salmão', 20, 'Olho de Cobra', 5.50, 'Rum de Guarma', 14.35)

print(f"        Tabela\n"
      f"{'='*25}\n"
      f"Item            Preço\n"
      f"{'='*25}\n"
      f"{tabela[0]}            R${tabela[1]}\n"
      f"{tabela[2]}            R${tabela[3]}\n"
      f"{tabela[4]}     R${tabela[5]}\n"
      f"{tabela[6]}     R${tabela[7]}\n")
