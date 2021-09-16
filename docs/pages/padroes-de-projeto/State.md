# <center> State

## Histórico de versão

| Data       | Versão | Descrição                       | Autor       |
| ---------- | ------ | ------------------------------- | ----------- |
| 16/09/2021 | 0.1    | Criação do documento            | Rafael Leão |
| 16/09/2021 | 0.2    | Escrita do tópico de Introdução | Rafael Leão |
| 16/09/2021 | 1.0    | Explicação do useState          | Rafael Leão |

## 1. Introdução

O state é utilizado quando se precisa isolar o comportamento de um objeto, que depende de seu estado interno. O padrão elimina a necessidade de condicionais complexos e que frequentemente serão repetidos. Com o padrão cada “ramo” do condicional acaba se tornando um objeto, assim você pode tratar cada estado como se fosse um objeto de verdade, distribuindo a complexidade dos condicionais. [1]

## 2. useState

No nosso projeto foi utilizado o framework React Native para o Front-end. O React possui o useState, que é um hook específico que altera o estado interno de uma variável sem precisar implementar lógicas complexas.

Um dos exemplos na aplicação é a utilização do useState para manter variáveis que serão inputadas pelos usuários.

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/padroes-de-projeto/State/input.png'>
  <figcaption align='center'>
    <b>Figura 1: Exemplo de uso do state na aplicação</b>
  </figcaption>
</p>

### Bibliografia

[1] - https://www.dofactory.com/javascript/design-patterns/state# último acesso em: 16/09/2021 às 9:45.
[2] - https://brizeno.wordpress.com/category/padroes-de-projeto/state/ último acesso em: 16/09/2021 às 10:05.
[3] - https://unbarqdsw.github.io/2020.1_G12_Stock/#/DesignPatterns/State último acesso em: 16/09/2021 às 10:15.
