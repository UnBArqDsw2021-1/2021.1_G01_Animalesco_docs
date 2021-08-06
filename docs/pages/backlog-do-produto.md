# Backlog do produto

## Histórico de versão

| Data | Versão | Descrição | Autor |
|------|--------|-----------|-------|
| 04/08/2021 | 0.1 | Estrutura inicial do documento | Rafael Leão e João Vitor Farias |
| 05/08/2021 | 0.2 | Revisão do documento | Hugo Sobral |
| 05/08/2021 | 0.3 | Reestruturação do backlog | Hugo Sobral |

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

<style>
tr {
    background-color: white;
}
.markdown-section td.backlog {
    border: 3px solid #EBEBEB;
}


table, td.backlog{
  border-collapse: collapse;
  background-color: white;
}
</style>

<table style="width: 933px; background-color:white">
<tbody>
<!-- Cabeçalho -->
<tr style="height: 43px; background-color:white">
    <td class="backlog" style="width: 35px; height: 43px;">Epics</td class="backlog">
    <td class="backlog" style="width: 35px; height: 43px;">Features</td class="backlog">
    <td class="backlog" style="width: 475px; height: 43px;">User stories</td class="backlog">
</tr>

<!-- Epic usuário -->
<!-- Feature perfil -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 35px; height: 138px;" rowspan="5">Usuário</td class="backlog">
    <td class="backlog" style="width: 35px; height: 69px; " rowspan="5">Perfil</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;">Eu como <b>usuário</b> desejo poder <b>realizar cadastro</b> para ter <b>acesso a aplicação</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>apagar meus dados</b> para <b>remover o perfil</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>alterar meus dados</b> para <b>manter o perfil atualizado</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>realizar login</b> para <b>ter acesso ao app</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>resgatar minha senha</b> para <b>recuperar o login</b>.</td class="backlog">
</tr>

<!-- Epic pet -->
<!-- Feature cadastro -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 35px; height: 460px; " rowspan="42">Pet</td class="backlog">
    <td class="backlog" style="width: 35px; height: 253px; " rowspan="3">Cadastro</td class="backlog">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo poder <b>cadastrar meu(s) pet(s)</b> na aplicação para <b>realizar o controle das informaçoẽs dele(s)</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo poder <b>alterar os dados do(s) meu(s) pet(s)</b> para <b>manter o(s) perfil(is) atualizado(s)</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo poder <b>deletar o(s) registro(s) do(s) meu(s) pet(s)</b> para <b>removê-lo(s) do app.</b></td class="backlog">
</tr>

<!-- Feature banho -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 35px; height: 253px; " rowspan="4">Banho</td class="backlog">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu com <b>usuário</b> desejo poder <b>registrar os banhos do(s) meu(s) pet(s)</b> para <b>manter o controle</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo poder <b>acessar o histórico de banho(s) do(s) meu(s) pet(s)</b> para <b>saber quando dar banho novamente.</b></td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>adicionar lembrete sobre o(s) banho(s)</b> para <b>não esquecer dele(s)</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>deletar o(s) banho(s) do(s) pet(s)</b> para <b>remover a(s) informação(ões)</b>.</td class="backlog">
</tr>


<!-- Feature medicaentos -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 35px; height: 253px; " rowspan="4">Medicamentos</td class="backlog">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>registrar um medicamento</b> para <b>realizar o controle dele</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo adicionar um lembrete</b> para <b>não esquecer o horário da administração do medicamento</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo poder <b>remover o medicamento</b> quando finalizar o seu período de administração para <b>manter o controle da saúde do meu pet atualizado</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>registar quando o medicamento foi dado</b> para <b>manter o histórico atualizado.</b></td class="backlog">
</tr>

<!-- Feature vacinação -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 35px; height: 253px; " rowspan="3">Carteira de vacina</td class="backlog">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>visualizar as vacinas do pet</b> para <b>me informar.</b></td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>registrar as vacinas que o pet tomou</b> para <b>manter o dados atualizados.</b></td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>apagar as vacinas</b> para <b>remover as informações</b>.</td class="backlog">
</tr>


<!-- Feature veterinária -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 35px; height: 253px; " rowspan="3">Idas a veterinárias</td class="backlog">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>registrar dados sobre as visitas</b> ao veterinário para <b>manter o registro da saúde do pet</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>visualizar histórico de visitas</b> ao veterinário para me <b>manter informado</b>.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;">Eu como <b>usuário</b> desejo <b>agendar notificações de retorno</b> a veterinária para que eu possa <b>ser lembrado da futura visita</b>.</td class="backlog">
</tr>
</tbody>
</table>


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
| RNF12 | A aplicação deve realizar autenticação de usuário|


### Bibliografia