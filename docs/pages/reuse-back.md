# <center> Reutilização no Backend

#### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 11/10/2021 |  0.1   | Criação do documento | Lorrany Oliveira Souza |
| 13/10/2021 |  0.2   | Atualização do documento | João Vitor Farias |



<div align="justify">

A construção de um software é um processo que demanda bastante tempo e esforço, e dependendo da complexidade do software, torna o processo mais demorado ainda. Pensando nisso, existe um conceito criado para amenizar essa situação chamada reutilização. "A reutilização de software se baseia no uso de conceitos, produtos ou soluções previamente elaboradas ou adquiridas para criação de um novo software, visando melhorar significativamente a qualidade e a produtividade".(Devmedia, 2011)

No desenvolvimento do backend foi utilizado o conceito de reutilização de software com o objetivo de otimizar a construção do aplicativo. Com isso, por meio de discussões entre o grupo foi decidido fazer o reuso do framework Django.

## Django

Django foi desenvolvido por uma empresa de software chamada Django Software Foundation. Ele utiliza a linguagem Python em sua escrita e tem como objetivo o desenvolvimento rápido para Web utilizando também o padrão model-template-view, em que cada model é considerado um aplicativo.

Utilizado em conjunto com o framework Django REST, possibilita uma maior praticidade no desenvolvimento de web API’s, além de possuir um sistema de autenticação e serialização de dados. Desta forma, ao utilizarmos os padrões já estabelecidos pelo Django REST já estamos utilizando as práticas da Alta Coesão e Baixo acoplamento, visto que cada um dos arquivos tem sua própria responsabilidade e seus próprios métodos definidos. Com estes padrões definidos a prática de reutilização se torna mais viável.

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/back-reuse/estruturaback.png'>
  <figcaption align='center'>
      <b>Figura 1: Estrutura do backend utilizando o Django</b>
      <br>
  </figcaption>
</p>

Além disso, outro aspecto do framework que contribui com a prática de reutilização é referente a utilização de API REST, em que os serviços fornecidos pelo backend da aplicação podem ser consumidos por qualquer interface, web e mobile, desde que as regras de negócio sejam condizentes. 

## Bibliografia

* [1] Devmedia. Reutilização de Software - Revista Engenharia de Software Magazine 39. Disponível em <https://www.devmedia.com.br/reutilizacao-de-software-revista-engenharia-de-software-magazine-39/21956> (Último acesso em 11/10/2021)

* [2] Alura. Django e Django Rest: Diferenças e aplicações. Disponível em <https://www.alura.com.br/artigos/django-django-rest-diferencas> (Último acesso em 13/10/2021)

</div>
