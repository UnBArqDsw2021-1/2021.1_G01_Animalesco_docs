# <center> Metodologia do projeto

#### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 02/08/2021 |  0.1   | Criação do documento | Durval Carvalho |
| 04/08/2021 |  1.0   | Revisão e reestruturação do documento | Hugo Sobral |

<div align="justify">


## 1. Introdução

Este documento de metodologia busca descrever as abordagens, metodologias e processos utilizados durante o desenvolvimento do projeto. Aqui estão descritas quais metodologias foram utilizadas como referência, além de quais métodos foram adotados e customizados para o nosso contexto. Este documento também visa explorar as maneiras como a equipe se organizou e realizou a comunicação durante o projeto.

## 2. Objetivo

Este documento tem como objetivo documentar as metodologias e abordagens utilizadas, assim como todos os processos adotados durante o desenvolvimento do projeto.

## 3. Metodologias e abordagens

Todas as metodologias adotadas durante esse projeto tem relação com dois princípios fundamentais do desenvolvimento ágil de software. Esses princípios são:

> * Os **indivíduos e suas interações** acima de procedimentos e ferramentas
> * A **capacidade de resposta a mudanças** acima de uma plano pré-estabelecido
>
> -- <cite> Manifesto Ágil [1] </cite>

A partir de decisões tomadas em conjunto e com base nestes princípios, foram utilizado partes de várias metodologias já conhecidas como SCRUM e XP. Estas estruturas atômicas foram utilizadas em conjunto e de forma customizada a fim de formar metodologia híbrida que melhor se adaptasse ao nosso contexto.

### 3.1 SCRUM

