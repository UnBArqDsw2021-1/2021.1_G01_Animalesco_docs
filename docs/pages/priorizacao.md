# <center> Priorização de requisitos

#### Histórico de Versão

|    Data    | Versão |      Descrição       |     Autor(es)     |
| :--------: | :----: | :------------------: | :---------------: |
| 04/08/2021 |  0.1   | Criação do documento | Lorrany Oliveira  |
| 05/08/2021 |  0.2   | Criação do quadro de histórias do usuario | Daniela Soares  |
| 05/08/2021 |  0.3   | Priorização dos requisitos | Lorrany Oliveira e Daniela Soares  |
| 05/08/2021 |  1.0   | Ajuste no histórico de versão e Revisão do documento | Leonardo Gomes  |
| 06/08/2021 |  1.1   | Revisão do documento | Hugo Sobral |
| 22/08/2021 |  1.2   | Adição da priorização de novas user stories | Hugo Sobral e Leonardo Gomes |

<div align="justify">

## 1. Introdução

A priorização de requisitos é um procedimento fundamental na hora da produção de um software, além de ser um dos fatores que minimiza a possibilidade de ocorrer uma falha na produção da aplicação. Isso ocorre porque, por meio de um __sistema de prioridades__, é possível realizar a análise de todos os requisitos e a devida priorização das tarefas, quase como uma ordem de implementação.

A execução de uma priorização deve levar em conta diversos fatores, como por exemplo, os diferentes tipos de tecnologias utilizados; qual o objetivo almejado; o determinado contexto do projeto; e entre outros. Desta forma, existem diversas técnicas que podem ser utilizadas para colaborar na priorização de requisitos, a qual deve ser escolhida com base na que mais se adequa ao projeto.

<br/>

## 2. MoSCoW

Uma das técnicas de priorização de requisitos, é o MoSCoW. É uma técnica que foi desenvolvida por _Dai Clegg_ na década de 90, enquanto ele trabalhava na Oracle, tendo como objetivo auxiliar a metodologia de desenvolvimento de sistemas dinâmicos. Seu nome é um acrônimo, o que facilita a aplicação da técnica e sua memorização. As letras em maiusculo indicam a ordem que deve ser seguida durante o processo:

 M - Must have: são os requisitos indispensáveis para a entrega do projeto, afetando diretamente o resultado de sucesso do seu projeto.

 S - Should have: são os requisitos que não são críticos para a entrega do projeto,  mas que seriam bom serem implementados.  

 C - Could have: são os requisitos que podem ser implementados caso haja recursos financeiros e de tempo.

 W - Wont have: são os requisitos que podem ser implementados posteriormente caso haja uma atualização ou melhoria do sistema.  

<br/>

## 3. Objetivo

O presente documento tem como objetivo a demostração do resultado da aplicação da técnica de priorização de requisitos _MoSCoW_, que foi aplicada no resultado da elicitação de requisitos do Animalesco, usando as diretrizes desta técnica como guia para classificação de quais deveriam ser priorizados ou não, e qual o grau de sua importância para o sucesso da aplicação.  

<br/>

## 4. Priorização das Histórias de Usuário

|  Épico  | Feature |  ID   |   Eu como    |   Desejo  |   Para   | Prioridade  |
| :-----: | :----:  |:-----:| :----------: | :-------: |:--------:| :---------: |
|  EP01   |  FT01   | US01  |   usuário    |   poder realizar o cadastro | ter acesso a aplicação    |   Must    |
|  EP01   |  FT01   | US02  |   usuário    |   alterar meus dados | manter o perfil atualizado      |   Should      |
|  EP01   |  FT01   | US03  |   usuário    |   poder realizar login  |    acessar a aplicação   | Must  |
|  EP01   |  FT01   | US04  |   usuário    |   apagar meus dados  |   remover o perfil   |   Should   |
|  EP01   |  FT01   | US05  |   usuário    |   resgatar a senha  |   realizar o login   |  Should  |
|  EP02   |  FT02   | US06  |   usuário    |   poder cadastrar meu(s) pet(s) na aplicação  |   realizar o controle das informaçoẽs dele(s)   | Must  |
|  EP02   |  FT02   | US07  |   usuário    |   poder alterar os dados do(s) meu(s) pet(s)  |   manter o(s) perfil(is) atualizado(s)   | Must  |
|  EP02   |  FT02   | US08  |   usuário    |   poder deletar o(s) registro(s) do(s) meu(s) pet(s)  |   remover os dados da aplicação   | Must   |
|  EP02   |  FT03   | US09  |   usuário    |   poder registrar os banhos do(s) meu(s) pet(s)  |   manter o controle   | Must  |
|  EP02   |  FT03   | US10  |   usuário    |   poder acessar o histórico de banho(s) do(s) meu(s) pet(s)  |   saber quando dar banho novamente   | Should  |
|  EP02   |  FT03   | US11  |   usuário    |   adicionar lembrete sobre o(s) banho(s)  |    não esquecer dele(s)   |  Should  |
|  EP02   |  FT03   | US12  |   usuário    |   deletar o(s) banho(s) do(s) pet(s)  |   remover a(s) informação(ões)   |  Could  |
|  EP02   |  FT04   | US13  |   usuário    |   registrar um medicamento  |   realizar o controle dele   | Must  |
|  EP02   |  FT04   | US14  |   usuário    |   registrar quando o medicamento foi dado | para manter o histórico atualizado | Must  |
|  EP02   |  FT04   | US15  |   usuário    |   adicionar um lembrete  |   não esquecer o horário da administração do medicamento   | Must  |
|  EP02   |  FT04   | US16  |   usuário    |   poder remover o medicamento  |   quando finalizar o seu período de administração   | Must  |
|  EP02   |  FT04   | US17  |   usuário    |   remover uma dose de medicação registrada  |   manter o controle da saúde do meu pet atualizado   | Could  |
|  EP02   |  FT04   | US18  |   usuário    |   acessar o histórico de medicações do meu pet para realizar o acompanhamento  | com a saúde do meu pet | Must  |
|  EP02   |  FT05   | US19  |   usuário    |   registrar as vacinas que o pet tomau  |   manter o dados atualizados   | Must  |
|  EP02   |  FT05   | US20  |   usuário    |   visualizar as vacinas do pet  |   me informar   | Must  |
|  EP02   |  FT05   | US21  |   usuário    |   apagar as vacinas  |   remover as informações   | Should  |
|  EP02   |  FT06   | US22  |   usuário    |   registrar dados sobre as visitas ao veterinário  |   manter o registro da saúde do pet   | Must  |
|  EP02   |  FT06   | US23  |   usuário    |   visualizar histórico de visitas ao veterinário  |   me manter informado   | Must  |
|  EP02   |  FT06   | US24  |   usuário    |   agendar notificações de retorno  |   ser lembrado da futura visita   | Must  |

## Bibliografia

1. REINEHR, Sheila. Engenharia de requisitos-Porto Alegre, 2020.

2. BECKER, Alice. Aprenda como o método MoSCoW poderá ajudá-lo a priorizar as tarefas da sua empresa. Disponível em <https://www.voitto.com.br/blog/artigo/metodo-moscow>. Acesso: 04/08/2021.

</div>