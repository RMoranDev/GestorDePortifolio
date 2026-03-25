from time import sleep
from datetime import datetime

# Definindo funções


def mostrar_menu():
    print("-=" * 30)
    print(f"{'GESTOR DE PROJETOS':^60}")
    print("-=" * 30)
    print("[ 1 ] Add Project"
          "\n[ 2 ] List Projects"
          "\n[ 3 ] About"
          "\n[ 4 ] Quit")


def opcao_add():
    while True:
        try: # Trata erros.
            print("-" * 60)
            numero_projetos = int(input("Quantos projetos quer cadastrar?: "))
            if numero_projetos <= 0:
                print(f"ERRO! Valor inválido!.")
                print("-" * 60)
                continue
            else:
                for projetos in range(numero_projetos):
                    novo_cadastro["nome"] = nome_projeto = input("Nome do projeto: ")
                    novo_cadastro["data"] = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
                    print(f"Projeto: '{nome_projeto}' cadastrado com sucesso.")
                    projetos_guardados.append(novo_cadastro.copy())
                    novo_cadastro.clear()
                break
        except ValueError:  # ValueError é um tipo de erro específico.
            print(f"ERRO! Digite apenas numeros inteiros.")
            print("-" * 60)


def opcao_list_project():
    if len(projetos_guardados) == 0:
        print("-" * 60)
        print("Desculpe, não foi salvo nenhum projeto.")
        while True:
            resposta_usuario = input("Quer adiconar um agora? [S/N] ").strip().upper()
            if resposta_usuario in "S":
                opcao_add()
                break
            else:
                print("-" * 60)
                print(f"ERRO! Responda apenas S ou N.")

    else:
        for projeto in projetos_guardados:
            print(f"Projeto: {projeto['nome']} - {projeto['data']}")


def opcao_about():
    print("Gestor de Projetos v1.0."
          "\nAutor: Ricardo Moran Software Solution." 
          "\nE-mail: ricardo.moranc@gmail.com")


def opcao_quit():
    print("-" * 60)
    print("Encerrando software...")
    sleep(1)
    print(f"Até logo!")

# Fim das funções.

projetos_guardados = list()
novo_cadastro = {}

# Começo do programa.
while True:
    mostrar_menu()
    comando = input("Digite um comando aqui: ").lower()  # .lower() no começo para evitar repetir o código.

    if comando == "1":
        opcao_add()
    elif comando == "2":
        opcao_list_project()
    elif comando == "3":
        opcao_about()
    elif comando == "4":
        opcao_quit()
        break
