lista = []
menu = ()
menu_estudantes = ""
while True:
    
    print("\n *****MENU PRINCIPAL*****") 
    print("[1]Estudantes")
    print("[2]Disciplinas")
    print("[3]Professores")
    print("[4]Turmas")
    print("[5]Matrículas")
    print("[0]Sair")
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
            print("\n*****[ESTUDANTES] MENU DE OPERAÇÕES*****")
            print("[1] Incluir")
            print("[2] Listar")
            print("[3] Atualizar")
            print("[4] Excluir")
            print("[0] Voltar ao menu principal")
            menu_estudantes = input("Selecione uma opção válida: ")
            if menu_estudantes == "0":
                print("\n \nvoltando ao menu principal\n")
                break
            if menu_estudantes == "1":
                print("====inclusão====")
                nome_estudantes = input("digite um nome ")
                lista.append(nome_estudantes)
                input("Pressione ENTER para continuar")
            if menu_estudantes == "2":
                print("====Listar====")
                if len(lista) == 0:
                    print("Não há estudantes cadastrados")
                else:
                    print(lista)
                input ("Pressione Enter para continuar")
            if menu_estudantes == "3":
                print("\nEM DESENVOLVIMENTO")
                input("Pressione enter para voltar ao menu de [ESTUDANTES]\n")            
        if menu == "2":
            print("\nEM DESENVOLVIMENTO")
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




            



    

