# Backlog do produto

## Histórico de versão

| Data | Versão | Descrição | Autor |
|------|--------|-----------|-------|
| 04/08/2021 | 0.1 | Estrutura inicial do documento | Rafael Leão e João Vitor Farias |
| 05/08/2021 | 0.2 | Revisão do documento | Hugo Sobral |

## 1. Introdução
O _backlog do produto_, tradução livre de _product backlog_, é um artefato descrito pela metodologia Scrum que consiste em uma lista de tarefas que descrevem as funcionalidades e comportamentos que são esperados do produto quando este alcança a conjuntura de conclusão. O _backlog do produto_ se organiza de maneira a separar as atividades por diferentes granularidades, estas são:
- Epics;
- Features;
- User stories.

Os _epics_ são as estruturas mais complexas a termos de granularidade de um backlog. Os epics abrigam um conjunto de _features_.

As _features_, por sua vez, descrevem um conjunto de funcionalidades e requisitos não funcionam para o projeto. Uma _feature_ agrupa um conjunto de _user stories_. Ao se realizar uma analogia à termos computacionais, temos que as _features_ são quase como componentes de um módulo; para este caso fictício, os módulos seriam definidos como os _epics_; que podem ser dividos em estruturas atômicas. 

Já as _user stories_ definem pedaços atômicos de funcionalidades. São as _user stories_ que guiam a delegação de tarefas para as sprints do projeto (o conceito de sprints e o processo de delegação de tarefas foi descrito no [documento de metodologia](pages/metodologia-do-projeto.md)).


## 2. Metodologia

A partir das técnicas de elicitação realizadas pela equipe, foi possível realizar o mapeamento dos requisitos funcionais e não funcionais do projeto. Os insumos levantados pelas técnicas de [brainstorming](), [questionário]() e [entrevistas]() foram a base para a identificação das necessidades do Animalesco como solução computacional.

Desta forma, foram realizados encontros em equipe para a identificação destes requisitos e devida tradução para o formato do _backlog do produto_, isto é, a escrita das necessidades do projeto de acordo com a granularização descrita pelo artefado de backlog.

## 3. Objetivo

Este documento tem como objetivo a identificação e devido agrupamento dos requisitos do Animalesco. Este documento apresenta, por meio de tabelas, as estruturas atômicas de tarefas relacionadas à cada um dos temas identificados anteriormente pelas técnicas de elicitação utilizadas pela equipe.

## 4. Requisitos funcionais

Os requisitos funcionais foram descritos por meio de uma tabela que os classifica em epics, features e user stories.

Vale ressaltar que as user stories seguem o padrão de papel-ação-valor:

>*eu como __tipo de usuário__,
desejo __uma ação__
para que __um benefício/valor__.*

### 4.1 Épicos
É uma história de usuário que ainda não foi detalhada, é muito grande ou ainda possui muita incerteza e portanto não pode ser transformada em incremento do produto.

| ID  | Épico|
| --- | ----- |
| EP01 | Gerenciamento de usuário |
| EP02 | Gerenciamento de pet |
| EP03 | Acompanhamento de idas ao veterinário|

### 4.2 Features
Uma feature é uma funcionalidade do sistema que entrega um benefício ou resolve um problema real do cliente.

|ID |Feature | ID Épico |
|------ |-- | ----- |
|FT01| Cadastro de usuário |EP01|
|FT02| Fazer login |EP01|
|FT03| Cadastro de pet |EP02|
|FT04| Controle banhos |EP02|
|FT05| Controle de medicamentos |EP02|
|FT06| Controle de vacinas|EP02|
|FT07| Controle de medidas |EP03|
|FT08| Controle de idas ao veterinário|EP03|

### 4.3 Histórias de usuários
Histórias de usuário é uma descrição curta, informal e em linguagem simples do que um usuário quer fazer dentro de um produto de software para obter algo que ele considere valioso.

As histórias de usuários normalmente seguem o padrão de papel-função-benefício (ou modelo):

>*Como um __tipo de usuário__,
eu quero __uma ação__
para que __um benefício/valor__*

