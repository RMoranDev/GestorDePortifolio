from time import sleep
from datetime import datetime
cadastros = {}
while True:
    print("-=" * 30)
    print(f"{'GESTOR DE PROJETOS':^60}")
    print("-=" * 30)
    print(  "[ 1 ] Add Project"
          "\n[ 2 ] List Projects"
          "\n[ 3 ] About"
          "\n[ 4 ] Quit")
    comando = input("Digite um comando aqui: ").lower() # .lower() no começo para evitar repetir o código.

    if comando == "1":
        while True:
            try: # Trata erros.
                numero_projetos = int(input("Quantos projetos quer cadastrar?: "))
                if numero_projetos <= 0:
                    print(f"ERRO! Valor inválido!.")
                else:
                    for projetos in range(numero_projetos):
                        cadastros["nome"] = nome_projeto = input("Nome do projeto: ")
                        cadastros["data"] = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
                        print(f"Projeto: '{nome_projeto}' cadastrado com sucesso.")

                    break
            except ValueError:  # ValueError é um tipo de erro específico.
                print(f"ERRO! Digite apenas numeros inteiros.")

    elif comando == "2":
        print(cadastros)

    elif comando == "3":
        print("Gestor de Projetos v1.0."
              "\nAutor: Ricardo Moran Software Solution." 
              "\nE-mail: ricardo.moranc@gmail.com")

    elif comando == "4":
        print("Encerrando software...")
        sleep(1)
        print("Até logo!")
        break # finaliza o loop encerrando o programa.

    else:
        print("Comando não reconhecido.")