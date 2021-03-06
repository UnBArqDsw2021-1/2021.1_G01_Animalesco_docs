# <center> Reutilização de software

#### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 03/10/2021 |  0.1  | Escrita da introdução | João Vitor Farias |
| 04/10/2021 |  0.2  | Escrita dos benefícios e obstáculos, e das técnicas de reuso | João Vitor Farias |
| 04/10/2021 |  0.3  | Escrita dos tipos de reutilização e adição da bibliografia | João Vitor Farias |
| 04/10/2021 |  0.4  | Revisão e reformulando tópico 4 | Daniela Soares |
| 12/10/2021 |  0.5  | Reestruturação do tópico 3 | João Vitor Farias |

<div align="justify">

## 1. Introdução
No ano de 1968, na conferência de Engenharia de Software da OTAN (Organização do Tratado do Atlântico Norte), pela primeira vez é colocado em discussão a ideia de reutilização de software a partir do artigo de McIlroy, que visava o reuso de pequenas partes de softwares para superar a crise de desenvolvimento de soluções da época. Esta crise foi causada pela dificuldade em construir grandes sistemas confiáveis de maneira controlada e com boa relação custo-benefício.

Após a proposição da ideia, os estudos sobre o tema prosseguiram de modo a aplicar o reuso em partes cada vez maiores dos sistemas. Em conjunto com este progresso, pesquisadores começaram a unir os conceitos de reuso com a utilização de objetos. Com o avanço dos estudos sobre a prática de reuso, na década de 1990 esta abordagem se estendeu para os componentes, e na década de 2000 o reuso chegou nos serviços de sistemas distribuídos, para facilitar a troca de informação.  

Para uma melhor compreensão, podemos definir a reutilização de software como uma abordagem que procura reusar partes do processo de construção de um software que já foi desenvolvido, não somente o código, mas todos os procedimentos utilizados durante a criação dele. Desta forma, é necessário pensar em um software como um produto de longa vida, que irá receber manutenções evolutivas e corretivas ao longo do tempo, e elas não deverão ocorrer de maneira custosa.

Segundo Ezran (Ezran et al. 2002 apud Ferreira e Naves , 2011), alguns estudos na área de reuso mostram que 40% a 60% de código é reutilizável de uma aplicação para outra, 60% do projeto e do código são reutilizáveis em aplicações de negócio, 75% das funções são comuns em mais de um programa, e somente 15% do código de um programa é único. Fica perceptível o potencial da aplicação do reuso de software, tendo um impacto significativo no processo de desenvolvimento de um software.

## 2. Benefícios e obstáculos
Algumas das principais vantagens do reuso de software  durante o processo de desenvolvimento são: 
* Maior produtividade no processo de desenvolvimento;
* Aumento da qualidade do software;
* Diminuição do tempo/prazo de entrega do software; 
* Aumento da confiança do produto, por conta de do software reusado já ter sido utilizado e testado;
* Conformidade com padrões, algumas funcionalidades ou características presentes em um projeto de interface já estão pré-definidas, de modo a apresentar o mesmo formato de interface para o usuário [1].

Porém, o mau uso desta prática pode gerar alguns obstáculos, entre eles estão:
* Custo de manutenção, caso o código fonte de um sistema reutilizável não esteja disponível, gera um aumento do custo de manutenção, por conta que os elementos do software podem se tornar cada vez mais incompatíveis com as mudanças necessárias para adaptação do sistema [1];
* Não produzi aqui, sendo uma premissa que ocorre quando os desenvolvedores tendem a reescrever componentes, pois acreditam que podem melhorá-los;
* Criação, manutenção e uso de uma biblioteca de componentes, é uma prática que pode sair bem cara, pois as atuais técnicas de classificação e recuperação de componentes de software são imaturas para garantir o sucesso deste procedimento.


## 3. Formas de reuso de software

A reutilização pode ser executada de formas diferentes, dependendo da capacidade do ambiente de implementação. A técnica mais simples é copiar o código de um lugar para outro. Isso não é aconselhável, pois não é realmente reutilização. Várias cópias de código fonte são difíceis de manter e eventualmente podem divergir umas das outras. A reutilização tem por objetivo realizar o uso de parte de um software/projeto para atender determinada demanda, como forma de aumentar a qualidade e reduzir a sobrecarga.

### 3.1. Framework

Os frameworks dão suporte ao reuso de software, por fornecer uma arquitetura de esqueleto para a aplicação. A arquitetura é definida por classes de objetos e suas interações. As classes são reutilizadas diretamente e podem ser implementadas no projeto por meio de recursos como a herança. Nos frameworks os aspectos da arquitetura são divididos em hot-spots (variáveis) e frozen-spots (invariáveis)

