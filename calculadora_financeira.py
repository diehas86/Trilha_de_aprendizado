#Definições de menu principal oferecendo opções para o usuario
def menu_principal():
    print("\n=== Calculadora Financeira ===")
    print(" Digite 1- Para Investimentos")
    print(" Digite 2 - Para Empréstimos e parcelamentos ")
    print(" DIgite 0 - Para sair")
    try:
        return int(input("Escolha uma opção: ").strip())
    except ValueError:
        print("Opção inválida. Por favor, digite um número existente.")
        return -1

#Definições do menu secundario para investimentos
def menu_investimentos():
    print("\n=== Menu de Investimentos ===")
    print(" Digite 1 - para juros simples")
    print(" Digite 2 - para juros compostos")
    print(" Digite 0 - para voltar para o menu principal")
    try:
        return int(input("Escolha uma opção: ").strip())
    except ValueError:
        print("Opção inválida. Por favor, digite um número existente.")
        return -1
#definir o loop do menu de investimentos
def rodando_menu_investimentos():
    while True:
        opcao = menu_investimentos()
        if opcao == 1:
            print ("Opção de juros simples definida")
            capital_c = (float(input("Digite o valor do investimento: ")))
            taxa_de_juros_i = (float(input("Digite a taxa de juros em (porcentagem %) ")))
            taxa = taxa_de_juros_i / 100
            tempo_t = (float(input("Digite o periodo de investimento em meses :")))
            juros_simples = capital_c * taxa * tempo_t
            montante = capital_c + juros_simples
            print(f" O valor do montante total após {tempo_t} meses é de R$ {montante:.2f}")
            break
        elif opcao == 2:
                 
           print("Opção de juros compostos definida")
           capital_c = (float(input("Digite o valor do investimento: ")))
           taxa_de_juros_i = (float(input("Digite a taxa de juros em (porcentagem %) ")))
           taxa = taxa_de_juros_i / 100
           tempo_t = (float(input("Digite o periodo de investimento em meses :")))
           juros_compostos = capital_c * ((1+ taxa)** tempo_t )
           print(f" O valor do montante total após {tempo_t} meses é de R$ {juros_compostos:.2f}")
           break
        else:
            print("Retornando ao menu principal...")
            break        

#Definição de menu de emprestimos 
def menu_emprestimos_parcelamentos():
    print("\n=== Menu de Empréstimos ===")
    print (" Digite 1 para empréstimo com juros")
    print (" Digite 2 - para parcelamento de dívidas")
    print (" Digite 0 - para retornar para menu principal")
    try:
        return int(input("Escolha uma opção: ").strip())
    except ValueError:
        print("Opção inválida. Por favor, digite um número existente.")
        return -1
def rodando_menu_emprestimos():  
    while True:
        opcao = menu_emprestimos_parcelamentos()
        if opcao == 1 :
           print("Opção de empréstimo com juros definida")
           capital_c = (float(input("Digite o valor do empréstimo: ")))
           taxa_de_juros_i = (float(input("Digite a taxa de juros em (porcentagem %) ")))
           taxa = taxa_de_juros_i / 100
           tempo_t = (float(input("Digite em quantos meses deseja parcelar: ")))
           juros = capital_c * ((1+ taxa)** tempo_t )
           print(f" O valor do montante total após {tempo_t} meses é de R$ {juros:.2f}")
           break
        elif opcao == 2 :          
           print("Opção de parcelamento com juros definida")
           capital_c = (float(input("Digite o valor total da divida: ")))
           taxa_de_juros_i = (float(input("Digite a taxa de juros em (porcentagem %) ")))
           taxa = taxa_de_juros_i / 100
           tempo_t = (float(input("Digite em quantos meses deseja parcelar: ")))
           juros = capital_c * ((1+ taxa)** tempo_t )
           parcelas = juros / tempo_t
           print(f" O valor do montante total após {tempo_t} meses é de R$ {juros:.2f} e cada parcela sera de R$ {parcelas:.2f}")
        elif opcao == 0:
              print("Retornando ao menu principal...")   
              break
def iniciar_calculadora():
    while True:
        opcao = menu_principal()
        if opcao == 1:
            rodando_menu_investimentos()
        elif opcao == 2:
            rodando_menu_emprestimos()
        elif opcao == 0:
           print  ("Saindo da calculadora financeira . Até Logo!!!") 
           break
        else:
            print ("Opção inválida. Por favor , tente novamente.")
            break
iniciar_calculadora()        





    
