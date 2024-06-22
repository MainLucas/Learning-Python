#LISTAS 
lista_estudantes = []
lista_professores = []
lista_disciplinas = []
lista_turmas = []
lista_matricula = []



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
def menu_secundario_professores():
    print("\n*****[PROFESSORES] MENU DE OPERAÇÕES*****")
    print("[1] Incluir")
    print("[2] Listar")
    print("[3] Atualizar")
    print("[4] Excluir")
    print("[0] Voltar ao menu principal\n")
def menu_secundario_turmas():
    print("\n*****[TURMAS] MENU DE OPERAÇÕES*****")
    print("[1] Incluir")
    print("[2] Listar")
    print("[3] Atualizar")
    print("[4] Excluir")
    print("[0] Voltar ao menu principal\n")
def menu_secundario_matriculas():
    print("\n*****[MATRICULAS] MENU DE OPERAÇÕES*****")
    print("[1] Incluir")
    print("[2] Listar")
    print("[3] Atualizar")
    print("[4] Excluir")
    print("[0] Voltar ao menu principal\n")
def incluir_nomes():
    print("====inclusão====")
    nome_estudantes = input("digite um nome ")
    cpf = input("digite o seu cpf: ")
    estudantes = {
        "nome": nome_estudantes,
        "cpf": cpf
    }
    lista_estudantes.append(estudantes)
    input("Pressione ENTER para continuar")
    return lista_estudantes
def listar_nomes():
    if menu_estudantes == "2":
        print("====Listar====")
        if len(lista_estudantes) == 0:
            print("Não há estudantes cadastrados")
        else:
            for estudant in lista_estudantes:
                print(f"Nome do estudante: {estudant}")
        input ("Pressione Enter para continuar")
def atualizar_dados_nomes():
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
def excluindo_dados():
    nome_estudante_excluir = input("\nQual nome deseja excluir? ")
    if nome_estudante_excluir in lista_estudantes:
        lista_estudantes.remove(nome_estudante_excluir)
        print(f"{nome_estudante_excluir} excluido com sucesso!")
    else:
        print("O nome não está na lista!")
        input("Pressione enter para voltar ao menu de [ESTUDANTES]\n")
def voltar_menu_principal():
    print("Voltando ao menu principal")
    input("Pressione **ENTER**")
    
