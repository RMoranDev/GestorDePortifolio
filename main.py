from time import sleep
from datetime import datetime
import json
import os

# Definindo funções


def mostrar_menu():
    print()
    print("-=" * 30)
    print(f"{'GESTOR DE PROJETOS':^60}")
    print("-=" * 30)
    print("[ 1 ] Add Project"
          "\n[ 2 ] List Projects"
          "\n[ 3 ] Update Projects"
          "\n[ 4 ] About"
          "\n[ 5 ] Quit")


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
                    novo_cadastro["nome"] = nome_projeto = input("Nome do projeto: ").upper()
                    novo_cadastro["data"] = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
                    novo_cadastro["status"] = "Não iniciado"
                    print(f"Projeto: '{nome_projeto}' cadastrado com sucesso.")
                    projetos_guardados.append(novo_cadastro.copy())
                    salvar_dados() # chama a função e salva os dados no arquivo.
                    novo_cadastro.clear() # limpa o dicionário para não repetir os dados.
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
            elif resposta_usuario in "N":
                break
            else:
                print("-" * 60)
                print(f"ERRO! Responda apenas S ou N.")
    else:
        for projeto in projetos_guardados:
            print(f"Projeto: {projeto['nome']:<8}")
            print(f"Data: {projeto['data']}")
            print(f"Status: {projeto['status']}")
            print("▪ " * 30)


def opcao_update():
    print("-" * 60)
    nome_busqueda = input("Digite o nome do projeto: ").upper().strip()
    localizado = False # Evita que o erro apareça na tela toda vez que o programa teste um nome.
    for projeto in projetos_guardados:
        if projeto['nome'].upper() == nome_busqueda:
            localizado = True
            print(f"Projeto localizado: {projeto['nome']}")
            novo_status = input(f"Digite um novo status: (Ex: Iniciado, Concluído.): ").capitalize()
            projeto['status'] = novo_status
            salvar_dados()
            print("Atualizando status...")
            sleep(1)
            print("O status do projeto foi atulizado!")
            break

    if not localizado:
        print("-" * 60)
        print(f"ERRO: O projeto '{nome_busqueda}' não foi localizado.")

def opcao_about():
    print("-" * 60)
    print("Gestor de Projetos v1.0."
          "\nAutor: Ricardo Moran Software Solution." 
          "\nE-mail: ricardo.moranc@gmail.com")


def opcao_quit():
    print("-" * 60)
    print("Encerrando software...")
    sleep(1)
    print(f"Até logo!")


#Aqui salvo os dados no arquivo .json com o json.dump
def salvar_dados():
    with open(DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(projetos_guardados, arquivo, indent=4, ensure_ascii=False)


# Fim das funções.

DADOS = 'dados.json' # variavel global em maiúscula, melhor para manutenção depois.
projetos_guardados = list()

#verifica se o arqivo existe, senão, o cria automáticamente.
if os.path.exists(DADOS):
    with open(DADOS, 'r', encoding='utf-8') as arquivo:
        projetos_guardados = json.load(arquivo)

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
        opcao_update()
    elif comando == "4":
        opcao_about()
    elif comando == "5":
        opcao_quit()
        break
    else:
        print("-" * 60)
        print(f"Comando inválido. Tente novamente.")
