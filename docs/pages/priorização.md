# <center> Priorização de requisitos

#### Histórico de Versão

|    Data    | Versão |      Descrição       |     Autor(es)     |
| :--------: | :----: | :------------------: | :---------------: |
| 04/08/2021 |  0.1   | Criação do documento | Lorrany Oliveira  |
| 05/08/2021 |  0.2   | Criação do quadro de histórias do usuario | Daniela Soares  |
| 05/08/2021 |  0.1   | Priorização dos requisitos | Lorrany Oliveira/Daniela Soares  |

<div align="justify">

## 1. Introdução
A priorização de requisitos é um procedimento fundamental na hora da produção de um softare, além de ser um dos fatores que minimiza a possibilidade de ocorrer uma falha na produção da aplicação. Isso ocorre porque por meio da priorização você analisa todos os requisitos e ver qual deles tem uma prioridade maior a ser implementada e por meio disso você cria algo similar a uma ordem de implementação.

A forma que irá ocorrer a priorização depende de diversos fatores, como por exemplo, os tipos de tecnologias que você estará utilizando, qual o objetivo que você deseja atingir, o contexto que você está inserido entre outros. Desta forma, existem diversas técnicas que podem ser utilizadas para colaborar na priorização de requisitos, a qual deve ser escolhida com base no que mais se adequa ao seu projeto.

<br/>

## 2. MoSCoW
Uma das técnicas de priorização de requisitos, é o MoSCoW. É uma técnica que foi desenvolvida por Dai Clegg na década de 90, enquanto ele trabalhava na Oracle, tendo como objetivo auxiliar a metodologia de desenvolvimento de sistemas dinâmicos. Seu nome é um acrônimo, o que facilita a aplicação da técnica e sua memorização. As letras em maiusculo indicam a ordem que deve ser seguida durante o processo:

 M - Must have: são os requisitos indispensáveis para a entrega do projeto, afetando diretamente o resultado de sucesso do seu projeto.

 S - Should have: são os requisitos que não são críticos para a entrega do projeto,  mas que seriam bom serem implementados.  

 C - Could have: são os requisitos que podem ser implementados caso haja recursos financeiros e de tempo.

 W - Wont have: são os requisitos que podem ser implementados posteriormente caso haja uma atualização ou melhoria do sistema.  

<br/>

## 3. Objetivo
O presente documento tem como objetivo a demostração do resultado da aplicação da técnica de priorização de requisitos MoSCoW, que foi aplicada no resultado da elicitação de requisitos usando as diretrizes desta técnica como guia para classificação de quais deveriam ser priorizados ou não, e qual o grau de sua importância para o sucesso da aplicação.  

<br/>

## 4. Priorização das Histórias de Usuário

|  Épico  | Feature |  ID   |   Eu como    |   Desejo  |   Para   | Prioridade  |
| :-----: | :----:  |:-----:| :----------: | :-------: |:--------:| :---------: |
|  EP01   |  FT01   | US01  |    usuário   |poder realizar o cadastro | ter acesso a aplicação.    |   Must        |
|  EP01   |  FT01   | US02  |   usuário    | alterar meus dados | manter o perfil atualizado      |   Should         |
|  EP01   |  FT01   | US03  |   usuário    |   apagar meus dados  |   remover o perfil   | Could  |
|  EP01   |  FT02   | US04  |   usuário    |   poder realizar login  |    acessar a aplicação   | Must  |
|  EP01   |  FT02   | US05  |   usuário    |   resgatar a senha  |   realizar o login   | Must  |
|  EP02   |  FT03   | US06  |   usuário    |   poder cadastrar meu(s) pet(s) na aplicação  |   realizar o controle das informaçoẽs dele(s)   | Must  |
|  EP02   |  FT03   | US07  |   usuário    |   poder alterar os dados do(s) meu(s) pet(s)  |   manter o(s) perfil(is) atualizado(s)   | Must  |
|  EP02   |  FT03   | US08  |   usuário    |   poder deletar o(s) registro(s) do(s) meu(s) pet(s)  |   remover os dados da aplicação   | Could   |
|  EP02   |  FT04   | US09  |   usuário    |   poder registrar os banhos do(s) meu(s) pet(s)  |   manter o controle   | Must  |
|  EP02   |  FT04   | US10  |   usuário    |   poder acessar o histórico de banho(s) do(s) meu(s) pet(s)  |   saber quando dar banho novamente   | Must  |
|  EP02   |  FT04   | US11  |   usuário    |   adicionar lembrete sobre o(s) banho(s)  |    não esquecer dele(s)   | Should  |
|  EP02   |  FT04   | US12  |   usuário    |   deletar o(s) banho(s) do(s) pet(s)  |   remover a(s) informação(ões)   | Could  |
|  EP02   |  FT05   | US13  |   usuário    |   registrar um medicamento  |   realizar o controle dele   | Must  |
|  EP02   |  FT05   | US14  |   usuário    |    adicionar um lembrete  |   não esquecer o horário da administração do medicamento   | Must  |
|  EP02   |  FT05   | US15  |   usuário    |   poder remover o medicamento  |   quando finalizar o seu período de administração   | Could  |
|  EP02   |  FT05   | US16  |   usuário    |   registar quando o medicamento foi dado  |   manter o histórico atualizado   | Must  |
|  EP02   |  FT06   | US17  |   usuário    |   visualizar as vacinas do pet  |   me informar   | Must  |
|  EP02   |  FT06   | US18  |   usuário    |   registrar as vacinas que o pet tomau  |   manter o dados atualizados   | Must  |
|  EP02   |  FT06   | US19  |   usuário    |    apagar as vacinas  |   remover as informações   | Could  |
|  EP03   |  FT08   | US20  |   usuário    |   registrar dados sobre as visitas ao veterinário  |   manter o registro da saúde do pet   | Must  |
|  EP03   |  FT08   | US21  |   usuário    |   visualizar histórico de visitas ao veterinário  |   me manter informado   | Must  |
|  EP03   |  FT08   | US22  |   usuário    |   visualizar um relátorio sobre a saúde do pet  |   ter acesso fácil a isso   | Should  |

## 5. Priorização dos Requisitos não funcionais 


|    ID    | Requisito |     Prioridade     |
| :------: | :-------: | :---------------:  |
| RNF01    | A aplicação deve estar disponível em celulares Android        |        Must            |
| RNF02    | A aplicação deve estar disponível em celulares IOS       |       Should             |
| RNF03    |  A aplicação deve estar disponível 24/7         |      Must            |
| RNF04    |   A aplicação não deve ocupar muito espaço na memória em disco dos celulares     |   Should              |
| RNF05    |   A aplicação deve ser segura        |      Must              |
| RNF06    |   A aplicação deve ser gratuita       |     Must               |
| RNF07    |   A aplicação deve armazenar apenas informações relevantes dos pets        |      Must              |
| RNF08    |  A aplicação deve oferecer uma boa experiência de usuário         |       Must             |
| RNF09    |    A aplicação deve ser rápida       |     Should               |
| RNF10    |   A aplicação deve ter uma interface agradável e simples        |     Must               |
| RNF11    |   A aplicação deve ser confiável em termos de informação        |     Must               |
| RNF12    |  Autenticação de usuário         |    Must                |

## Bibliografia
1. REINEHR, Sheila. Engenharia de requisitos-Porto Alegre, 2020.
2. BECKER, Alice. Aprenda como o método MoSCoW poderá ajudá-lo a priorizar as tarefas da sua empresa. Disponível em <https://www.voitto.com.br/blog/artigo/metodo-moscow>. Acesso: 04/08/2021.
</div>