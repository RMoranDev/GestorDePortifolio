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


def titulo(texto):
    largura = len(texto) + 30
    print(f"-----{texto:^{largura}}-----")


def mostrar_menu():
    print()
    print("-=" * 30)
    print(f"{'GESTOR DE PROJETOS':^60}")
    print("-=" * 30)
    print("[ 1 ] Adicionar Projetos"
          "\n[ 2 ] Listar Projetos"
          "\n[ 3 ] Atualizar Projetos"
          "\n[ 4 ] Apagar Projetos"
          "\n[ 5 ] Acerca de"
          "\n[ 6 ] Sair")


def buscador_projetos(lista, operacao="Buscando Projetos"):
    while True:
        titulo(f"{operacao}")
        print("\n[0] para cancelar.")
        nome = input("Digite o nome do projeto: ").strip().title()

        if nome == '0':
            return None  # Indica que o usuário desistiu

        if not nome:
            print("Desculpe. O nome não pode estar vazio.")
            continue

        for projeto in lista:
            if projeto['nome'] == nome:
                return projeto
        # Auto aviso. Esse print só executados depois do for.
        print(f"\nDesculpe. Projeto '{nome}' não encontrado.")
        print("Tente novamente.")


def opcao_add(lista):  # <-- dei um nome local à lista.
    titulo('Cadastro de Projetos')
    numero_projetos = 0
    while True:
            entrada= input("Quantos projetos deseja cadastrar?"
                                        "\n[MÁXIMO: 10] ").strip()
            if not entrada:
                print(f"ERRO. Este campo não pode estar vazio.")
                print("-" * 60)
                continue
            try: # trata o erro deste bloco.
                numero_projetos = int(entrada)
                if 0 < numero_projetos <= 10: # Condição de saída = True.
                    break
                else:
                    print(f"Valor inválido.") # Só é executado se a condição for False.
                    print("-" * 60)
            except ValueError:  # ValueError é um tipo de erro específico.
                print(f"ERRO. Digite apenas números inteiros.")
                print("-" * 60)
    while True:
        nome_projeto = input("Digite o nome do projeto: ").strip().title()
        if not nome_projeto: # Verifica se esta vazio.
            print("Erro: O nome não pode ser vazio.")
            continue

        existe = False
        for p in lista: # Percorre a lista e verifica se já existe um projeto com esse nome.
            if p['nome'] == nome_projeto:
                existe = True
                break
        if existe:
            print(f"\nERRO: O projeto '{nome_projeto}' já existe! Escolha outro nome.")
        else:
            break # Senao existe sai do while.

    # Cadastro dos projetos.

    for _ in range(numero_projetos):  # Dicionário dentro da função.
        projeto = {
            "nome": nome_projeto,
            "concluido": False,
            "historico": [],
            "data": datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
            "status": "Não iniciado"
        }
        print(f"Projeto: '{projeto['nome']}' cadastrado com sucesso.")
        print("-" * 60)
        lista.append(projeto)  # guarda os projetos do dicionário local na lista.
    salvar_dados()  # chama a função e salva os dados no arquivo ao final para poupar recursos.
    while True:
        try: # Trata o erro deste bloco.
            continuar = int(input("[1] Novo Cadastro"
                  "\n[2] Voltar ao menu principal"
                  "\n[3] Sair"
                    "\n>>>>>  "))
            if continuar == 1:
                opcao_add(lista)
                return
            elif continuar == 2:
                return
            elif continuar == 3:
                opcao_quit()
                return
            else:
                print("Opção inválida. Tente novamente.")
                print("-" * 60)
        except ValueError:
            print(f"Entrada inválida. Tente novamente.")
            print("-" * 60)


def opcao_list_project(lista):  # <-- dei um nome local à lista.
    titulo("Lista de Projetos")
    if not lista:
        print("-" * 60)
        print("Desculpe, sem projetos cadastrados.")
        while True:
            resposta_usuario = input("Quer adicionar um novo projeto agora? [S/N] ").strip().upper()

            if not resposta_usuario:
                print("Desculpe este campo não pode estar vazio.")
                print("-" * 60)
                continue
            if resposta_usuario in "S":
                opcao_add(lista)
                return
            elif resposta_usuario in "N":
                return
            else:
                print("-" * 60)
                print(f"ERRO! Responda apenas S ou N.")

    for projeto in lista:
        print()
        print(f"{'Projeto:':<10} {projeto['nome']:>22}")
        print(f"{'Data:':<10} {projeto['data']:>22}")
        print(f"{'Status:':<10} {projeto['status']:>22}")
        print("▪ " * 30)
    while True:
        titulo("Opções")
        print("[1] Atualizar Projeto"
              "\n[2] Apagar Projeto"
              "\n[3] Voltar ao menu anterior")
        resposta_menu = input("O que deseja fazer? ").strip()
        if not resposta_menu:
            print("Desculpe este campo não pode estar vazio.")
            print("-" * 60)
            continue
        if resposta_menu == "1":
            opcao_update(lista)
            return
        elif resposta_menu == "2":
            opcao_delete(lista)
            return
        elif resposta_menu == "3":
            return
        else:
            print("Opção inválida.")


