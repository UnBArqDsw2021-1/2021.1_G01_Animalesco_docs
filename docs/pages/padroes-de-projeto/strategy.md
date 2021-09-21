# <center> Strategy

## Histórico de versão

| Data       | Versão | Descrição                                  | Autor       |
| ---------- | ------ | ------------------------------------------ | ----------- |
| 17/09/2021 | 0.1    | Criação do documento                       | Rafael Leão |
| 17/09/2021 | 0.2    | Escrita do tópico de Introdução            | Rafael Leão |
| 17/09/2021 | 1.0    | Escrita do tópico de Aplicação do Strategy | Rafael Leão |

## 1. Introdução

Permite que você defina uma família de algoritmos, coloque-os em classes separadas, e faça os objetos deles intercambiáveis. [2]

O padrão Strategy, além de encapsular os algoritmos da mesma família também permite a reutilização do código.

## 2. Aplicação do Strategy

A aplicação do strategy na nossa aplicação se refere a uma lógica de services que foi criada com o intuito de simplificar o código das telas da aplicação. Há um arquivo central dos services (useService.js) que contém é uma função criada para executar qualquer um dos outros services da aplicação.

Por exemplo:
Temos o service de users que contém as funções createUser(cadastro) e getUser(login). Ao necessitar de um desses dois algoritmos, o useService é importado na tela em questão e a partir dos parâmetros passados ele redireciona para o service desejado.

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/padroes-de-projeto/strategy/useService.png'>
  <figcaption align='center'>
      <b>Figura 1: Exemplo de uso do strategy na aplicação (useService.js)</b>
  </figcaption>
</p>

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/padroes-de-projeto/strategy/user.png'>
  <figcaption align='center'>
      <b>Figura 2: Exemplo de uso do strategy na aplicação (user.js)</b>
  </figcaption>
</p>

### Bibliografia

[1] - https://www.dofactory.com/javascript/design-patterns/strategy último acesso em: 17/09/2021 às 18:20. <br/>
[2] - https://refactoring.guru/design-patterns/strategy último acesso em: 17/09/2021 às 18:25. <br/>
[3] - https://unbarqdsw.github.io/2020.1_G12_Stock/#/Project/Estudos/comportamental?id=strategy último acesso em: 17/09/2021 às 18:37. <br/>
[4] - https://imasters.com.br/javascript/design-patterns-com-javascript-typescript-padroes-comportamentais último acesso em: 17/09/2021 18:40. <br/>
[5] - https://brizeno.wordpress.com/2011/08/31/strategy/ último acesso em: 17/09/2021 às 19:03. <br/>
