# <center> Questionário

### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 03/08/2021 |  0.1   | Criação do documento | Durval Carvalho e Leonardo Gomes |
| 03/08/2021 |  0.2   | Criação da Introdução e Metodologia | Durval Carvalho |
| 03/08/2021 |  0.3   | Adição do gráfico de fluxo de perguntas | Leonardo Gomes |
| 03/08/2021 |  1.0   | Adição da bibliografia e resultados | Durval Carvalho e Leonardo Gomes |
| 05/08/2021 |  1.1   | Revisão do documento | Hugo Sobral |


<div align="justify">

## 1. Introdução

O uso de questionários é uma das técnicas de coleta de dados mais frequentemente utilizadas. Um questionário é um formulário impresso ou digital com perguntas que os usuários ou grupo de foco devem responder, com a finalidade de fornecer dados necessários para um futura análise. Diferentemente das demais técnicas, questionários permitem coletar dados a partir de uma amostragem de pessoas potencialmente maior quando comparada a outros métodos, visto que estes permitem a resposta em massa de um grande número de pessoas, mesmo que geograficamente dispersas. [1]

A utilização da técnica de questionários para a elicitação de requisitos, tem como objetivo principal a coleta rápida de dados de muitos usuários, principalmente dados quantitativos (COURAGE e BAXTER, 2015). Essa técnica tem como principal vantagem a capacidade de coletar informações de muitos usuários com um custo relativamente barato, quando comparado com as demais técnicas (entrevistas, grupos de focos, estudo de campos e outras). Porém, por mais que o uso dessa técnica seja simples, é necessário experiência do elaborador e avaliador do questionário, para que sejam evitadas perguntas ambíguas e dinâmicas que induzam respostas enviesadas. [1] [2]

Questionários de elicitação de requisitos podem conter perguntas abertas e fechadas, mas geralmente as perguntas fechadas são mais utilizadas por serem de rápido preenchimento e por viabilizar análises estatísticas. [1] 

Uma característica dos questionários é sua assincronicidade, isto é, o grupo alvo do questionário pode respondê-lo no seu próprio tempo e no conforto do seu ambiente, sem a necessidade de combinar datas e horário de encontro, e sem a necessidade de deslocamento físico para um local ou ingressar em uma chamada de vídeo/audio. No entanto essa característica também pode apresentar desvantagens, pois a pessoa que estiver respondendo o questionário não terá como tirar dúvidas sobre as perguntas, o que pode acarretar em interpretações erradas. Desta forma, a elaboração do questionário deve ser cuidadosa e deve-se evitar ao máximo ambiguidades e mal-entendidos (Lazar el.al., 2010).

## 2. Metodologia

O uso da técnica de questionário surgiu da necessidade de se conhecer melhor o nosso público alvo. Desta forma, os integrantes do grupo se reuniram durante o dia 30 de julho de 2021 e discutiram quais eram as informações interessantes que o grupo gostaria de saber sobre seus usuários. Após essa dinâmica de brainstorming, as seguintes questões surgiram:

* Quantos Pets o nosso publico alvo tem? 
* Quais são as espécies dos Pets do nosso público alvo?
* O nosso publico alvo dá banho no seu animal ou leva no Petshop?
* Com qual frequência os Pets do nosso público alvo tomam banho?
* Será que o nosso público alvo tem a vacinação de seus Pets em dia?
* Será que o nosso público alvo tem os tratamentos de anti-parasitas em dia?
* Será que o nosso público alvo leva seus Pets ao veterinário de tempos em tempos?
* Como será que o nosso público alvo gerencia os cuidados dos seus Pets?
* Será que os Pets do nosso público alvo tomam algum medicamento de uso contínuo? Se sim quais medicamentos são esses? E com que frequência?

Uma vez que as perguntas principais que o grupo estava interessado em saber foram definidas, foi utilizado a ferramenta Google Forms para elaborar um questionário digital. Essa ferramenta permite a criação de questionário com diversos tipos de perguntas (múltiplas escolhas, faixa de valores, escalas, perguntas abertas, etc.), além de criar gráficos dinâmicos que facilitam a análise posterior.


Após a conclusão do formulário, foram contabilizadas 16 perguntas, no seguinte fluxo:

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/fluxo_do_questionario.png'>
  <figcaption align='center'>
      <b>Figura 1: Fluxo de perguntas do questionário</b>
      <br>
      <small>Autores: Leonardo Gomes</small>
  </figcaption>
</p>

## 2.1. Validação do questionário

Após a criação do questionário foi realizado um estudo piloto com 9 pessoas, com o objetivo de validar as perguntas, as opções e o fluxo do formulário.

