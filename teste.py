def opcao_update():
    if len(projetos_guardados) == 0:
        print("-" * 60)
        print("Sem projetos cadastrados para atualizar.")
        return  # encerra a fun��o na hora e volta para o menu.
    else:
        nome_busqueda = input("Digite o nome do projeto: ").strip().title()
        localizado = False  # Evita que o erro apare�a na tela toda vez que o programa teste um nome.
        for projeto in projetos_guardados:
            if projeto['nome'] == nome_busqueda:
                localizado = True
                print(f"Projeto localizado: {projeto['nome']}")
                novo_status = input(f"[1] Iniciado\n[2] Conclu�do\nSelecione um novo status: ").capitalize()
                if novo_status == "1":
                    novo_status = 'Iniciado'
                elif novo_status == "2":
                    novo_status = 'Concluido'
                else:
                    print("-" * 60)
                    print(f"Op��o inv�lida. Tente novamente.")
                projeto['status'] = novo_status
                salvar_dados()
                print("Atualizando status...")
                sleep(1)
                print("O status do projeto foi atulizado!")
                break
        if not localizado:
            print("-" * 60)
            print(f"ERRO: O projeto '{nome_busqueda}' n�o foi localizado.")
            print("-" * 60)
