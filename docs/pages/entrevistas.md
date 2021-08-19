# <center> Entrevistas

#### Histórico de Versão
|    Data    | Versão | Descrição            |    Autor(es)    |
| :--------: | :----: | :------------------: | :-------------: |
| 30/07/2021 |  0.1   | Criação do roteiro de entrevista | Hugo Sobral, Daniela Soares, João Vitor, Lorrany Souza e Vinicius Oliveira |
| 02/08/2021 |  0.2   | Inclusão da introdução, reestruturação do documento e inclusão das entrevistas | Hugo Sobral |
| 03/08/2021 |  0.3   | Revisão do documento e ajuste da bibliografia | Hugo Sobral |
| 03/08/2021 |  1.0   | Inclusão dos requisitos elicitados a partir das entrevistas | Hugo Sobral |
| 04/08/2021 |  1.1   | Revisão do documento | Durval Carvalho |
| 18/08/2021 |  1.2   | Ajuste no título do documento | Leonardo Gomes |

<div align="justify">

## 1. Introdução

A entrevista é uma técnica de elicitação de requisitos  que provê uma fácil utilização e que retorna bons resultados à termos de obtenção de recursos e insumos a um determinado projeto de software. As entrevistas são baseadas em um roteiro de perguntas que deve ser feito a uma pessoa que se enquadra no perfil de usuário do projeto, tais pessoas também podem ser denominadas de _Stakeholders_, contudo, não se deve restringir a abrangência dos _Stakeholders_ apenas para os usuários. Para o caso do Animalesco, o perfil de usuário foi traçado e formulado através de outra técnica de elicitação, o Questionário.
Desta forma, as entrevistas foram realizadas com o intuito de coletar amostras de dados úteis para a melhor compreensão das necessidades do aplicativo.

## 2. Roteiro de entrevista

1. Você possui algum pet?
2. Qual a espécie do seu(s) pet(s)?
3. Qual a frequência que você leva seu pet ao veterinário?
4. Qual a frequência que você dá banho no seu pet?
5. Você realiza algum controle das datas de ida do seu pet aos estabelecimentos das perguntas anteriores?
6. Seu pet toma algum tipo de medicação?
7. O seu pet possui carteira de vacinação?
8. Seu pet está com a vacinação e com as medicações (como vermífugos e anti-pulgas) em dia?
9. Como você faz o controle das vacinações e medicações do seu pet?
10. Já te ocorreu de, por algum motivo, esquecer de fornecer a medicação ou levar seu pet para a vacinação?
11. Você acharia interessante ter um App que realiza o controle das medicações que fornece um resumo das idas do seu pet ao veterinário/petshop?

## 3. Entrevistas realizadas

[**Entrevista 1 - Micaella Gouveia, 22 anos**](pages/entrevistas/entrevista_01.md)

[**Entrevista 2 - Maira Menezes, 20 anos**](pages/entrevistas/entrevista_02.md)

[**Entrevista 3 - Anieli Juliana, 21 anos**](pages/entrevistas/entrevista_03.md)

[**Entrevista 4 - Esio Gustavo, 24 anos**](pages/entrevistas/entrevista_04.md)

[**Entrevista 5 - Rebeca Diniz, 21 anos**](pages/entrevistas/entrevista_05.md)

[**Entrevista 6 - Gabriela Lopes, 21 anos**](pages/entrevistas/entrevista_06.md)

## 4. Requisitos elicitados a partir das entrevistas
### 4.1 Requisitos funcionais

|  ID  | NOME |
| :--: | :--: |
| RF01 | Cadastro de usuário |
| RF02 | Login |
| RF03 | Cadastro de pets do usuário |
| RF04 | Atualizar dados de pets do usuário |
| RF05 | Excluir pets dos usuários |
| RF06 | Registro de passeios do pet |
| RF07 | Histórico de passeios do pet |
| RF08 | Registro de banhos do pet |
| RF09 | Histórico de banhos do pet |
| RF10 | Registro de idas ao veterinário do pet |
| RF11 | Histórico de idas ao veterinário do pet |
| RF12 | Registro de medicação do pet |
| RF13 | Histórico de medicação do pet |
| RF14 | Disponibilizar cartão de vacinação digital para o pet |
| RF15 | Criação de eventos no calendário para idas ao veterinário |
| RF16 | Criação de eventos no calendário para a vacinação |
| RF17 | Notificação para medicação |
| RF18 | A aplicação deve ter integração com os principais aplicativos de agenda |

### 4.2 Requisitos não funcionais

|  ID   | NOME |
| :--:  | :--: |
| RNF01 | A aplicação deve estar disponível em celulares Android |
| RNF02 | A aplicação deve estar disponível em celulares IOS |
| RNF03 | A aplicação deve estar disponível 24/7 |
| RNF04 | A aplicação não deve ocupar muito espaço na memória em disco dos celulares |
| RNF05 | A aplicação deve ser segura |
| RNF06 | A aplicação deve ser gratuita |
| RNF07 | A aplicação deve persistir apenas informações relevantes dos pets |
| RNF08 | A aplicação deve oferecer uma boa experiência de usuário |
| RNF09 | A aplicação deve ser rápida |
| RNF10 | A aplicação deve ter uma interface agradável e simples |
| RNF11 | A aplicação deve ser confiável a termos de informação |


##  Bibliografia

1. Técnicas para levantamento de Requisitos. **DevMedia**. Disponível em https://www.devmedia.com.br/tecnicas-para-levantamento-de-requisitos/9151 (último acesso em 02/08/2021)
2. BORGES, K.; DUTRA, L.; FREITAS, E. Entrevista. **Pax App**. Disponível em https://pax-app.github.io/Wiki/#/docs/DS/dinamica-e-seminario-1/Entrevista (últio acesso em 02/08/2021)
3. ALVES, G.; DAVI, G.; IGOR, P.; GOUVEIA, M.; PATROCÍNIO, S. Entrevista. **Stock**. Disponível em https://unbarqdsw.github.io/2020.1_G12_Stock/#/Elicitation/Entrevista (último acesso em 02/08/2021)
4. KADER, S. Entrevistas. **Requisitos Habitica**. Disponível em https://requisitos-habitica.netlify.app/Entrevista (último acesso em 02/08/2021)

</div>