O estudo piloto se mostrou eficiente, após sua realização foi encontrado um parte do fluxo que não estava conectado corretamente, e também foi realizado melhorias de usabilidade para tornar as perguntas não ambíguas e para adicionar opções de respostas que o nosso grupo piloto sugeriu.

A parte do fluxo que estava faltando conexão era o seguinte:

```python
if Pergunta("Seu pet toma algum medicamento de uso contínuo?") == "Sim":
    # A pergunta abaixo não estava dependendo da pergunta anterior
    Pergunta("Qual Medicamento?")
else:
    # Outras Perguntas
```

A correção de usabilidade de maior impacto foi:

```python
Pergunta("Seu pet tomou todas as vacinas necessárias") ---+
                                                          |
                                                          |
Pergunta("Seu pet está com a vacinação em dia?")  <<------+
```

## 3. Resultados

O questionário começou a ser divulgado no dia 30 de julho de 2021 às 22h, em diversos grupos que os membros do projeto participavam. A primeira resposta obtida foi no mesmo dia às 22:18 e o formulário foi fechado para novas respostas no dia 02 de agosto às 20h.

No total foram obtidas 95 respostas, porém somente 86 delas serão úteis para o projeto, pois as 9 participantes não tinham pets e o fluxo se encerrava logo na primeira pergunta.

### 3.1 Perguntas

#### 3.1.1 Pergunta 1

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta1.png'>
  <figcaption align='center'>
      <b>Figura 2: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.2 Pergunta 2

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta2.png'>
  <figcaption align='center'>
      <b>Figura 3: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.3 Pergunta 3

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta3.png'>
  <figcaption align='center'>
      <b>Figura 4: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.4 Pergunta 4

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta4.png'>
  <figcaption align='center'>
      <b>Figura 5: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.5 Pergunta 5

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta5.png'>
  <figcaption align='center'>
      <b>Figura 6: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.6 Pergunta 6

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta6.png'>
  <figcaption align='center'>
      <b>Figura 7: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.7 Pergunta 7

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta7.png'>
  <figcaption align='center'>
      <b>Figura 8: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.8 Pergunta 8

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta8.png'>
  <figcaption align='center'>
      <b>Figura 9: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.9 Pergunta 9

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta9.png'>
  <figcaption align='center'>
      <b>Figura 10: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.10 Pergunta 10

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta10.png'>
  <figcaption align='center'>
      <b>Figura 11: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.11 Pergunta 11

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta11.png'>
  <figcaption align='center'>
      <b>Figura 12: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.12 Pergunta 12

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta12.png'>
  <figcaption align='center'>
      <b>Figura 13: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.13 Pergunta 13

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta13.png'>
  <figcaption align='center'>
      <b>Figura 14: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>


#### 3.1.14 Pergunta 14

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta14.png'>
  <figcaption align='center'>
      <b>Figura 15: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.15 Pergunta 15

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta15.png'>
  <figcaption align='center'>
      <b>Figura 16: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>

#### 3.1.16 Pergunta 16

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/questionario/pergunta16.png'>
  <figcaption align='center'>
      <b>Figura 17: </b>
      <br>
      <small>Autores: Equipe do projeto animalesco</small>
  </figcaption>
</p>


### 3.2 Análise das perguntas e elicitação de requisitos

A partir dos dados obtidos pela técnica de elicitação foi possível analisar o grupo alvo da aplicação e realizar suposições que levam a requisitos do sistema que será desenvolvido.

Dessa forma, foi analisado estatisticamente as respostas do formulário e foi presumido os seguintes requisitos:

| ID   | Requisito | 
|:-:   | :-: |  
| RF01 | Adicionar local do banho |
| RF02 | Histórico de banho |
| RF03 | Histórico de vacinação |
| RF04 | Agenda de vacinação |
| RF05 | Histórico de medicação |
| RF06 | Histórico de consultas |
| RF07 | Lembrete de medicamento |
| RF08 | Agenda de medicamento |


| ID    | Requisito | 
|:-:    | :-: | 
| RNF01 | Compatibilidade com IOS |
| RNF02 | Compatibilidade com Android |


Vale ressaltar que os requisitos aqui listados ainda precisam ser verificados e validados.


## Bibliografia

[1] BARBOSA, Simone; DINIZ, Bruno. Interação Humano-Computador, Editora Elsevier, Rio de Janeiro, 2010.

[2] Courage, Catherine; Baxter, Kathy; Caine, Kelly. Understanding Your Users: A Practical Guide to User.  Burlington, Massachusetts: Morgan Kaufmann, 2015.

[3] Lazar, J.; Feng, J. H.; Hochheiser, H. Research Methods in Human-Computer Interaction. New York, NY: John Wiley & Sons, 2010.

</div>
