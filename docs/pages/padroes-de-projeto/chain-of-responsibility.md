# <center> Chain Of Responsibility

## Histórico de versão

| Data       | Versão | Descrição                                                 | Autor       |
| ---------- | ------ | --------------------------------------------------------- | ----------- |
| 17/09/2021 | 0.1    | Criação do documento                                      | Rafael Leão |
| 17/09/2021 | 0.2    | Escrita do tópico de Introdução                           | Rafael Leão |
| 17/09/2021 | 1.0    | Escrita do tópico de Aplicação do Chain of Responsibility | Rafael Leão |

## 1. Introdução

Padrão que permite passar solicitações ao longo de uma cadeia de manipuladores. Ao receber uma solicitação, cada manipulador decide processar a solicitação ou passá-la para o próximo manipulador na cadeia. Ele evita o acoplamento do remetente de uma solicitação ao seu destinatários, dando a mais de um objeto a chance de tratar a solicitação. Encadeia os objetos receptores e passa a solicitação ao longo da cadeia até que um objeto a trate.

## 2. Aplicação do Chain of Responsibility

Para fazer as requisições ao Back-end da nossa aplicação estamos utilizando o _Axios_, que é um cliente HTTP simples baseado em promessas para o navegador e para o nodeJS. Axios fornece uma biblioteca simples de usar em um pacote pequeno com uma grande interface.

A aplicação do _Chain of Responsibility_ na nossa aplicação se refere ao uso dos interceptors do _Axios_. Quando a aplicação faz alguma requisição, ela é interceptada e há uma verificação do token de autenticação para decidir se o sistema dará prosseguimento com a ação seguinte ou não.

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/padroes-de-projeto/chain-of-responsibility/interceptor.png'>
  <figcaption align='center'>
      <b>Figura 1: Exemplo de uso do iterator na aplicação</b>
  </figcaption>    
</p>

### Bibliografia

[1] - https://www.dofactory.com/javascript/design-patterns/chain-of-responsibility último acesso em: 17/09/2021 às 10:49.
[2] - https://brizeno.wordpress.com/2011/11/09/mao-na-massa-chain-of-responsibility/ último acesso em: 17/09/2021 às 10:54.
[3] - https://unbarqdsw.github.io/2020.1_G12_Stock/#/DesignPatterns/ChainResponsibility último acesso em: 17/09/2021 às 11:02.
[4] - https://refactoring.guru/design-patterns/chain-of-responsibility último acesso em: 17/09/2021 às 11:15.
[5] - https://imasters.com.br/javascript/design-patterns-com-javascript-typescript-padroes-comportamentais último acesso em: 17/09/2021 11:21.
