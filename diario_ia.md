# Diário de Bordo de IA - Ricardo Moran

## 2026-03-23
### Objetivo do Dia: 
Adiconar a estrutura `while True` e o `break` no código.
### Desafio
Realoquei o `print(f"ATÉ LOGO")` que ficou fora do loop para dentro do comando `QUIT`.
### Melhorias pessoais
- Decidi implementar o `Try/Except` para tratar erros.
### Dificuldades
- Teve problemas para implementar o `try/except` de forma correta, o loop estava voltando ao começo.
- Foi necessário adicionar um `while True` para complementar o `try/except` e também um `break` ao receber uma entrada correta.
### Aprendizado 
- O uso do `while True` combinado ao `break` permite ao `try/except` não voltar ao loop principal.
- Aprendí que o `break` finaliza apenas o `while` no qual esta inserido.
## 2026-03-25
### Objetivo do Dia
- Criar menu de opcões mais interativo.
### O que fiz
- Criei uma interface numerada (1. add, 2. list Projects, 3. About, 4. Quit).
- Notei que um `break` estava dando erro dentro do `for`, realoquei para dentro do `else`.
### Desafios
- Teve dificuldades para entender a lógica certa do `break` combinado ao `try/except`. O programa estava voltando ao menu anterior.
### Aprendizado
- Aprendi que o `break` interrompe a execução e pode impedir que o tratamento de exceções seja finalizado corretamente se não for bem posicionado.