def opcao_update(lista):
    # Verificação inicial de lista vazia.
    if not lista: # Este bloco é ignorado se tiver projetos cadastrados.
        print("-" * 60)
        print("Sem projetos cadastrados para atualizar.")
        while True:
            resposta_usuario = input("Quer adicionar um novo projeto agora? [S/N] ").strip().upper()

            if not resposta_usuario:
                print("Este campo não pode estar vazio.")
                continue
            if resposta_usuario in "S":
                opcao_add(lista)
                return
            elif resposta_usuario in "N":
                return
            else:
                print("-" * 60)
                print(f"ERRO. Responda apenas S ou N.")

    # Começa aqui se tiver projetos cadastrados.
    while True:
        titulo("Atualizar Projetos")
        print("\n[1] Atualizar status"
                "\n[2] Adicionar histórico."
                "\n[3] Marcar como concluído."
                "\n[4] Voltar ao menu principal.")
        opcao_usuario = input("\nSelecione uma opção: ").strip()

        if not opcao_usuario:
            print("ERRO. Deve selecionar uma opção.")
            #titulo("Atualizar Projetos")
            continue

        if not opcao_usuario in ["1", "2", "3", "4"]:
            print("Opção invalida. Tente novamente.")

        if opcao_usuario == "1":
            projeto_encontrado = buscador_projetos(lista)  # Entra na função buscardor_projetos().

            if projeto_encontrado: # Uma condicional que é executada somente se teve retorno de algo.
                titulo("Atualizar Status")
                print(f"Projeto: {projeto_encontrado['nome']} encontrado.")

                # Menu dentro da opção status.
                while True:
                    print("[1] Não iniciado"
                          "\n[2] Iniciado")
                    novo_status = input("Selecione um novo status: ").strip()

                    if novo_status not in ["1", "2"]: # Validamos primeiro com not.
                        print(f"\nOpção inválida. Tente novamente.")
                        continue

                    status_mapeado = 'Não iniciado' if novo_status == "1" else 'Iniciado' # depois de validado o else sempre sera em teoria "2"

                    if status_mapeado == projeto_encontrado['status']:
                        print(f"O status já é '{status_mapeado}'.")
                        print("-" * 60)
                        continue

                    projeto_encontrado['status'] = status_mapeado
                    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    historico = (data, "Projeto Iniciado", projeto_encontrado['nome'])
                    projeto_encontrado['historico'].append(historico)
                    salvar_dados()
                    print(f"Status atualizado com sucesso!")
                    input("Presione ENTER para voltar ao menu.")
                    break

        elif opcao_usuario == "2":
            projeto_encontrado = buscador_projetos(lista)
            if projeto_encontrado:
                print(f"Projeto: {projeto_encontrado['nome']} encontrado.")
                # Menu dentro da opção histórico.
                while True:
                    titulo("Adicionado Notas")
                    print("[0] Voltar ao menu anterior")
                    print(f"Digite uma anotação")
                    anotacao = input("")
                    if anotacao == "0":
                        break
                    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    historico = (data, anotacao, projeto_encontrado['nome'])
                    projeto_encontrado['historico'].append(historico)
                    salvar_dados()
                    print(f"Projeto '{projeto_encontrado['nome']}' finalizado com sucesso!")
                    input("Pressione ENTER para voltar ao menu.")

        elif opcao_usuario == "3":
            projeto_encontrado = buscador_projetos(lista, "Marcar como Concluído")
            if projeto_encontrado:
                projeto_encontrado['concluido'] = True
                projeto_encontrado['status'] = "Concluído"
                # Isto "Automatiza" o histórico.
                data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                historico = (data, "Concluído", projeto_encontrado['nome'])
                projeto_encontrado['historico'].append(historico)
                salvar_dados()
                print(f"Projeto '{projeto_encontrado['nome']}' finalizado com sucesso!")
                input("Presione ENTER para voltar ao menu.")
                continue

        elif opcao_usuario == "4":
            return


def opcao_delete(lista):
    if not lista:
        print("-" * 60)
        print(f"Nenhum projeto cadastrado")
        while True:
            resposta_usuario = input("Quer adicionar um novo projeto agora? [S/N] ").strip().upper()

            if not resposta_usuario:
                print("Este campo não pode estar vazio.")
                continue
            if resposta_usuario in "S":
                opcao_add(lista)
                return
            elif resposta_usuario in "N":
                return
            else:
                print("-" * 60)
                print(f"ERRO. Responda apenas S ou N.")

    while True:
        projeto_encontrado = buscador_projetos(lista) # Chama a função.

        if isinstance(projeto_encontrado, dict):
            print(f"Projeto localizado: {projeto_encontrado['nome']}")
            while True:
                titulo("Apagando Projeto")
                confirmacao = input("\nDeseja realmente excluir? [S/N] ").strip().lower()
                if not confirmacao in ["s", "n"]:
                    print("ERRO: OPÇÃO INVALIDA!")
                    print("TENTE NOVAMENTE!")
                    continue
                elif confirmacao == "s":
                    projetos_guardados.remove(projeto_encontrado)
                    salvar_dados()
                    print("Removendo Projeto...")
                    sleep(1)
                    print(f"Projeto '{projeto_encontrado['nome']}' removido com sucesso.")
                    print("Voltando...")
                    sleep(2)
                    return
                else:
                    break


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


# Aqui salvo os dados no arquivo .json com o json.dump
def salvar_dados():
    with open(DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(projetos_guardados, arquivo, indent=4, ensure_ascii=False)


# Fim das funções.

projetos_guardados = carregar_dados() # Lista principal.

# Começo do programa.
while True:

    mostrar_menu()
    comando = input("Digite um comando aqui: ").lower()  # .lower() no começo para evitar repetir o código.

    if comando == "1":
        opcao_add(projetos_guardados)  # aqui entrega a lista real na hora de chamar a função.
    elif comando == "2":
        opcao_list_project(projetos_guardados)
    elif comando == "3":
        opcao_update(projetos_guardados)
    elif comando == "4":
        opcao_delete(projetos_guardados)
    elif comando == "5":
        opcao_about()
    elif comando == "6":
        opcao_quit()
    else:
        print("-" * 60)
        print(f"Comando inválido. Tente novamente.")
