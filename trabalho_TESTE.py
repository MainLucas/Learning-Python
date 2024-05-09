lista_estudantes = []
menu = ()
menu_estudantes = ""
def menu_principal():
    print("\n *****MENU PRINCIPAL*****") 
    print("[1]Estudantes")
    print("[2]Disciplinas")
    print("[3]Professores")
    print("[4]Turmas")
    print("[5]Matrículas")
    print("[0]Sair")

def menu_secundario_estudantes():
    print("\n*****[ESTUDANTES] MENU DE OPERAÇÕES*****")
    print("[1] Incluir")
    print("[2] Listar")
    print("[3] Atualizar")
    print("[4] Excluir")
    print("[0] Voltar ao menu principal")

def menu_secundario_disciplinas():
    print("\n*****[DISCIPLINAS] MENU DE OPERAÇÕES*****")
    print("[1] Incluir")
    print("[2] Listar")
    print("[3] Atualizar")
    print("[4] Excluir")
    print("[0] Voltar ao menu principal")



while True:
    menu_principal()

    while True:
    
        menu = input("Escolha uma opção válida: ")
    
    
        if menu == "0" or menu == "1" or menu == "2" or menu == "3" or menu == "4" or menu == "5":
            print("\nOpção válida")
            input("Precione ENTER para continuar")
            break
                
                
        elif menu > "5":
            print("\nopção invalida, digite uma opção válida")
            input("pressione ENTER para continuar ")
            
            
    if menu == "0":
        print("O programa encerrou")
        break

    while True:
        if menu == "1":
            menu_secundario_estudantes()

            menu_estudantes = input("Selecione uma opção válida: ")
            if menu_estudantes == "0":
                print("\n \nvoltando ao menu principal\n")
                break
            if menu_estudantes == "1":
                print("====inclusão====")
                nome_estudantes = input("digite um nome ")
                lista_estudantes.append(nome_estudantes)
                input("Pressione ENTER para continuar")
            if menu_estudantes == "2":
                print("====Listar====")
                if len(lista_estudantes) == 0:
                    print("Não há estudantes cadastrados")
                else:
                    lista_estudantes.sort()
                    print(lista_estudantes)
                input ("Pressione Enter para continuar")
            if menu_estudantes == "3":
                print("\nATUALIZAR")
                if len(lista_estudantes) == 0:
                    print("Não há estudantes cadastrados")
                else:
                    for indice in range(len(lista_estudantes)):
                        print(f"indice[{indice}]  {lista_estudantes[indice]}")

                    
                    indice_selecionado_estudantes = input("Deseja alterar qual nome?")
                    if indice_selecionado_estudantes in lista_estudantes:
                        lista_estudantes.remove(indice_selecionado_estudantes)
                        print("digite o nome correto para atualizar!")
                        nome_estudantes = input("nome: ")
                        lista_estudantes.append(nome_estudantes)


                    else:
                        print("o nome não está na lista")
                        print(lista_estudantes)
            
            if menu_estudantes == "4":
                nome_estudante_excluir = input("\nQual nome deseja excluir? ")
                if nome_estudante_excluir in lista_estudantes:
                    lista_estudantes.remove(nome_estudante_excluir)
                    print(f"{nome_estudante_excluir} excluido com sucesso!")
                
                else:
                    print("O nome não está na lista!")
                    input("Pressione enter para voltar ao menu de [ESTUDANTES]\n") 


        if menu == "2":
            menu_secundario_disciplinas()
            input("Pressione enter para voltar ao Menu Principal\n")
            break
        if menu == "3":
            print("\nEM DESENVOLVIMENTO")
            input("Pressione enter para voltar ao Menu Principal\n")
            break
        if menu == "4":
            print("\nEM DESENVOLVIMENTO")
            input("Pressione enter para voltar ao Menu Principal\n")
            break
        if menu == "5":
            print("\nEM DESENVOLVIMENTO")
            input("Pressione enter para voltar ao Menu Principal\n")
            break

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaa


            



    

