<!--

https://fga-eps-mds.github.io/2019.1-Gaia/#/projeto/DocArquitetura?id=_15-vis%c3%a3o-geral
https://pax-app.github.io/Wiki/#/docs/DS/dinamica-e-seminario-4-b/DAS
https://botlino.github.io/docs/doc-arquitetura
https://desenhosoftware-2018-2.github.io/wiki/docArquitetura
https://fga-eps-mds.github.io/2020.1-eSaudeUnB-Wiki/documento_arquitetura/#2-representacao-da-arquitetura
https://fga-eps-mds.github.io/2020.2-Violeta-Documentacao/Projeto/doc_arquitetura/#15-visao-geral
https://fga-eps-mds.github.io/2020-2-SiGeD/architecturedocument/#escopo
http://diatinf.ifrn.edu.br/prof/lib/exe/fetch.php?media=user:1301182:disciplinas:arquitetura:exemplo-arquitetura-02.pdf
http://site.maruge.com.br/documentacoes/Mar_Doc_Arq_V.3.13.pdf
http://repositorio.aee.edu.br/bitstream/aee/1106/3/TCC2_2018_2_GabrielLeiteDias_MatheusLimadeAlbuquerque_Apendice2.pdf
http://www.facom.ufu.br/~flavio/pds1/files/2016-01/Documento%20de%20Arquitetura%20de%20Software%20do%20SPEU%201-Exemplo-RUP.pdf
-->

# <center> Documento de Arquitetura - DAS

#### Histórico de Versão

|    Data    | Versão |                    Descrição                    |                   Autor(es)                   |
| :--------: | :----: | :---------------------------------------------: | :-------------------------------------------: |
| 07/10/2021 |  0.1   |              Criação do Documento               | Durval Carvalho, Hugo Sobral e Leonardo Gomes |
| 07/10/2021 |  0.2   |               Escrita do Sumário                |                Durval Carvalho                |
| 07/10/2021 |  0.3   |              Escrita da Introdução              |                Durval Carvalho                |
| 07/10/2021 |  0.4   |              Escrita da Finalidade              |                Durval Carvalho                |
| 07/10/2021 |  0.5   |                Escrita do Escopo                |                Durval Carvalho                |
| 07/10/2021 |  0.6   | Escrita das Definições, Acrônimos e Abreviações |                Durval Carvalho                |
| 07/10/2021 |  0.7   |             Escrita da Visão Geral              |                Durval Carvalho                |
| 07/10/2021 |  0.8   |      Escrita da Representação Arquitetural      |                Durval Carvalho                |
| 10/10/2021 |  0.9   |        Escrita da Visão de Casos de Uso         |                  Rafael Leão                  |
| 10/10/2021 |  0.10  |         Escrita da Visão de Implantação         |                  Rafael Leão                  |
| 13/10/2021 |  0.11  |         Escrita do tópico Tecnologias           |                Durval Carvalho                |
| 13/10/2021 |  0.12  |        Django e Django REST Framework           |                Durval Carvalho                |
| 13/10/2021 |  0.13  |              Aurora DB e Postgres               |                Durval Carvalho                |
| 13/10/2021 |  0.14  |                      Expo                       |                Durval Carvalho                |
| 13/10/2021 |  0.15  |        Adiciona Diagrama de Componentes         |                Durval Carvalho                |
| 13/10/2021 |  0.16  |        Reescrita e ajuste da Representação Arquitetural         |                Hugo Sobral                |
| 13/10/2021 |  0.17  |        Adição do diagrama de relacionamentos do projeto         |                Hugo Sobral                |
| 13/10/2021 |  0.18  |        Escrita dos padrões arquiteturais         |                Hugo Sobral                |



<hr>

## Sumário

