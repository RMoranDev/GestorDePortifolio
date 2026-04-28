import sys
from time import sleep
from datetime import datetime
import json


DADOS = 'dados.json'  # variavel global em maiúscula, melhor para manutenção depois.


# Definindo funções

# função para verificar e carregar os dados
def carregar_dados():
    try:
        with open(DADOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return [] # se o arquivo não existe retorna uma lista vazia.

    except json.JSONDecodeError:
        print(f"AVISO: O arquivo '{DADOS}' está corrompido. Iniciando lista vazia.")
        return [] # Arquivo corrompido retorna lista vazia também.


def titulo(texto):
    largura = len(texto) + 30
    print(f"-----{texto:^{largura}}-----")


def mostrar_menu():
    print()
    print("-=" * 30)
    print(f"{'GESTOR DE PROJETOS':^60}")
    print("-=" * 30)
    print("[ 1 ] Adicionar Projetos",
          "\n[ 2 ] Listar Projetos",
          "\n[ 3 ] Atualizar Projetos",
          "\n[ 4 ] Apagar Projetos",
          "\n[ 5 ] Estatísticas",
          "\n[ 6 ] Acerca de",
          "\n[ 7 ] Sair")
    escolha = input("\nDigite um comando aqui: ").strip()
    return escolha


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


def opcao_add(lista):
    print("\n" * 2)# <-- dei um nome local à lista.
    titulo('Cadastro de Projetos')
    numero_projetos = 0
    while True: # Aqui definimos o número de projetos.
        print("[0] para voltar ao menu principal.")
        entrada= input("Quantos projetos deseja cadastrar?" # Peguei o dado como str para poder tratar como vazio.
                                    "\n[MÁXIMO: 10] ").strip()
        if entrada == "0":
            return
        if not entrada:
            print(f"ERRO. Este campo não pode estar vazio.")
            print("-" * 60)
            continue
        try: # trata o erro deste bloco.
            numero_projetos = int(entrada) # A entrada str aqui vora int.
            if 0 < numero_projetos <= 10: # Condição de saída = True.
                break
            else:
                print(f"Valor inválido.") # Só é executado se a condição for False.
                print("-" * 60)
        except ValueError:  # ValueError é um tipo de erro específico.
            print(f"ERRO. Digite apenas números inteiros.")
            print("-" * 60)

    for i in range(numero_projetos):
        while True: # while dentro do for para o 'continue' funcionar.
            print(f"\n--- Cadastro do Projeto {i + 1}/{numero_projetos} ---")
            nome_projeto = input("Digite o nome do projeto: ").strip().title()

            if not nome_projeto: # Verifica se esta vazio.
                print("Erro: O nome não pode ser vazio.")
                continue

            if any(p['nome'] == nome_projeto for p in lista): # Esta linha verifica se já existe um projeto com o mesmo nome do que tento cadastrar.
                print(f"ERRO: O projeto '{nome_projeto}' já existe! Escolha outro nome.")
                continue

      # Dicionário dentro da função.
            projeto = {
                "nome": nome_projeto,
                "concluido": False,
                "historico": [],
                "data": datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
                "status": "Não iniciado"
            }
            lista.append(projeto) # guarda os projetos do dicionário local na lista.
            print(f"Projeto: '{nome_projeto}' cadastrado com sucesso.")
            print("-" * 60)
            break # Este break sai do while e volta para o 'for' e começa seguinte cadastro.
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


def opcao_list(lista):  # <-- dei um nome local à lista.
    titulo("Lista de Projetos")
    if not lista:
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
        if projeto['historico']:
            print(f"{'Histórico:':<10}")
            for data, acao, nome in projeto['historico']:
                print(f"  └─ {data} | {acao} | {nome}")
        print("▪ " * 30)

    while True:
        titulo("Opções")
        print("[1] Atualizar Projeto"
              "\n[2] Apagar Projeto"
              "\n[3] Voltar ao menu anterior")
        resposta_menu = input("O que deseja fazer? ").strip()
        if not resposta_menu:
            print("Desculpe, este campo não pode estar vazio.")
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
        print("\n[1] Adicionar histórico."
                "\n[2] Marcar como concluído."
                "\n[3] Voltar ao menu principal.")
        opcao_usuario = input("\nSelecione uma opção: ").strip()

        if not opcao_usuario:
            print("ERRO. Deve selecionar uma opção.")
            continue

        if not opcao_usuario in ["1", "2", "3"]:
            print("Opção invalida. Tente novamente.")
            continue

        if opcao_usuario == "1":
            projeto_encontrado = buscador_projetos(lista)

            if projeto_encontrado is None:
                print("Busca cancelada.")
                continue

            if projeto_encontrado['status'] == "Concluído":
                print(f"\nProjeto '{projeto_encontrado['nome']}' encontrado.")
                print("Este projeto já foi finalizado.")
                while True:
                    resposta = input("Deseja exibirlo? [S/N] ").strip().upper()

                    if not resposta in ["S", "N"]:
                        print("ERRO. Responda apenas S ou N.")
                        continue

                    if resposta in "S":
                        print()
                        print(f"{'Projeto:':<10} {projeto_encontrado['nome']:>22}")
                        print(f"{'Data:':<10} {projeto_encontrado['data']:>22}")
                        print(f"{'Status:':<10} {projeto_encontrado['status']:>22}")
                        print(f"{'Histórico:':<10}")
                        for data, acao, nome in projeto_encontrado['historico']:  # Desempacotamento
                            print(f"  └─ {data} | {acao} | {nome}")
                        input("Pressione ENTER para voltar ao menu principal.")
                        return
                    elif resposta in "N":
                        return

            if projeto_encontrado:
                print(f"Projeto: '{projeto_encontrado['nome']}' encontrado.")
                # Menu dentro da opção histórico.
                while True:
                    titulo("Adicionado Notas")
                    print("[0] Voltar ao menu anterior")

                    print(f"Digite uma anotação:")
                    anotacao = input("").capitalize().strip()
                    if anotacao == "0":
                        break
                    if not anotacao:
                        print("Este campo não pode ficar vazio.")
                        print("-" * 60)
                        continue
                    while True:
                        titulo("Adicionado Notas")
                        print(f"Digite o nome do desenvolvedor:")
                        nome_desenvolvedor = input("").title().strip()
                        if not nome_desenvolvedor:
                            print("Este campo não pode ficar vazio.")
                            print("-" * 60)
                            continue
                        break

                    if projeto_encontrado['status'] == "Não iniciado":
                        projeto_encontrado['status'] = "Iniciado"

                    data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    historico = (data, anotacao, nome_desenvolvedor)
                    projeto_encontrado['historico'].append(historico)
                    salvar_dados()
                    print(f"Anotação salva com sucesso!")
                    input("Pressione ENTER para voltar ao menu.")
                    break

        elif opcao_usuario == "2":
            projeto_encontrado = buscador_projetos(lista, "Marcar como Concluído")
            print(f"\nProjeto '{projeto_encontrado['nome']}' encontrado.")
            if projeto_encontrado['status'] == "Concluído":
                print("Este projeto já foi finalizado.")
                while True:
                    resposta = input("Deseja exibirlo? [S/N] ").strip().upper()

                    if not resposta in ["S", "N"]:
                        print("ERRO. Responda apenas S ou N.")
                        continue

                    if resposta in "S":
                        print()
                        print(f"{'Projeto:':<10} {projeto_encontrado['nome']:>22}")
                        print(f"{'Data:':<10} {projeto_encontrado['data']:>22}")
                        print(f"{'Status:':<10} {projeto_encontrado['status']:>22}")
                        print(f"{'Histórico:':<10}")
                        for data, acao, nome in projeto_encontrado['historico']:  # Desempacotamento
                            print(f"  └─ {data} | {acao} | {nome}")
                        input("Pressione ENTER para voltar ao menu principal.")
                        return
                    elif resposta in "N":
                        return
            if projeto_encontrado:
                while True:
                    resposta = input("Deseja realmente concluir este projeto? [S/N] ").strip().upper()
                    if not resposta in ["S", "N"]:
                        print("ERRO. Responda apenas S ou N.")
                        continue
                    if resposta in "S":
                        break
                    elif resposta in "N":
                        return
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

        elif opcao_usuario == "3":
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


def opcao_stats(lista):
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

    titulo("Estatísticas")
    print(f"Total de Projetos: {len(lista):>4}")

    projetos_em_andamento = 0
    projetos_concluidos = 0
    ultima_data_projeto = None

    for projeto in lista: # Um for é suficiente para verificar várias chaves.
        if projeto['status'] == 'Iniciado':
            projetos_em_andamento += 1

        elif projeto['status'] == 'Concluído':
            projetos_concluidos += 1

            data_atual = datetime.strptime(projeto['data'], '%d/%m/%Y - %H:%M:%S') # Aqui transforma a data num objeto.
            if ultima_data_projeto is None or data_atual > ultima_data_projeto:
                ultima_data_projeto = data_atual

    print(f"Projetos Iniciados: {projetos_em_andamento:>4}")
    print(f"Projetos finalizados: {projetos_concluidos:>4}")

    if ultima_data_projeto:
        data_formatada = ultima_data_projeto.strftime('%d/%m/%Y') # Formata a saída para ficar somente a data.
        print(f"Último projeto finalizado em: {data_formatada}")
    else:
        print("Última projeto finalizado em: 'Nenhum projeto finalizado'.")



    input("Pressione ENTER para voltar ao menu.")


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
    comando = mostrar_menu()

    if comando == "1":
        opcao_add(projetos_guardados)  # aqui entrega a lista real na hora de chamar a função.
    elif comando == "2":
        opcao_list(projetos_guardados)
    elif comando == "3":
        opcao_update(projetos_guardados)
    elif comando == "4":
        opcao_delete(projetos_guardados)
    elif comando == "5":
        opcao_stats(projetos_guardados)
    elif comando == "6":
        opcao_about()
    elif comando == "7":
        opcao_quit()
    else:
        print("-" * 60)
        print(f"Comando inválido. Tente novamente.")
