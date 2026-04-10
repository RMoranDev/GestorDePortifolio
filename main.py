import sys
from time import sleep
from datetime import datetime
import json
import os

DADOS = 'dados.json'  # variavel global em maiúscula, melhor para manutenção depois.


# Definindo funções

# função para verificar e carregar os dados
def carregar_dados():
    if os.path.exists(DADOS):
        with open(DADOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return []  # senão existe o arquivo retorna uma lista vazia.


def limpar_tela():
    """
Limpa o terminal de forma compatível com Windows e Linux/Mac.
    """
    # 'nt' é para Windows e 'posix' é para Linux e macOS.

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def mostrar_menu():
    limpar_tela()
    print()
    print("-=" * 30)
    print(f"{'GESTOR DE PROJETOS':^60}")
    print("-=" * 30)
    print("[ 1 ] Add Project"
          "\n[ 2 ] List Projects"
          "\n[ 3 ] Update Projects"
          "\n[ 4 ] Delete Projects"
          "\n[ 5 ] About"
          "\n[ 6 ] Quit")


def opcao_add(lista):  # <-- dei um nome local à lista.
    while True:
        try:  # Trata erros.
            print("-" * 60)
            numero_projetos = int(input("Quantos projetos deseja cadastrar?"
                                        "\n[MÁXIMO: 10] "))
            if numero_projetos <= 0 or numero_projetos > 10:
                print(f"ERRO! Valor inválido!.")
                sleep(2)
                limpar_tela()
                continue
            else:
                for _ in range(numero_projetos):  # Dicionário dentro do loop
                    projeto = {
                        "nome": input("Nome do projeto: ").strip().title(),
                        "data": datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
                        "status": "Não iniciado"
                    }
                    print(f"Projeto: '{projeto['nome']}' cadastrado com sucesso.")
                    lista.append(projeto)  # guarda os projetos do dicionário local na lista.
                    salvar_dados()  # chama a função e salva os dados no arquivo em cada iteração.
                    sleep(2)
                break
        except ValueError:  # ValueError é um tipo de erro específico.
            print(f"ERRO! Digite apenas numeros inteiros.")
            print("-" * 60)


def opcao_list_project(lista):  # <-- dei um nome local à lista.
    if len(lista) == 0:
        print("-" * 60)
        print("Desculpe, não foi salvo nenhum projeto.")
        while True:
            limpar_tela()
            resposta_usuario = input("Quer adicionar um novo projeto agora? [S/N] ").strip().upper()
            if resposta_usuario in "S":
                opcao_add(lista)
                break
            elif resposta_usuario in "N":
                break
            else:
                print("-" * 60)
                print(f"ERRO! Responda apenas S ou N.")
    else:
        for projeto in lista:
            print(f"{'Projeto:':<10} {projeto['nome']:>22}")
            print(f"{'Data:':<10} {projeto['data']:>22}")
            print(f"{'Status:':<10} {projeto['status']:>22}")
            print("▪ " * 30)
    print("-" * 60)
    print("OPÇÕES")
    print("[1] Atualizar Projeto"
          "\n[2] Apagar Projeto")
    resposta_menu = input("O que deseja fazer? ")
    if resposta_menu == "1":
        opcao_update()
    if resposta_menu == "2":
        opcao_delete()


def opcao_update():
    if len(projetos_guardados) == 0:
        print("-" * 60)
        print("Sem projetos cadastrados para atualizar.")
        return  # encerra a função na hora e volta para o menu.
    else:
        while True:
            limpar_tela()
            menu_voltar()
            print(f"{'---------- Update Projects ----------':^60}")
            nome_busqueda = input("Digite o nome do projeto: ").strip().title()
            if nome_busqueda == "0":
                opcao_quit()
            if nome_busqueda == "1":
                return
            if not nome_busqueda: # Nome vazio.
                print("ERRO: O nome do projeto não pode estar vazio!")
                continue
            localizado = False  # Evita que o erro apareça na tela toda vez que o programa teste um nome.
            for projeto in projetos_guardados:
                if projeto['nome'] == nome_busqueda:
                    print(f"Projeto localizado: {projeto['nome']}")
                    while True:
                        novo_status = input(f"[1] Iniciado"
                                            f"\n[2] Concluído"
                                            f"\nSelecione um novo status: ").capitalize().strip()
                        if novo_status == "1":
                            projeto['status'] = 'Iniciado'
                            break
                        elif novo_status == "2":
                            projeto['status'] = 'Concluído'
                            break
                        else:
                            print("-" * 60)
                            print(f"Opção inválida. Tente novamente.")
                            continue
                    salvar_dados()
                    print("Atualizando status...")
                    sleep(1)
                    print("O status do projeto foi atulizado!")
                    return
            if not localizado:
                print("-" * 60)
                print(f"ERRO: O projeto '{nome_busqueda}' não foi localizado!")
                print("-" * 60)


def opcao_delete():
    if len(projetos_guardados) == 0:
        print(f"Nenhum projeto cadastrado")
        return
    while True:
        limpar_tela()
        menu_voltar()
        nome_busqueda = input("Digite o nome do projeto: ").strip().title()
        nome_remover = None
        if nome_busqueda == "0":
            opcao_quit()
        if nome_busqueda == "1":
            return
        if not nome_busqueda: # Nome vazio.
            print("ERRO: O nome do projeto não pode estar vazio!")
            continue
        for projeto in projetos_guardados:
            if projeto['nome'] == nome_busqueda:
                nome_remover = projeto
                break
        if isinstance(nome_remover, dict):
            print(f"Projeto localizado: {nome_remover['nome']}")
            while True:
                confirmacao = input("Deseja realmente excluir? [S/N] ").strip().lower()
                if not confirmacao in ["s", "n"]:
                    print("ERRO: OPÇÃO INVALIDA!")
                    print("TENTE NOVAMENTE!")
                    continue
                elif confirmacao == "s":
                    projetos_guardados.remove(nome_remover)
                    salvar_dados()
                    print("Removendo Projeto...")
                    sleep(1)
                    print(f"Projeto '{nome_remover['nome']}' removido com sucesso.")
                    print("Voltando...")
                    sleep(2)
                    return
                else:
                    break
        else:
            print(f"ERRO: Projeto '{nome_busqueda}' não encontrado!")


def opcao_about():
    print(f"{'---------- Version 1.1 ----------':^60}")
    print("Gestor de Projetos v1.0."
          "\nAutor: Ricardo Moran Software Solution."
          "\nE-mail: ricardo.moranc@gmail.com")
    input("\nPressione ENTER para voltar ao menu...")


def opcao_quit():
    print("-" * 60)
    print("Encerrando software...")
    sleep(1)
    print(f"Até logo!")
    sys.exit() # encerra o programa totalmente.


def menu_voltar():
    print("-" * 60)
    print("[0] sair."
          "\n[1] Voltar ao Menu principal.")
    print("-" * 60)


# Aqui salvo os dados no arquivo .json com o json.dump
def salvar_dados():
    with open(DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(projetos_guardados, arquivo, indent=4, ensure_ascii=False)


# Fim das funções.

projetos_guardados = carregar_dados() # Lista principal.

# Começo do programa.
while True:
    limpar_tela()
    mostrar_menu()
    comando = input("Digite um comando aqui: ").lower()  # .lower() no começo para evitar repetir o código.

    if comando == "1":
        opcao_add(projetos_guardados)  # aqui entrega a lista real na hora de chamar a função.
    elif comando == "2":
        opcao_list_project(projetos_guardados)
    elif comando == "3":
        opcao_update()
    elif comando == "4":
        opcao_delete()
    elif comando == "5":
        opcao_about()
    elif comando == "6":
        opcao_quit()
    else:
        print("-" * 60)
        print(f"Comando inválido. Tente novamente.")
