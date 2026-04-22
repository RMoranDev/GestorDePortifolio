# Diário de Bordo de IA - Ricardo Moran

## 2026-03-23
### Objetivo do Dia
Adiconar a estrutura `while True` e o `break` no código.
### Desafios
Realoquei o `print(f"ATÉ LOGO")` que ficou fora do loop para dentro do comando `QUIT`.
### Melhorias pessoais
- Decidi implementar o `Try/Except` para tratar erros.
### Dificuldades
- Teve problemas para implementar o `try/except` de forma correta, o loop estava voltando ao começo.
- Foi necessário adicionar um `while True` para complementar o `try/except` e também um `break` ao receber uma entrada correta.
### Aprendizado 
- O uso do `while True` combinado ao `break` permite ao `try/except` não voltar ao loop principal.
- Aprendí que o `break` finaliza apenas o `while` no qual está inserido.
## 2026-03-25
### Objetivo do Dia
- Criar menu de opcões mais interativo.
### O que fiz
- Criei uma interface numerada (1. add, 2. list Projects, 3. About, 4. Quit).
- Notei que um `break` estava dando erro dentro do `for`, realoquei para dentro do `else`.
- Adicionei um dicionário para guardar os dados.
- Configurei a opção de escolha 2 que serve para mostrar os dados guardados.
- Nova chave para o dicionário `cadastros['data']`, foi usado o comando `datetime.now().strftime()` para obter automáticamente a data já formatada, melhor que deixar o usuário digitar.
- Adicionei separações usando `print("-" * 60)` para melhorar o visual para o usuário.
- Iniciei a refatoração do sistema utilizando `def`
- Usei `.strip().upper()[0]` para eliminar espaços e pegar somente a primeira letra.
- tratei erros em `def opcao_list_project()`,
### Desafios
- Teve dificuldades para entender a lógica certa do `break` combinado ao `try/except`. O programa estava voltando ao menu anterior.
### Aprendizado
- Aprendi que o `break` interrompe a execução e pode impedir que o tratamento de exceções seja finalizado corretamente se não for bem posicionado.
- Melhorei o sistema para utilizar uma lista composta (list de dict). Fiquei feliz hoje por entender o uso do método `.copy()`.
- Comecei executar o meu conhecimento de funcões. Exelente saber que consegui comprender e executar o básico desta vez sem ajuda.
### 2026-03-27
### Objetivo do dia
- Implementar salvamento automático em JSON e organizar o histórico de commits via terminal.
- Adicionar função _**UPDATE**_.
### O que fiz
- importei o módulo `json`.
- importei o módulo `os` para dar um plus no programa e criar automáticamente o arquivo `json`.
- função salvar dados adicionada.
- primeiro projeto-piloto guardado.
- Lembrei de usar o `elif` dentro da função `opcao_list_project` caso o usuario não deseje cadastrar um novo projeto.
- refatorei o menu para adiconar a opção **UPDATE PROJECTS**
- Foi adicionado o `else` ao final do `white True` principal para tratar o erro de opção inválida.
- Funcão update:
  - `input()` adiconado.
  - flag sinalizadora evitar o programa escrever um erro por cada nome não encontrado.