O SCRUM é um _framework_ de gerenciamento de projetos, da organização ao desenvolvimento ágil de produtos complexos e adaptativos com o mais alto valor possível, através de várias técnicas, utilizando desde o início de 1990 e que atualmente é utilizado em mais de 60% dos projetos ágeis em todo o mundo. [[2]](https://pt.wikipedia.org/wiki/Scrum_(desenvolvimento_de_software))

Essa metodologia define várias atividades que devem ocorrer durante o processo de desenvolvimento. No nosso contexto foram adotadas as seguintes atividades: **_Product Backlog_**, **_Sprints_**, **_Sprint Planning_**, **_Sprint Review_** e **_Daily Meeting_**.


#### **3.1.1 Product Backlog**

Product backlog é um dos artefatos descritos pelo SCRUM. Este artefato é uma lista dinâmica de requisitos do projeto, ou seja, são as atividades e limitações que o projeto deve realizar ou está sujeito para que seja bem sucedido. [[2]](https://pt.wikipedia.org/wiki/Scrum_(desenvolvimento_de_software))

No nosso contexto, essa lista de requisitos são as [_issues_ do nosso repositório](https://github.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/issues). Essas _issues_ são abstrações de cartões de tarefas que descrevem o que deve ser feito e as limitações como tempo e pessoas alocadas.

O único campo obrigatório na criação de uma issue é o título. Porém é de suma importância que tais issues possuam uma descrição muito bem escrita. A experiência dos integrantes do projeto demonstrou que issues mal escritas são mal interpretadas e resultam em entregas de baixa qualidade ou até mesmo confusão para com os entregáveis de cada issue.

<!-- Visando padronizar a criação de issues no nosso projeto, foi criado um template de criação onde é preciso definir outros campos. Esses campos são: Descrição, Critérios de aceitação e tarefas.

Na descrição irá descrever a atividade da issue, inserindo informações necessárias para o entendimento. Nesse campo deve ser evitado descrições genéricas e ambíguas. É comum a utilização das próprias _user stories_ serem inseridas no campo de descrição das issues.

Nos critérios de aceitação deve descrever quais serão os indicadores usados para verificar a qualidade do trabalho entregue. Alguns exemplos de critérios de aceitação são:

* Esse documento deve conter tabela de versionamento
* Esse documento deve conter as referências bibliográficas

Por fim, as tarefas são uma lista de sub atividades que devem ser feitas para que a issue seja concluída. Essas atividades são opcionais para a criação da issue, pois nem sempre pode ser possível definí-las durante a criação de uma tarefa. Alguns exemplos de tarefas são:

* Buscar referência
* Analisar os projetos de semestres anteriores -->

#### **3.1.2 Sprints**

Uma sprint é a unidade básica de tempo durante o desenvolvimento na metodologia SCRUM. As sprints podem durar entre uma semana a um mês, e são um esforço dentro de uma faixa de tempo. Esse faixa de tempo deve ser relativamente curta para possibilitar entregas parciais do sistema, busca-se tais entregas parciais para que seja possível gerar valor de maneira contínua ao projeto e que seja possível a avaliação dinâmica e periódica do trabalho desenvolvido. [[2]](https://pt.wikipedia.org/wiki/Scrum_(desenvolvimento_de_software))

No nosso contexto, foi definido que as sprints irão durar entre 5 a 7 dias.

#### **3.1.3 Sprint Planning**

_Sprint planning_ é um evento de planejamento onde será definido quais tarefas (no nosso caso _issues_) do _product backlog_ serão feitas na próxima _sprint_. [[2]](https://pt.wikipedia.org/wiki/Scrum_(desenvolvimento_de_software))

No nosso contexto, o projeto e suas entregas estão definidos no plano de ensino da disciplina. Assim foram criadas [4 milestones](https://github.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/milestones), cada uma representando um ponto de controle da disciplina, com cada milestone agrupando suas respectivas tarefas.

Desse modo, todas as atividade e seus prazos são conhecidas, restando somente a definição dos responsáveis pela sua realização.

Com isso em mente, são realizadas reuniões periódicas a cada segunda-feira, às 20h. Estas reuniões servem o propósito de definição de quais atividades devem ser priorizadas e alocadas na sprint seguinte com base na milestones mais próxima da data atual. Uma vez definido o _backlog da sprint_; o _backlog da sprint_ se assemelha bastante com o _product backlog_, com a diferença localizada no escopo de cada um dos backlogs; são definido os responsáveis e a data de término da sprint.

#### **3.1.4 Sprint Review**

_Sprint Review_ é um evento de validação e verificação que ocorre antes do _Sprint planning_. Durante esse evento, as entregas da sprint anterior são analisados assim como é feita a verificação da qualidade dos artefatos, sejam estes documentais ou de código, gerados. Após tal análise, a atividade pode ser concluída ou pode voltar para o _product backlog_, associada a um pedido de correção. Durante esse evento também são discutidas dificuldades enfrentadas e pontos de melhoria para a próxima sprint. [[2]](https://pt.wikipedia.org/wiki/Scrum_(desenvolvimento_de_software))

No nosso contexto, os _sprints review_ ocorrem em duas etapas. A etapa de validação e verificação ocorre durante a sprint, sempre que um _pull request_ é criado. Pull request é a abstração da entrega de uma atividade. As atividades são realizadas em um ambiente individual de desenvolvimento, esse ambiente é um clone do ambiente original onde fica as atividades entregues, esse ambiente é conhecido por branches. Sempre uma atividade é concluída em seu ambiente clone, é criado um _pull request_, isso é, um pedido para que as alterações criadas no ambiente clone vá para o ambiente original. É nessa etapa que ocorre a validação e verificação. Antes do _pull request_ ser aceito é revisado a atividade.

A segunda etapa ocorre antes da _sprint review_, onde é discutido as dificuldades enfrentadas e as sugestões de melhoria para a próxima sprint.

#### **3.1.5 Daily Meeting**

Na metodologia SCRUM é recomendado que se realize reuniões de status do projeto diariamente, sendo essa reunião conhecida como _daily meeting_. Essa reunião é sempre realizada em um mesmo horário e deve durar no máximo 15 minutos. O objetivo é deixar todos os integrantes cientes do trabalho um do outro, desse modo cada participante deve responder a três perguntas:
* O que você tem feito da daily passada para a daily atual?
* O que você está planejando fazer da daily atual para a daily de amanhã?
* Você tem algum problema impedindo você de realizar sua atividade?

No nosso contexto, as _dailies_ serão realizadas de forma assíncrona, utilizando a ferramenta Telegram. Foi criado um grupo com todos os membros do projeto, onde diariamente é enviado a respostas das três perguntas descritas acima. Essa abordagem assíncrona se provou necessária devido a dificuldade de encontrar um momento do dia onde todos os membros pudessem participar.

### 3.2 Kanban

Kanban é um quadro de cartões, sendo que cada cartão representa uma atividade, onde é controlado os fluxos em que cada cartão se encontra. Esses fluxos podem ser vários, dependendo do processo em questão, mas no geral são 3 fluxos principais: "a fazer", "fazendo" e "feito".

No nosso contexto, o kanban foi dividido em 5 fluxos: _project backlog_, _sprint backlog_, _in progress_, _review_ e _done_. No primeiro processo é onde ficam todos os cartões de tarefas mapeados até o momento. No segundo fluxo ficam os cartões de tarefa que serão realizados na sprint atual, no terceiro fluxo ficam as cartões cuja as tarefas já foram iniciadas, no fluxo _review_ ficam as tarefas que já foram concluídas e estão esperando por revisão de terceiros, e no último fluxo, _done_, ficam as tarefas que já foram revisadas e aprovadas. [[3]](https://pt.wikipedia.org/wiki/Kanban).

<!-- O Kanban do nosso projeto pode ser encontrado no seguinte link: <p style="color: red;">TODO: Adicionar link para o Kanban</p>. -->

### 3.3 Extreme Programming (XP)

Extreme Programming é uma metodologia com foco em agilidade de equipes e qualidade de projetos, apoiada em valores como simplicidade, comunicabilidade e feedback. Objetivando a execução de projetos dentro prazo e do orçamento, fazendo que o cliente fique satisfeito com os resultados sem que a equipe do projeto seja sobrecarregada. [[4]](https://www.devmedia.com.br/extreme-programming-conceitos-e-praticas/1498).

No nosso contexto, as seguintes ferramentas do XP foram adotadas e adaptadas:

#### **3.3.1 Small Releases**

Todas as tarefas do projeto são planejadas para serem `pequenos entregáveis`, para que assim 1 pessoa consiga entregar dentro do time-box do projeto.

#### **3.3.2 Refactoring**

Todos os entregáveis do projeto são revisados por membros do grupo que não estiveram envolvidos na criação, dessa forma reduzindo o enviesamento e aumentando a qualidade do artefato.

#### **3.3.3 Propriedade coletiva e "Programação" Pareada**

Essas duas atividades buscam fazer com que todos os membros do tipo, ou a maior parte deles, tenham o sentimento de posse sobre os artefatos do projeto. E assim evitar ao máximo possível o sentimento de "Isso não foi eu que fiz, então não é problema meu".

Com o objetivo de se criar um propriedade coletiva de todos os artefatos do projeto, as atividades chaves são sempre atribuidas para mais de uma pessoa, e revisada por terceiros. Desse modo se envolve várias pessoas durante a conclusão da tarefa, difundindo conhecimento gerado e a "posse" sobre o artefato.

## 4. Plano de comunicação

Com o objetivo de evitar problemas na comunicação dos membros e consequentemente gerar problemas nas entregas do projeto, foi pensado no plano de comunicação da equipe.

Oficialmente, toda a comunicação deve ser realizada por meio de três canais:
* 1. O o site de hospedagem de repositórios, GitHub;
* 2. Pelo Telegram;
* 3. Pelo Microsoft Teams;

As tarefas são delegadas por meio de issues e pull request, e toda definição de responsabilidade deve ser feito por meio do Github. Também utilizamos os comentários das próprias issues para documentar e rastrear evoluções em tempo real de cada uma das tarefas.

O Telegram é utilizado para realizar a comunicação assíncrona da equipe, isto é, foi criado um canal de texto para a comunicação acerca de temas pertinentes ao projeto e à disciplina de Arquitetura e Desenho de Software. O Telegram também é utilizado para a realização das _dailies meetings_, descritas anteriormente neste documento.

O Microsoft Teams é utilizado para eventos síncronos e que necessitem de chamadas por voz e/ou vídeo. Foi criada uma organização dentro do aplicativo para hospedar este canal de comunicação da equipe.

É fortemente desencorajado a utilização de canais não oficiais para abordar temas pertinentes sobre o projeto. Isso por que se busca deixar documentado todas as atividades realizadas durante o desenvolvimento, e comunicação por canais não oficiais dificultam essa documentação.

### Bibliografia

* [1] Manifesto Ágil, Disponível em: [https://agilemanifesto.org/iso/ptbr/manifesto.html](https://agilemanifesto.org/iso/ptbr/manifesto.html)

* [2] SCRUM, Metodologia Ágil. Disponível em: [https://pt.wikipedia.org/wiki/Scrum_(desenvolvimento_de_software)](https://pt.wikipedia.org/wiki/Scrum_(desenvolvimento_de_software))

* [3] KANBAN. Disponível em [https://pt.wikipedia.org/wiki/Kanban](https://pt.wikipedia.org/wiki/Kanban)

* [4] Extreme Programming. Disponível em [https://www.devmedia.com.br/extreme-programming-conceitos-e-praticas/1498](https://www.devmedia.com.br/extreme-programming-conceitos-e-praticas/1498)


</div>
