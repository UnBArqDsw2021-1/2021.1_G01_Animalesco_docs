# <center> Reutilização no Frontend

|    Data    | Versão |      Descrição       |   Autor(es)    |
| :--------: | :----: | :------------------: | :------------: |
| 11/10/2021 |  0.1   | Criação do documento | Daniela Soares |

<div align="justify">

A reutilização no Frontend se deu por meio de biblioteca como react native.

# React Native

O React Native é um biblioteca do React.js, adaptado para construir aplicativos móveis, onde permite que os desenvolvedores usem JavaScript, uma linguagem muito utilizada para o desenvolvimento web, também sendo usada para desenvolver aplicativos que possuem uma interface nativa para cada plataforma Android e iOS.

## Frozen Spots

São considerados aqueles pontos que permanecem fixos em todas as instanciações, representa uma arquitetura geral do sistema. No React Native, estamos utilizando um fronzen sports:

- Hooks: Permite reutilizar lógica com estado sem mudar sua hierarquia de componentes.

Exemplo de uso da hook useEffect

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/165-software-reuse-doc/docs/assets/images/useEffect.png'>
    <figcaption align='center'>
</p>

Exemplo de uso da hook useState

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/165-software-reuse-doc/docs/assets/images/useState.png'>
    <figcaption align='center'>
</p>

## Hot Sport

São considerados aqueles pontos que são projetados para serem genéricos, dando liberdade ao usuário de modelar como quiser. Representa partes específicas do sistema. No React Native, estamos utilizando um hot sports.

- Componentes: São como funções JavaScript. Eles aceitam entradas arbitrárias (chamadas "props") e retornam elementos React Native que descrevem o que deve aparecer na tela.

Exemplo de instância de  componentes

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/165-software-reuse-doc/docs/assets/images/components.png'>
    <figcaption align='center'>
    <p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/165-software-reuse-doc/docs/assets/images/GoBackHeader.png'>
    <figcaption align='center'>
    <p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/165-software-reuse-doc/docs/assets/images/Alert.png'>
    <figcaption align='center'>
</p>

# Bibliografia

* [1] Pricipais diferenças entre Ract & React Native Disponivel em:<https://www.luby.com.br/mobile/principais-diferencas-entre-react-e-react-native/> Acessado em: 11/10/2021

* [2] Introdução aos Hooks. Disponível em <https://pt-br.reactjs.org/docs/hooks-intro.html#motivation> Acessado em: 11/10/2021

</div>