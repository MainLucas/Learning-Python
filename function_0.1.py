def mostrar_menu_principal():
    print("====MENU PRINCIPAL====")
    print("[1] Estudantes")
    print("[2] Turmas")
    print("[3] Disciplinas")
    print("[4] Professores")
    print("[5] Matriculas")
    print("[0] Sair")

    return  input("Digite uma opção: ")
def mostrar_menu_operacoes():
    print("====MENU OPERAÇÕES====")
    print("[1] Incluir")
    print("[2] Listar")
    print("[3] Editar")
    print("[4] Excluir")
    print("[0] Sair")
    
    return input("Digite uma opção: ")

def incluir_dados(lista):
    print("====INCLUIR====")
    nome = input("Digite seu nome: ")
    codigo_geral = input("Digite o código: ")
    cpf_geral = input("digite seu cpf")
    lista.append({
        "nome": nome,
        "codigo":codigo_geral,
        "cpf": cpf_geral 
    })
lista = []
while True:
    #DICA -> quando haver uma variavel em uma função, sempre colocar ela como um parâmetro (se ela já existir no código)
    menu = mostrar_menu_principal()

    if menu == "1":
        print(f"Você escolheu a opção {menu}")
        
        while True:
            operacoes = mostrar_menu_operacoes()
            if operacoes == "1":
                incluir_dados()
            if operacoes == "2":
                print("====LISTAR====")
                print(lista)

                

