# <center> Iterator

## Histórico de versão

| Data       | Versão | Descrição                                  | Autor       |
| ---------- | ------ | ------------------------------------------ | ----------- |
| 16/09/2021 | 0.1    | Criação do documento                       | Rafael Leão |
| 16/09/2021 | 0.2    | Escrita do tópico de Introdução            | Rafael Leão |
| 16/09/2021 | 1.0    | Escrita do tópico de Aplicação do Iterator | Rafael Leão |

## 1. Introdução

A ideia principal o iterator é permitir percorrer os elementos de uma coleção sem expor sua representação subjacente (lista, pilha, árvore etc.). A ideia principal do padrão é extrair o comportamento de passagem de uma coleção para um objeto separado denominado iterador.

Além de implementar o algoritmo em si, um objeto iterador encapsula todos os detalhes do percurso, como a posição atual e quantos elementos faltam para o final. Por causa disso, vários iteradores podem passar pela mesma coleção ao mesmo tempo, independentemente uns dos outros. Todos os iteradores devem implementar a mesma interface. Isso torna o código do cliente compatível com qualquer tipo de coleção ou qualquer algoritmo de passagem, desde que haja um iterador adequado. Se você precisa de uma maneira especial de percorrer uma coleção, basta criar uma nova classe iteradora, sem ter que alterar a coleção ou o cliente.

## 2. Aplicação do Iterator

Como o Front-end da nossa aplicação é feita na linguagem JavaScript, estamos utilizando uma abstração do padrão iterator. A linguagem JavaScript utiliza abstrações do padrão por meio de loops.

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/padroes-de-projeto/Iterator/iterator.png'>
  <figcaption align='center'>
      <b>Figura 1: Exemplo de uso do iterator na aplicação</b>
  </figcaption>    
</p>

### Bibliografia

[1] - https://www.dofactory.com/javascript/design-patterns/iterator último acesso em: 16/09/2021 às 11:05.
[2] - https://brizeno.wordpress.com/2011/09/15/mao-na-massa-iterator/ último acesso em: 16/09/2021 às 11:20.
[3] - https://unbarqdsw.github.io/2020.1_G12_Stock/#/DesignPatterns/Iterator último acesso em: 16/09/2021 às 11:25.
[4] - https://refactoring.guru/design-patterns/iterator último acesso em: 16/09/2021 às 11:29