* **Hot-spots:** são partes específicas de sistemas  individuais, que são projetados para serem genéricos e geralmente são representados por classes abstratas.

* **Freozen-spots:** corresponde a maior parte da arquitetura de um sistema,  permanecem fixos em todas as instânciações do framework e também são conhecidos como “core” do framework.

Já quanto aos tipos os frameworks, são divididos em três categorias:

* **Caixa branca:** orientado a hot-spots, este tipo baseia-se no conceito de herança e ligação dinâmica.

* **Caixa preta:** orientado a frozen-spots, possibilitada a composição de objetos sem detalhes internos.

* **Caixa cinza:** híbrido de caixa branca com caixa preta, permite adaptação tanto por herança, quanto por composição de componentes.

### 3.2. Plugins

No modelo de plugins o software é composto por dois componentes: um único sistema nuclear e os módulos plug-ins. Desta forma a aplicação está dividida entre os módulos de plug-ins independentes e o sistema nuclear básico, de forma a proporcionar extensibilidade, flexibilidade e isolamento das principais características do núcleo.

### 3.3. Serviços

O modelo de serviços tem por objetivo o fornecimento de um serviço independente da aplicação que o usa. Os serviços podem ser desenvolvidos de forma especializada, com a finalidade de atender determinada demanda, e podem ser oferecidos para uma variedade de usuários de serviço de diferentes organizações.

### 3.4. Componentes

Os componentes são abstrações de nível mais alto do que objetos e são definidos por suas interfaces. Eles são independentes, então não interferem na operação uns dos outros, podem ser alterados sem afetar o restante do sistema e  comunicam-se por meio de interfaces bem definidas. As infraestruturas dos componentes oferecem uma gama de serviços padrão que podem ser usados em sistemas de aplicações, o que reduz a quantidade de códigos novos a serem desenvolvidos.

### 3.5. Linhas de produto de software

O desenvolvimento através de linhas de produto de software é utilizada para conseguir o reuso de forma bastante abrangente. A aplicação dessa abordagem possui a premissa de reuso de um conjunto de características de um sistema que satisfaça determinada demanda do mercado, sendo essas características:

* Requisitos e análise de requisitos;
* Modelo de domínio;
* Arquitetura e design de software;
* Documentação;
* Testes componentes.

### 3.6. Engenharia reversa e reengenharia

De acordo com Ferreira e Naves (2011), a engenharia reversa é uma área da reengenharia que pode ser considerada a reconstrução de algo do mundo real com o objetivo de entender a sua construção buscando  o entendimento necessário para melhorá-lo. Dessa forma, ela torna-se uma importante técnica para auxiliar no reuso de software, visto que é possível obter componentes, funções e abstrações, que são às vezes mais altas que o próprio código fonte de um programa, o que permite obter diferentes visões a partir dos níveis de abstração de um sistema. Entre essas possíveis visualizações do software as principais são:

* **Visão em nível implementacional**, que abstrair características da linguagem de programação e características específicas da implementação;
* **Visão em nível de domínio**, que abstrai o contexto em que o sistema está  operando, ou seja, o porquê do sistema a ser desenvolvido.

## Bibliografia

* [1] FERREIRA, H. N. M., NAVES, T. F. Reuso de software: suas vantagens, técnicas e práticas. 2011. Faculdade de Computação – Universidade Federal de Uberlândia (UFU). Uberlândia, Minas Gerais.

* [2] SILVA, E. R., SPÍNOLA, R. O., KALINOWSKI, M. Implementando Gerência de Reutilização de Software. 2013. Edição 59, Engenharia de Software Magazine. Disponìvel em <https://www.researchgate.net/profile/Marcos-Kalinowski/publication/256091379_Implementando_Gerencia_de_Reutilizacao_de_Software/links/0c960521abe1c16097000000/Implementando-Gerencia-de-Reutilizacao-de-Software.pdf> (Último acesso em 03/09/2021).

* [3] CYBULSKI, J. L. Introduction to Software Reuse. Department of Information Systems. The University of Melbourne. Austrália. Disponìvel em <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.83.7716&rep=rep1&type=pdf> (Último acesso em 03/09/2021).

* [4] Reutilização de código. **Wikipédia**. Disponìvel em <https://pt.wikipedia.org/wiki/Reutiliza%C3%A7%C3%A3o_de_c%C3%B3digo> (Último acesso em 04/09/2021).

* [5] Reutiçização de Software. **Stock**. Disponível em: https://unbarqdsw.github.io/2020.1_G12_Stock/#/Architecture/EstudoDirigido/reutilizacao?id=formas-comuns-de-reutiliza%c3%a7%c3%a3o (último acesso em 11/10/2021).

</div>