- Foi criada a primeira _branch_ para proteger o código principal.
### Dificuldades
- Erro `cannot delete branch`: Entendi que não posso apagar a branch em que estou posicionado. Precisei dar checkout para a main antes.
### Desafios
- Implementar um arquivo `JSON` para não perder os dados.
- Terminar a função `opcao_list_project` ainda falta o `elif` para voltar ao menu principal.
- Criar a função _**UPDATE**_.
### Aprendizado
- Dominei o uso de commits detalhados (título e descrição) usando a flag _-m_ repetida no terminal.
- Entendi que o arquivo JSON só é criado fisicamente no disco após a primeira execução da função de escrita.
## 2026-04-03
### Objetivo do Dia
- Modularização: Transformação do bloco de carregamento de arquivos numa função dedicada `(carregar_dados)`.
- Refatoração do Cadastro: Movi a criação do dicionário projeto para dentro do loop for, eliminando a dependência de dicionários globais e do comando `.clear()`.
- Implementei uma trava de segurança `(if len == 0)` nas função _Update_.
### Aprendizado
- Entendi a diferença entre manipular um dicionário global e criar instâncias locais numa função. Isso evita que um dado "suje" o outro.
- Aprendi que salvar no disco `(salvar_dados)` num loop é mais seguro contra quedas de energia, mas salvar fora do loop é uma boa prática para não estressar o hardware.
## 2026-04-08
### Objetivo do dia
- Refatorar a função de exclusão de projetos, implementar persistência de dados segura e criar uma estrutura de menu reutilizável para evitar a repetição de código (DRY - Don't Repeat Yourself).
### O que fiz
- Refatoração da opcao_delete: implementação de um fluxo de confirmação robusto antes de remover dados.
- Criação da opcao_voltar: desenvolvimento de uma função utilitária que centraliza o input e as opções de navegação (Sair/Voltar) para ser usada por todo o sistema.
- Tratamento de Tipos: Uso do isinstance() para garantir que o programa não tente acessar atributos de variáveis nulas (None).
### Dificuldades
- Sinalização entre Funções: Entender que o return de uma função secundária não encerra a função principal. A solução foi usar o valor retornado como um "sinal" para a função pai.
- Avisos do Editor (Linter): Lidar com o erro Member 'None' does not have attribute, que foi resolvido com a validação explícita de tipo
- Fluxo de Repetição: Organizar os loops while para que o usuário não ficasse "preso" em menus redundantes após um erro de busca.
### Aprendizado
- Comunicação entre Escopos: Aprendi como passar informações de volta de uma função (return) e como a função chamadora deve interpretar esse dado para decidir o próximo passo.
- Programação Defensiva: A importância de validar se um objeto existe e se ele é do tipo esperado (dict) antes de tentar acessar as suas chaves.
- Arquitetura Modular: Percebi que isolar o visual e o input em funções separadas torna o código muito mais fácil de manter e expandir.
## 2026-04-14
### Objetivo do Dia
- Refatorar o código.
### O que fiz
- Adicionei proteção contra entradas vazias.
- Refatorei para conectar as funções `buscador_projetos` e `opcao_update`. Usei IA para aprender a fazer, realmente desconheço o conceito neste dia.
### Dificuldades
- Muita dificuldade na hora de juntar a funcionamento de duas funções.
- Muita dificuldade em conectar a função nova `buscador_projetos` com a função `opcao_update`.
### Aprendizado
- Modifiquei `if len(lista) == 0:` para `if not lista` estou aprendendo usar o `not`.
- Estou começcando esclarecer a ordem lógica de cada bloco.
## 2026-04-16
### Objetivo do Dia
- Refatorar o código.
### O que fiz
- Apaguei a função `limpar_tela`, percebi que teve que configurar o meu projeto no pycharm para rodar corretamente, isso não funcionaria en outro PC.
- Identifiquei e resolvi um bug da função `Update`.
- Arrumei a função `Delete`, faltava juntar com a função de buscador de nomes de projetos.
- Automatização do histórico.
### Aprendizado
- Cada função deve fazer a sua parte.
- A questão das tuplas não ficou clara. Teve que consultar uma IA para me explicar, entendi que arquivos JSON não tem tuplas e ele transforma as tuplas em Arrays, que seria as listas em Python.
## 2026-04-20
### Objetivo do Dia
- Adicionar ao programa a capacidade de verificar antes de adicionar se já existe um nome com esse mesmo projeto.
### O que fiz
- Teve que criar um while antes do dicionário somente para o nome do projeto, foi a unica forma que achei de poder manipular o dicionário. 
## 2026-04-22
### Objetivo do Dia
- Refatorar função de listar, esta faltando adicionar o histórico.
### O que fiz
- formatei a lista de histórico para ficar melhor exibida na tela.
- Eliminei a possibilidade de atualizar o status do projeto manualmente e fiz a automação do status direto ao adicionar o primeiro histórico.
- Admito ter usado IA para me lembrar de alguns conceitos sobre a mostra de listas, esqueci como mostrar apenas 1 item, 
### Aprendizado
- Lembrei que não preciso do `for` para mostar apenas um item do dicionário, apenas usar um `print` usando o nome do *projeto_encontrado* e a chave.
## "Especificamente, utilizei a IA para:

**Esclarecimento de Fluxo:** Compreender como o comando break e o continue afetam a execução dentro de loops aninhados com try/except.

**Depuração de Persistência:** Entender por que as tuplas do Python são convertidas em listas no formato JSON e como realizar o desempacotamento desses dados na função de listagem.

**Refatoração Lógica:** Validar a melhor forma de integrar a função de busca (buscador_projetos) com a função de atualização, garantindo a separação de responsabilidades."

Realmente fiz o meu trabalho usando `JSON` e funções quase desde o começo, mas ao chegar nas aulas de JSON foi quando consegui estudar e ver mais afundo com a sua explicação como funciona este tipo de arquivo e o seu código no Python, posso dizer que sabia que existia e que devia usar JSON, mas não sabia com totalidade o que significava cada palavra do cogido:
```python
with open(DADOS, 'w', encoding='utf-8') as arquivo:
    # O dump converte o objeto Python para o arquivo físico
    json.dump(projetos_guardados, arquivo, indent=4, ensure_ascii=False)
```   
- DADOS: é o nome do arquivo que queremos carregar.
- 'w': Abre em modo de escrita (write), que sobrescreve o arquivo com os dados atualizados.
- encoding='utf-8': Padrão de codificação que suporta caracteres globais.
- arquivo: Sería como a função with chama o arquivo dentro do seu escopo.
- indent=4: Garante a legibilidade do arquivo JSON.
- ensure_ascii=False: Permite a gravação de caracteres especiais (acentos).
    
## Observação de Integridade Acadêmica
Em conformidade com a Resolução nº 274/2024 – Consun, declaro que utilizei ferramentas de IA como suporte para esclarecimento de conceitos lógicos e auxílio na documentação deste diário. Durante o processo, atentei-me ao conceito de Half-Life e às diretrizes de similaridade impostas pela disciplina, garantindo a autoria e a originalidade da lógica implementada no código final.