[1. Introdução](#_1-introdução) <br>
&emsp; [1.1 Finalidade](#_11-objetivo) <br>
&emsp; [1.2 Escopo](#_12-escopo) <br>
&emsp; [1.3 Definições, Acrônimos e Abreviações](#_13-definições-acrônimos-e-abreviações) <br>
&emsp; [1.4 Referências](#_14-referências) <br>
&emsp; [1.5 Visão Geral](#_15-visão-geral) <br>

[2. Representação Arquitetural](#_2-representação-arquitetural) <br>

&emsp; [2.3 Padrões](#_23-padrões) <br>

&emsp; [2.4 Tecnologias](#_24-tecnologias) <br>
&emsp; &emsp; [2.4.1 Django e Django REST Framework](#_241-django-e-django-rest-framework) <br>
&emsp; &emsp; [2.4.2 Aurora DB](#_242-aurora-db-e-postgres) <br>
&emsp; &emsp; [2.4.3 Expo](#_243-expo) <br>

[3. Metas e Restrições da Arquitetura](#_3-metas-e-restrições-da-arquitetura) <br>
&emsp; [3.1 Restrições Tecnológicas](#_31-restrições-tecnológicas) <br>
&emsp; [3.2 Requisitos Não Funcionais](#_31-requisitos-não-funcionais) <br>

[4. Visão Lógica](#_4-visão-lógica) <br>
&emsp; [4.1. Visão Geral](#_41-visão-geral) <br>
&emsp; [4.2. Pacotes de Design Significativos do Ponto de Vista da Arquitetura](#_42-pacotes-de-design-significativos-do-ponto-de-vista-da-arquitetura) <br>
&emsp; &emsp; [4.2.1 Diagrama de Pacotes](#_421-diagrama-de-pacotes) <br>
&emsp; &emsp; [4.2.2 Diagrama de Classes](#_422-diagrama-de-classes) <br>

[5. Visão de Casos de Uso](#_5-visão-de-casos-de-uso) <br>
&emsp; [5.1. Diagrama de Casos de Uso](#_51-diagrama-de-casos-de-uso) <br>

[6. Diagrama de Componentes](#_6-diagrama-de-componentes) <br>
&emsp; [6.1. Componente de exportação](#_61-componente-de-exportação) <br>
&emsp; [6.2. Componente de Autorização e Autentificação](#_62-componente-de-autorização-e-autentificação) <br>
&emsp; [6.3. Componente de roteamento](#_63-componente-de-roteamento) <br>
&emsp; [6.4. Componente de alertas e notificações](#_64-componente-de-alertas-e-notificações) <br>
&emsp; [6.5. Componente de tarefas periódicas](#_65-componente-de-tarefas-periódicas) <br>

[7. Visão de Implantação](#_7-visão-de-implantação) <br>

<hr>

## 1. Introdução

&emsp;&emsp; O documento de arquitetura - DAS tem como objetivo descrever a arquitetura da solução de software _Animalesco_. Esse sistema tem como finalidade ajudar os usuários que possuem animais de estimação a cuidar de seus pets. Por meio do aplicativo mobile disponível para os sistemas operacionais Android e IOS, os usuários podem registar seus animais de estimação, assim como as vacinas, os medicamentos, os banhos e visitas veterinárias.

### 1.1 Finalidade

Esse documento apresenta a visão arquitetural geral do sistema do projeto _Animalesco_, por meio de diversas visões arquiteturais em diferentes graus de detalhamento. A finalidade desse documento é capturar e comunicar as diversas decições arquiteturais que foram tomadas no decorrer do desenvolvimento do projeto.

### 1.2 Escopo

&emsp;&emsp; Esse documento se aplica ao sistema de gerenciamento de animais doméstico _Animalesco_. Nesse documento estão contemplados os padrões de software, componentes de software, plataformas e frameworks de desenvolvimento, casos de uso e serviços de persistência de dados.

&emsp;&emsp; É também escopo deste documento orientar todo o pessoal técnico envolvido nas equipes de desenvolvimento do projeto, oferecendo diretrizes quanto às tecnologias utilizadas nesse projeto, assim como seu padão de utilização.

### 1.3 Definições, Acrônimos e Abreviações

| Abreviação |                                Acrônimo                                |                                                                                                  Definição                                                                                                  |
| :--------: | :--------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|    API     | Application Program Interface (Interface de Programação de Aplicações) |                                                                              API é um interface de programação de aplicações.                                                                               |
|    HTTP    | HyperText Transfer Protocol (Protocolo de Transferência de Hipertexto) |                                           O HTTP é um protocolo de comunicação utilizado para sistemas de informação de hipermídia, distribuídos e colaborativos.                                           |
|    MVC     |                         Model View Controller                          |    Padrão de arquitetura de software onde M significa modelo sendo responsável pela parte de regras de negócio, V a visualização responsável pela parte de interfaces e C a parte de controle dos dados.    |
|    S.O     |                          Sistema Operacional                           |                                                          O S.O. é o software responsável pelo gerenciamento de todo o hardware do seu computador.                                                           |
|    REST    |                    Representational State Transfer                     |                               REST é um estilo de arquitetura de software que define um conjunto de restrições a serem usadas para a criação de web services (serviços Web).                                |
|    DRY     |                         Don't Repeat Yourself                          | DRY é um conceito de programação de computadores o qual propõe que cada porção de conhecimento em um sistema deve possuir uma representação única, de autoridade e livre de ambiguidades em todo o sistema. |
|    WEB     |                             World Wide Web                             |                                               A World Wide Web designa um sistema de documentos em hipermídia que são interligados e executados na Internet.                                                |

### 1.4 Referências

- MARIOTTI, Flávio. Como documentar a Arquitetura de Software. Disponível em: <http://www.linhadecodigo.com.br/artigo/3343/como-documentar-a-arquitetura-de-software.aspx>. Acesso em 07 de Outubro de 2021.

- Muhamad, Youssef; Freitas, Esio; Campos, Felipe; Junior, Rogério; Albino, Gabriel; Ribas, Fabiana Luiza V. P.; Nery, Marcos; Borges, Kaique; Nascimento, Lucas Dutra Ferreira do. Pax App: Documento de Arquitetura. Disponível em: <https://pax-app.github.io/Wiki/#/docs/DS/dinamica-e-seminario-4-b/DAS>. Acesso em 07 de Outubro de 2021.

- Albuquerque, Luciana; Muniz, Amanda; Duarte, Indiara; Patrocinio, Sofia; Gouveia, Micaella; Taira, Luís Henrique Pereira; Rios, Calebe; Buters, Samuel. Gaia: Documento de Arquitetura. Disponível em: <https://fga-eps-mds.github.io/2019.1-Gaia/#/projeto/DocArquitetura>. Acesso em 07 de Outubro de 2021.

- The API Gateway Pattern; Disponível em: <https://freecontent.manning.com/the-api-gateway-pattern/>; Acesso em 07 de Outubro de 2021.

- RICHARDSON, Chris; Pattern: Pattern: API Gateway / Backends for Frontends; Disponível em: <https://microservices.io/patterns/apigateway.html>; Acesso em 07 de Outubro de 2021.

- NEWMAN, Sam; Building Microservices Second edition: Designing Fine-Grained Systems. 2nd Ed. O'Reilly. ISBN 1492034029, 978-1492034025.

### 1.5 Visão Geral

Para melhor entendimento do documento, o texto foi dividido em X partes, das quais documento as decições tomadas durante o desenvolvimento da aplicação _Animalesco_. Cada um dos X tópicos traz consigo suas características e importâncias para esse documento. Esses tópicos estão estruturados da seguinte forma:

| Numeração |              Tópico               |                                                                                                       Definição                                                                                                       |
| :-------: | :-------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|    02.    |    Representação Arquitetural     |                                                                                     Sessão que descreve a arquitetura do software                                                                                     |
|    03.    | Metas e Restrições da Arquitetura |                                                               Sessão que descreve os requisitos e os objetivos do software que impactam na arquitetura                                                                |
|    04.    |       Visão de Casos de Uso       |                                                                                                         TODO                                                                                                          |
|    05.    |           Visão Lógica            |                                                           Sessão que descreve as partes significativas do ponto de vista da arquitetura do modelo de design                                                           |
|    06.    |        Visão de Processos         |                                                                 Sessão que descreve a decomposição do sistema em processos leves e processos pesados                                                                  |
|    07.    |       Visão de Implantação        | Sessão que descreve a estrutura geral do modelo de implementação, a divisão do software em camadas e os subsistemas no modelo de implementação e todos os componentes significativos do ponto de vista da arquitetura |
|    08.    |          Visão de Dados           |                                                                  Sessão que descreve a perspectiva de armazenamento de dados persistentes do sistema                                                                  |
|    09.    |       Tamanho e Desempenho        |                                    Sessão que descreve as principais características de dimensionamento que impactam na arquitetura, bem como as restrições do desempenho desejado                                    |
|    10.    |             Qualidade             |                                                                                                         TODO                                                                                                          |

## 2. Representação Arquitetural

Com o advento e o sucesso da rede mundial de computadores, a maneira de entregar serviços de interface de usuários mudou de aplicações desktop para interfaces web. Um outro marco importante para o modelo de consumo de softwares foi a popularização de smartphones: a partir deste momento a grande tendência de desenvolvimento se tornou as aplicações mobile. A partir desta perspectiva, pode-se destacar uma das grandes problemáticas do desenvolvimento mobile: a criação de produtos de software multiplataforma (Android e IOS, por exemplo) se tornou complexa e redundante, sendo necessário a reescrita e refatoração da mesma lógica de negócio em diversas bases de código diferentes. (NEWMAN, 2021)

Dado o devido problema, uma solução criada e amplamente utiliza em aplicações modernas de software é a utilização de uma única API do lado do servidor, cuja a responsabilidade é aplicar o processamento das informações a partir das regras negociais mapeadas e realizar a comunicação com a camada de persistência de dados. Tal serviço, tido como servidor, provê as funcionalidades por meio de uma API REST para as várias aplicações mobile disponíveis e distribuidas para os usuários, estas tidas como o lado do cliente.

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/das-documento-de-arquitetura/bff.png'>
  <figcaption align='center'>
      <b>Figura 1: Ilustração com duas aplicações de interface de usuário consumindo uma única API</b>
      <br>
      <small>Fonte: (NEWMAN, 2021)</small>
  </figcaption>
</p>

Esse padrão arquitetural é derivado do estilo arquitetural N-Camandas, onde é utilizado 3 camadas: a camada de visualização (serviços de interface gráfica), a camada de regras de negócios (API) e serviço de persistência de dados (servidor de banco de dados). Uma nomenclatura comum para esse padrão arquitetural é o _Backends For Frontends_.

<img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/das-documento-de-arquitetura/das-diagram.jpg'>
  <figcaption align='center'>
      <b>Figura 2: Diagrama com os principais módulos que compõe a arquitetura do sistema Animalesco</b>
      <br>
  </figcaption>
</p>

A Figura 2 mostra uma visão macro dos subsistemas que compõe a solução desenvolvida no projeto Animalesco. Na camada mais alta, está presente um cluster de serviços de interface de usuários. Um cluster é um conjunto de instâncias de um mesmo serviço com a finalidade de aumentar a disponibildiade do serviço para cenários de alto volume de acesso. A camada logo abaixo é a camada do serviço de API Gateway, cuja finalidade é distribuir a carga de acesso da camada de cima para as várias instâncias da camada de baixo. A camada logo abaixo é a camada das APIs, cuja finalidade é disponibilizar os serviços e funcionalidades para a camada de serviços de interface gráfica. E por fim, a última camada é a camada de persistência de dados, que no diagrama é representado pelo serviço denominado Aurora DB, forneceido pela AWS Amazon, cuja finalidade é atuar como um banco de dados.

### 2.1 Diagrama de Relações

<img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/das-documento-de-arquitetura/das-relacionamento.png'>
  <figcaption align='center'>
      <b>Figura 3: Diagrama de relacionamentos do sistema Animalesco</b>
      <br>
  </figcaption>
</p>


### 2.3 Padrões

#### 2.3.1 Padrão Cliente-Servidor

O padrão arquitetural Cliente-Servidor descreve a modularização de um sistema de software a partir de diferentes camadas separadas por funcionalidades, isto é, vários serviços clientes requisitam para e recebem informações de um módulo central, o servidor. Serviços que assumem o papel de cliente devem prover ao usuário uma interface que o permita realizar a comunicação e interação com os dados e informações contidas e tratadas no servidor.     
Idealmente, um servidor deve ser robusto o suficiente para que as camadas de cliente não precisem conhecer os módulos que implementam as tratativas e regras negociais acordadas para o sistema.    
Para o Projeto Animalesco, os dispositivos que assumem o papel de cliente são os celulares cujo o aplicativo mobile esteja devidamente instalado, enquanto o papel de servidor é tomado pela API REST desenvolvida.

## 2.4 Tecnologias

Para a realização desse projeto foi utilizado um conjunto de ferramentas, sendo as mais importantes delas o Framework de desenvolvimento de APIs Web `Django REST Framework` e a plataforma de desenvolvimento de aplicativos nativos Expo. Além dessas duas tecnologias foi utilizado o serviço de banco de dados relacional Aurora DB.

### 2.4.1. Django e Django REST Framework

Django é um framework, gratuito e de código aberto, de desenvolvimento Web escrito em Python, de alto nível e que incentiva o desenvolvimento rápido e um design limpo e pragmático.

Django REST Framework (DRF) é um framework para o framework Django. O DRF é um kit de ferramentas poderosas e flexíveis que possibilitam a construção de APIs da Web.

Ambas as tecnologias foram escolhidas para desenvolver as APIs backend utilizada para disponibilziar os serviços utilizados pela camada de visualização. As duas principais motivações para escolher essas duas tecnologias foram:

* Havia participantes no grupo que possuia experiência com ambas ferramentas e estava disposto a realizar treinamentos e fornecer ajuda aos demais membros.

* Ambas ferramentas possibilitam um rápido desenvolvimento, compatível com o tempo de duração do projeto.

### 2.4.2. Aurora DB e Postgres

Para realizar a persistência de dados foi utilizado o sistema gerenciador de banco de dados objeto relacional open source Postgres e o serviço de banco de dados relacional Aurora DB.

No desenvolvimento local do projeto foi utilizado uma instância do Postgres enquanto que no ambiente de homologação foi utilizado o serviço de banco de dados Heroku Postgres. Já no ambiente de produção é utilizado o serviço de banco de dados relacional fornecido pela Amazon, e retrocompatível com a API do Postgres, Aurora DB.

### 2.4.3. Expo

Na camada de visualização foi utilizado o framework Expo. O Expo é uma estrutura e uma plataforma para aplicações React universais. É um conjunto de ferramentas e serviços criados em torno de plataformas React Native e nativas que ajudam a desenvolver, construir, implantar e iterar rapidamente em aplicativos iOS, Android e web a partir da mesma base de código JavaScript / TypeScript.

A principal motivação para a utilização do Expo foi o requisito de desenvolvimento de aplicações nativas para smartphones. Dessa forma, devida ao tempo de duração do projeto e ao requisito de disponibilizar o aplicativo tanto para a plataforma Android e iOS, foi escolhido a ferramenta Expo.

## 3. Metas e Restrições de Arquitetura

### 3.1 Restrições Tecnológicas

<!--
<p align="justify">&emsp;&emsp;Para o desenvolvimenta da Gaia serão utilizados as seguintes tecnologias:</p>

- Rasa: Conjuntos de ferramentas de Machine Learning para a criação de chatbots.
- Python: Linguagem base utilizada no Rasa.
- Node.js: Plataforma de aplicação utilizada nos microsserviços.
- JavaScript: Linguagem base utilizada no Node.js.
- MongoDB: Software utilizado para o banco de dados,

### 3.2 Requisitos Não Funcionais

- O sistema deve ter integração com o Telegram;
- O sistema deve ter integração com o Facebook;
- O sistema deve conversar com o usuário em linguagem natural;
- O sistema deve respeitar a personalidade do bot;
- O sistema deve aprender novos comportamentos de acordo com a resposta do usuário; -->

## 4. Visão Lógica

### 4.1 Visão Geral

<!--
<p align=”justify”>&emsp;&emsp; A aplicação do ChatBot Gaia é construída com a tecnologia Rasa em linguagem Python no bot e sobre a plataforma Node.js em linguagem JavaScript nos microsserviços. O objetivo do RasaNLU é aplicar algoritmos de linguagem natural para extrair a intenção do usuário (intents) e a partir do Rasa Core é possível gerir o diálogo entre o usuário e o bot. A principal funcionalidade é o policy, que recebe a intent do usuário, atualiza o tracker() e prevê a melhor ação do bot (utter, action, listening). A plataforma Node.js é um ambiente de tempo de execução que executa o código em JavaScript para escrever ferramentas de linha de comando e para scripts do lado do servidor, capaz de executar uma entrada/saída assíncrona, que permite que outro processamento continue antes que a transmissão tenha encerrado.</p> -->

### 4.2 Pacotes de Design Significativos do Ponto de Vista da Arquitetura

#### 4.2.1 Diagrama de pacotes

<!--
![](../assets/imgs/architecture/diagramaRasa.png)

Imagem 04 - Diagrama de Pacotes da Gaia

![](../assets/imgs/architecture/diagramaPacotesGateway.png)

Imagem 05 - Diagrama de Pacotes do Gaia-Gateway

![](../assets/imgs/architecture/diagramaPacotesEsporte.png)

Imagem 06 - Diagrama de Pacotes do Gaia-Esporte

![](../assets/imgs/architecture/diagramaPacotesCiclone.png)

Imagem 07 - Diagrama de Pacotes do Gaia-Ciclone -->

#### 4.2.2 Diagrama de classe

##### 4.2.2.1 Diagrama de Classe do Gaia-Esporte

<!--
![](../assets/imgs/architecture/diagramaClasseEsporte.png)

Imagem 08 - Diagrama de Classe do Microsserviço Gaia-Esporte -->

##### 4.2.2.2 Diagrama de Classe do Gaia-Ciclone

<!--
![](../assets/imgs/architecture/diagramaClasseCiclone.png)

Imagem 09 - Diagrama de Classe do Microsserviço Gaia-Ciclone -->

## 5. Visão de Casos de Uso

A **Visão de Casos de Uso** descreve um modelo com alta significância de alto nível em relação às funcionalidades do sistema. Normalmente feito através do **Diagrama de Casos de Uso**.

### 5.1 Diagrama de Casos de Uso

A figura abaixo "Diagrama de Caso de Uso", demonstra todos os casos de uso que o sistema pretende atender.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/use-case/use_case_diagram.png'>
    <figcaption align='center'>
        <b>Diagrama de caso de uso</b>
        <br>
        <small>Autores: João Vitor Farias e Lorrany Souza, 2021.</small>
    </figcaption>p
</p>

A abaixo uma lista das especificações dos casos de uso com uma breve descrição de cada um.

| Id   | Caso de uso                                                   | Descrição                                                                                                                                                                                                                                                                                                             |
| ---- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UC01 | [Cadastrar usuário](pages/casos-de-uso/UC01.md)               | O presente caso de uso descreve o fluxo de atividade que inclui realizar o cadastro de um novo usuário. O sistema deve fornecer ao usuário a possibilidade de se cadastrar, com o objetivo de ter acesso e desfrutar das demais funcionalidades.                                                                      |
| UC02 | [Realizar login](pages/casos-de-uso/UC02.md)                  | O presente caso de uso descreve o fluxo de atividade que inclui efetuar a autenticação do usuário. O sistema deve fornecer ao usuário a possibilidade de realizar o login, com o objetivo de ter acesso às demais funcionalidades.                                                                                    |
| UC03 | [Recuperar senha](pages/casos-de-uso/UC03.md)                 | O presente caso de uso descreve o fluxo de atividade que inclui resgatar a senha que o usuário esqueceu. O sistema deve fornecer ao usuário a possibilidade de recuperar a senha, com o objetivo de restabelecer o acesso.                                                                                            |
| UC04 | [Visualizar perfil usuário](pages/casos-de-uso/UC04.md)       | O presente caso de uso descreve o fluxo de atividade que inclui tornar visível os dados do usuário cadastrado. O sistema deve fornecer ao usuário a possibilidade de visualizar os próprios dados, atualizá-los e removê-los, com o objetivo de estar ciente dos dados cadastrado.                                    |
| UC05 | [Cadastrar pet](pages/casos-de-uso/UC05.md)                   | O presente caso de uso descreve o fluxo de atividade que inclui cadastrar os dados do pet. O sistema deve fornecer ao usuário a possibilidade de cadastrar os dados do pet, com o objetivo de manter registrado os dados do animal de estimação.                                                                      |
| UC06 | [Visualizar pefil pet](pages/casos-de-uso/UC06.md)            | O presente caso de uso descreve o fluxo de atividade que inclui tornar visível os dados do pet cadastrado. O sistema deve fornecer ao usuário a possibilidade visualizar os dados do pet cadastrado, atualizá-los e removê-los, com o objetivo de estar ciente dos dados cadastrado.                                  |
| UC07 | [Registrar medidas](pages/casos-de-uso/UC07.md)               | O presente caso de uso descreve o fluxo de atividade para registrar as medidas do pet. O sistema deve permitir que o usuário consiga registrar as medidas do seu animal de estimação, com o intuito de auxiliar o usuário a ter uma forma de registrar as medidas do seu pet, caso ele deseje.                        |
| UC08 | [Registrar banho](pages/casos-de-uso/UC08.md)                 | O presente caso de uso descreve o fluxo de atividade que inclui realizar o registro de banho. O sistema deve permitir que o usuário consiga registrar o banho de seu animal de estimação, com o intuito de auxiliar para que o usuário consiga saber quando será banho do pet.                                        |
| UC09 | [Controlar medicamento](pages/casos-de-uso/UC09.md)           | O presente caso de uso descreve o fluxo de atividade que inclui realizar o controle de medicamento do pet. O sistema deve permitir que o usuário consiga realizar o controle de medicamento do seu animal de estimação, com o intuito de auxiliar que o usuário consiga ter um controle sobre a medicação de seu pet. |
| UC10 | [Visualizar vacinas](pages/casos-de-uso/UC10.md)              | O presente caso de uso descreve o fluxo de atividade que inclui visualizar as vacinas do pet. O sistema deve fornecer ao usuário a possibilidade de visualizar as vacinas do seu animal de estimação, com o intuito de manter o controle da vacinação do pet.                                                         |
| UC11 | [Registrar visita ao veterinário](pages/casos-de-uso/UC11.md) | O presente caso de uso descreve o fluxo de atividade que inclui registrar os dados de uma visita ao veterinário. O sistema deve fornecer ao usuário a possibilidade de registrar uma visita ao veterinário, com o intuito manter o controle de quando e como foi a visita ao veterinário.                             |
| UC12 | [Adicionar lembrete](pages/casos-de-uso/UC12.md)              | O presente caso de uso descreve o fluxo de atividade que inclui adicionar lembrete. O sistema deve permitir a adição de lembretes com o intuito de que sistema lembre o usuário para que o usuário não se esqueça de realizar algo.                                                                                   |


## 6. Diagrama de Componentes

Para a realização do diagrama de componentes do projeto Animalesco, foi necessário tomar algumas decisões. A primeira grande decisão tomada na diagramação foi a de aumentar o nível de detalhamento das componentes que lidam com regras de negócio.

A segunda  grande decisão foi a de diminuir o nível de detalhamento de algumas partes do diagrama e a de aumentar o nível de detalhamento das partes que envolve regras de negócios. Essa decisão foi tomada pois as partes que lidão com regras de negócios tem maior probabilidade de sofrer mudanças e logo devem ser melhor compreendidas. Dessa forma, pode ser visto que o maior detalhamento está no no grande componente de backend.

Outra decisão tomada foi a de não representar as conexões triviais, para assim evitar a poluição do diagrama. A primeira classe de conexões "escondidas" foi as conexões com o componente de persistência (todos os componentes se comunicam com os bancos de dados). A segunda classe de conexões "escondida" foi a comunicação com o componente de roteamento. O componente de roteamento é responsável por mapear a comunicação do frontend com um módulo ou funcionalidade específica. Desse modo, tal componente está conectado com todos os demais componentes, e a representação de tais conexões iria diminuir a compreensibilidade do diagrama.

Outra decisão do diagrama foi a de utilizar _tags_ para representar alguns módulos do sistema. As principais _tags_ utilizadas e seus respectivo significados foram:

* «sistema» - Representa um sistema em execução um hardware independente (servidor ou smartphone)
* «subsistema» - Representa um sistema em execução um servidor compartilhado com outros sistemas (servidor ou smartphone)
* «módulo» - Representa os módulos que pode existir dentro de um componente

O diagrama construído pode ser acessado através da plataforma [Draw.IO](https://app.diagrams.net/). Basta fazer o download do arquivo do diagrama e carregá-lo da plataforma. O arquivo do diagrama está disponível no seguinte link: https://github.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/tree/main/docs/assets/pages/component-diagram

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/component-diagram/diagrama-de-componentes.jpg'>

    <figcaption align='center'>
        <b>Figura 1: Imagem do diagrama de componentes</b>
        <br>
        <small>Fonte: Durval Carvalho</small>
    </figcaption>
</p>

### 6.1. Componente de exportação

Esse é o componente responsável por obter dados dos demais componentes e gerar um relatório que será enviado por email.

Como pode ser visto no diagrama, esse serviço utiliza a interface de vários componentes do sistema para obter as informações do relatório e por fim utiliza o componente de envio de emails para finalizar o envio do relatório.


### 6.2. Componente de Autorização e Autentificação

Esse é o componente responsável por controlar quem acessar e o que acessa na API do backend. Neste componente irá agrupar toda a lógica de controle de acesso através do uso de _middlewares_.

Como pode ser visualizado no diagrama, toda a comunicação passa por esse componente.

### 6.3. Componente de roteamento

Esse é o componente responsável por conectar todos os componentes internos do backend com as requisições do frontend. Neste componente será mapeado as requisições (_endpoint_ das apis) com as várias controladoras que utilizam os demais componentes.

Esse é um componente chave que possui conexões com todos os demais componentes, porém, visando não diminuir a compreensibilidade do diagrama, tais conexões não foram ilustradas.

### 6.4. Componente de alertas e notificações

Esse é o componente responsável por emitir notificações para o frontend. Assim, esse componente irá grupar toda a lógica de comunicação com o aplicativo ou com a sessão web. Além de agrupar as várias potenciais integrações com serviços de notificações que podem ser contratados.

### 6.5. Componente de tarefas periódicas

Esse é o principal componente do sistema. As principais funcionalidades que mais agregam valor ao nosso produto estão contidas nesse componente. Dessa forma, os demais componentes desse sistema utilizam ou dão suporte as funcionalidades desse componente (emissão de emails, emissão de notificações e emissão de relatórios).

Por ser um componente de extrema importância, esse é o único componente que detalha seus módulos internos, para assim facilitar a compreensão do diagrama.


## 7. Visão de Implantação

O animalesco é uma aplicação mobile que segue um modelo de camadas. Temos a camada do Front-end, Back-end e o Banco de Dados. A camada de Front-end realiza requisições à camada de Back-end que interage com o Banco de dados e retorna uma resposta ao Front-end que organiza como esses dados serão mostrados ao usuário.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/das-documento-de-arquitetura/implantacao.png'>
    <figcaption align='center'>
        <b>Diagrama de Implantação</b>
        <br>
        <small>Autor: Rafael Leão, 2021.</small>
    </figcaption>
</p>