while True:
    menu_principal()
    menu = input("Escolha uma opção válida: ")
    if menu == "0" or menu == "1" or menu == "2" or menu == "3" or menu == "4" or menu == "5":
        print("\nOpção válida")
        input("Precione ENTER para continuar")
    if menu > "5":
        print("\nOPÇÃO INVÁLIDA")   
    if menu == "1":
        while True:
            menu_secundario_estudantes()
            menu_estudantes = input("Selecione uma opção válida: ")
            if menu_estudantes == "1":
                incluir_nomes()
                nomes1 = lista_estudantes
            if menu_estudantes == "2":
                listar_nomes(nomes1)
            if menu_estudantes == "3":
                atualizar_dados_nomes()
            if menu_estudantes == "4":
                excluindo_dados()
            if menu_estudantes == "0":
                voltar_menu_principal()
                break
                         
    
    if menu == "2":
        while True:
            menu_secundario_disciplinas()
            secundario_disciplinas = input("\nDigite uma opção válida: ")
            if secundario_disciplinas == "1":
                incluir_nomes()
                nomes2 = lista_estudantes
            if secundario_disciplinas == "2":
                if menu_estudantes == "2":
                    listar_nomes(nomes2)
                    
            if secundario_disciplinas == "0":
                print("Voltando ao MENU PRINCIPAL")
                input("Pressione **ENTER**")
                break      
    if menu == "3":
        while True:
            menu_secundario_professores()
            secundario_professores = int(input("digite uma opção válida: "))
            if secundario_professores == 1:
                print("\n====INCLUIR====")
                codigo_professor = int(input("Digite o código: "))
                nome_professor = str(input("Digite o nome: "))
                cpf_professor = str(input("Digite o cpf: "))

                dados_professores = {
                    "código": codigo_professor,
                    "nome": nome_professor,
                    "cpf": cpf_professor
                }
                lista_professores.append(dados_professores.values())
                input("\nPressione **ENTER** para voltar ao MENU DOS PROFESSORES")
            if secundario_professores == 2:
                if len(lista_professores) == 0:
                    print("\nestá lista está vazia")
                    print("Inclua algum dado para obter a lista.")
                else:
                    for z,k,v in lista_professores:
                        print("\n ---LISTA DE PROFESSORES---")
                        print(f"\nCódigo {z} Nome {k} CPF {v}")
                        input("Pressione **ENTER**")
            
            if secundario_professores == 0:
                print("Voltando ao MENU PRINCIPAL")
                input("Pressione **ENTER**")
                break       
    if menu == "4":
        while True:
            menu_secundario_turmas()
            secundario_turmas = input("\ndigite uma opção válida: ")
            if secundario_turmas == "1":
                print("\n====INCLUIR====")
                codigo_turma = int(input("Digite o código da turma: "))
                codigo_turma_professor = int(input("Digite o código do professor: "))
                codigo_turma_disciplina = int(input("Digite o código da disciplina: "))
                dados_turma = {
                    "código_turma": codigo_turma,
                    "código_turma_professor": codigo_turma_professor,
                    "código_turma_disciplina": codigo_turma_disciplina 
                }
                lista_turmas.append(dados_turma)
                input("\nPressione **ENTER**")
            
            if secundario_turmas == "2":
                print("\n ---LISTA DE TURMAS---")
                if len(lista_turmas) == 0:
                    print("\nEstá lista está vazia")
                    print("Inclua algum dado para obter a lista.")
                    input("\nPressione **ENTER** para voltar ao MENU DAS TURMAS\n")
                else:
                    for z,y,n in lista_turmas:
                        print(f"Código da turma: {z}, código do professor: {y}, código da disciplina: {n}")
                    input("Pressione **ENTER** para voltar ao MENU DAS TURMAS\n")
            if secundario_turmas == "3":
                codigo = int(input("Digite um código para editar: "))
                for turma in lista_turmas:
                    if turma["código_turma"] == codigo:
                        turma["código_turma_professor"] = input ("Digite o novo código do professor: ")
                        turma["código_turma_disciplina"] = input ("Digite o novo código da disciplina: ")
                        break
            if secundario_turmas == "4":
                remover_codigo_turma = input("Digite um código para remover.")
                
            if secundario_turmas == "0":
                print("Voltando ao MENU PRINCIPAL")
                input("Pressione **ENTER**")
                break  
    if menu == "5":
        while True:
            menu_secundario_matriculas()
            secundario_matriculas = input("\ndigite uma opção válida: ")
            if secundario_matriculas == "1":
                print("\n====INCLUIR====")
                codigo_turma_matricula = int(input("Digite o código da turma: "))
                codigo_estudante_matricula = int(input("Digite o código do estudante: "))
                dados_matriculas = {
                    "código_turma_matricula": codigo_turma_matricula,
                    "código_estudante_matricula": codigo_estudante_matricula
                }
                lista_matricula.append(dados_matriculas.values())
                input("\nPressione **ENTER**")
            if secundario_matriculas == "2":
                if len(lista_matricula) == 0:
                    print("\nEstá lista está vazia")
                    print("Inclua algum dado para obter a lista.")
                    input("\nPressione **ENTER** para voltar ao MENU DAS MATRICULAS\n")
                else:
                    print("\n ---LISTA DE TURMAS---")
                    for z,y in lista_matricula:
                        print(f"Código da turma: {z}, código do estudante: {y}")
                    input("Pressione **ENTER** para voltar ao MENU DAS MATRICULAS\n")
            if secundario_matriculas == "0":
                print("Voltando ao MENU PRINCIPAL")
                input("Pressione **ENTER**")
                break                
    if menu == "0":
        print("   _________________________")
        print("\n  |   O PROGRAMA ENCERROU   |")
        print("  |_________________________|")
        break 




        



    