|ID | História de usuário | ID Feature |
|---| ------------------- | ---------- |
|US01| Eu como __usuário__ desejo poder realizar o __cadastro__ para ter acesso a aplicação. |FT01|
|US02|Eu como __usuário__ desejo __alterar__ meus dados para manter o perfil atualizado.  |FT01|
|US03| Eu como __usuário__ desejo __apagar__ meus dados para remover o perfil.| FT01|
|US04|Eu como __usuário__ desejo poder realizar __login__ para acessar a aplicação. |FT02|
|US05| Eu como __usuário__ desejo __resgatar__ a senha para realizar o login.|FT02|
|US06| Eu como __usuário__ desejo poder __cadastrar__ meu(s) pet(s) na aplicação para realizar o controle das informaçoẽs dele(s).|FT03|
|US07| Eu como __usuário__ desejo poder __alterar__ os dados do(s) meu(s) pet(s) para manter o(s) perfil(is) atualizado(s).|FT03|
|US08| Eu como __usuário__ desejo poder __deletar__ o(s) registro(s) do(s) meu(s) pet(s) para remover os dados da aplicação.|FT03|
|US09| Eu com __usuário__ desejo poder __registrar__ os banhos do(s) meu(s) pet(s) para manter o controle.| FT04 |
|US10| Eu como __usuário__ desejo poder __acessar__ o histórico de banho(s) do(s) meu(s) pet(s) para saber quando dar banho novamente.|FT04|
|US11| Eu como __usuário__ desejo __adicionar__ lembrete sobre o(s) banho(s) para não esquecer dele(s). | FT04|
|US12|Eu como __usuário__ desejo __deletar__ o(s) banho(s) do(s) pet(s) para remover a(s) informação(ões). | FT04|
|US13| Eu como __usuário__ desejo __registrar__ um medicamento para realizar o controle dele. |FT05|
|US14| Eu como __usuário__ desejo __adicionar__ um lembrete para não esquecer o horário da administração do medicamento.|FT05|
|US15| Eu como __usuário__ desejo poder __remover__ o medicamento quando finalizar o seu período de administração.|FT05|
|US16| Eu como __usuário__ desejo __registar__ quando o medicamento foi dado para manter o histórico atualizado. |FT05|
|US17| Eu como __usuário__ desejo __adicionar__ um lembrete para não esquecer o horário da administração do medicamento.|FT05|
|US18|Eu como __usuário__ desejo __visualizar__ as vacinas do pet para me informar. |FT06|
|US19| Eu como __usuário__ desejo __registrar__ as vacinas que o pet tomau para manter o dados atualizados. |FT06|
|US20| Eu como __usuário__ desejo __adicionar__ lembre da vacinação para não esquecer a data.|FT06|
|US21| Eu como __usuário__ desejo __apagar__ as vacinas para remover as informações. |FT06|
|US22| Eu como __usuário__ desejo __registrar__ o peso do pet para manter os dados atualizados.|FT07|
|US23|Eu como __usuário__ desejo __registrar__ o tamanho do pet para manter os dados atualizados.|FT07|
|US24| Eu como __usuário__ desejo __visualizar__ um gráfico com o histórico do peso do meu pet para acompanhar sua evolução.|FT07|
|US25|Eu como __usuário__ desejo __visualizar__ um gráfico com o histórico do tamanho do meu pet para acompanhar sua evolução.|FT07|
|US26|Eu como __usuário__ desejo __registrar__ dados sobre as visitas ao __veterinário__ para manter o registro da saúde do pet.|FT08|
|US27|Eu como __usuário__ desejo __visualizar__ histórico de visitas ao veterinário para me manter informado. |FT08|
|US28|Eu como __usuário__ desejo __visualizar__ um relátorio sobre a saúde do pet para ter acesso fácil a isso.|FT08|


## 5. Requisitos não funcionais
Os requisitos não funcionais são aqueles que não interferem diretamente no desenvolvimento do sistema propriamente dito, ou seja, não é um requisito que tem regras de negócios e, portanto, é necessário para determinar o que será feito no software.

|  ID   | Requisito |
| :--:  | :--: |
| RNF01 | A aplicação deve estar disponível em celulares Android |
| RNF02 | A aplicação deve estar disponível em celulares IOS |
| RNF03 | A aplicação deve estar disponível 24/7 |
| RNF04 | A aplicação não deve ocupar muito espaço na memória em disco dos celulares |
| RNF05 | A aplicação deve ser segura |
| RNF06 | A aplicação deve ser gratuita |
| RNF07 | A aplicação deve armazenar apenas informações relevantes dos pets|
| RNF08 | A aplicação deve oferecer uma boa experiência de usuário |
| RNF09 | A aplicação deve ser rápida |
| RNF10 | A aplicação deve ter uma interface agradável e simples |
| RNF11 | A aplicação deve ser confiável em termos de informação |
| RNF12 | Autenticação de usuário|