from time import sleep
while True:
    comando = input("Digite um comando aqui: ").lower() # .lower() no começo para evitar repetir o código.

    if comando == "about":
        print("Gestor de Projetos v1.0\nAutor: Ricardo Moran Software Solution.\nE-mail: ricardo.moranc@gmail.com")

    elif comando == "quit":
        print("Encerrando software...")
        sleep(1)
        print("Até logo!")
        break # finaliza o loop encerrando o programa.

    elif comando == "add":
        while True:
            try: # Trata erros.
                numero_projetos = int(input("Quantos projetos quer cadastrar?: "))
                if numero_projetos <= 0:
                    print(f"ERRO! Não pode ser um valor negativo.")
                else:
                    for projetos in range(numero_projetos):
                        nome_projeto = str(input("Digite o nome do projeto: "))
                        print(f"Projeto: [{nome_projeto}] cadastrado com sucesso.")
                        break
            except ValueError: # ValueError é um tipo de erro específico.
                print(f"ERRO! Digite apenas numeros inteiros.")

    else:
        print("Comando não reconhecido.")

print(f"hjola")