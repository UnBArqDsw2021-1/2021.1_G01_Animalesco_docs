# <center> Backlog do produto

## Histórico de versão

| Data | Versão | Descrição | Autor |
|------|--------|-----------|-------|
| 04/08/2021 | 0.1 | Estrutura inicial do documento | Rafael Leão e João Vitor Farias |
| 05/08/2021 | 0.2 | Revisão do documento | Hugo Sobral |
| 05/08/2021 | 0.3 | Reestruturação do backlog | Hugo Sobral |
| 05/08/2021 | 1.0 | Revisão do documento e inclusão da bibliografia | Hugo Sobral |
| 05/08/2021 | 1.1 | Revisão do documento | Leonardo Gomes |
| 22/08/2021 | 1.2 | Refatoração da introdução | Hugo Sobral e Leonardo Gomes |
| 22/08/2021 | 1.3 | Adição do tema e das tasks no backlog | Hugo Sobral e Leonardo Gomes |
| 22/08/2021 | 1.4 | Refatoração de histórias de usuário | Hugo Sobral e Leonardo Gomes |
| 23/08/2021 | 2.0 | Revisão final do documento | Durval Carvalho |

## 1. Introdução
O _backlog do produto_, tradução livre de _product backlog_, é um artefato descrito pela metodologia SCRUM que consiste em uma lista de tarefas que descrevem as funcionalidades e comportamentos que são esperados do produto quando este alcança a conjuntura de conclusão. O _backlog do produto_ se organiza de maneira a separar as atividades por diferentes granularidades, sendo elas:
- _Theme_ (Temas);
- _Epics_ (Épicos);
- _Features_ (Funcionalidade);
- _User stories_ (História de usuários);
- _Tasks_ (Tarefas).

Os _Themes_, também denotados como _Investment Themes_, são a granularidade mais alta de um backlog. Os _themes_ estabelecem a relação direta entre o investimento; de esforço, financeiro ou de recursos; e os objetivos do projeto. Isto é, os _themes_ ficam responsáveis por guiar a visão dos _epics_, das _features_ e do restante da granularidade do produto. Em linhas gerais, os _themes_ descrevem a visão do produto, estes representam os princípios que agregam valor à aplicação.

Os _epics_ são as estruturas mais complexas a termos de granularidade de um backlog. Os _epics_ abrigam um conjunto de _features_.

As _features_, por sua vez, descrevem um conjunto de funcionalidades e requisitos não funcionam para o projeto. Uma _feature_ agrupa um conjunto de _user stories_. Ao se realizar uma analogia à termos computacionais, temos que as _features_ são quase como componentes de um módulo; para este caso fictício, os módulos seriam definidos como os _epics_; que podem ser divididos em estruturas atômicas.

Já as _user stories_ definem pedaços atômicos de funcionalidades. São as _user stories_ que guiam a delegação de tarefas para as sprints do projeto (o conceito de sprints e o processo de delegação de tarefas foi descrito no [documento de metodologia](pages/metodologia-do-projeto.md)).

As _tasks_ são a granularidade de mais baixo nível de um backlog. Estas descrevem, a partir de um aspecto mais detalhado, o mapeamento de todas as atividades envolvidas em uma determinada user story, isto é, as _tasks_ funcionam como uma checklist para guiar o estado de conclusão de uma user story.


## 2. Metodologia

A partir das técnicas de elicitação realizadas pela equipe, foi possível realizar o mapeamento dos requisitos funcionais e não funcionais do projeto. Os insumos levantados pelas técnicas de [brainstorming](/pages/brainstorming.md), [questionário](/pages/questionario.md) e [entrevistas](/pages/entrevistas.md) foram a base para a identificação das necessidades do Animalesco como solução computacional.

Desta forma, foram realizados encontros em equipe para a identificação destes requisitos e devida tradução para o formato do _backlog do produto_, isto é, a escrita das necessidades do projeto de acordo com a granularização descrita pelo artefato de backlog.

## 3. Objetivo

Este documento tem como objetivo a identificação e devido agrupamento dos requisitos do Animalesco. Este documento apresenta, por meio de tabelas, as estruturas atômicas de tarefas relacionadas a cada um dos temas identificados anteriormente pelas técnicas de elicitação utilizadas pela equipe.

## 4. Requisitos funcionais

Os requisitos funcionais foram descritos por meio de uma tabela que os classifica em _epics_, features e user stories.

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
    <td class="backlog" style="width: 10px; text-align: center; font-weight: bold; height: 43px;">Theme</td class="backlog">
    <td class="backlog" style="width: 10px;  text-align: center; font-weight: bold; height: 43px;">Epics</td class="backlog">
    <td class="backlog" style="width: 10px;  text-align: center; font-weight: bold; height: 43px;">Features</td class="backlog">
    <td class="backlog" style="width: 475px;  text-align: center; font-weight: bold; height: 43px;">User stories</td class="backlog">
    <td class="backlog" style="width: 475px;  text-align: center; font-weight: bold; height: 43px;">Tasks</td class="backlog">
</tr>

<!-- Epic usuário -->
<!-- Feature perfil -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 10px; height: 100%; text-align: center; writing-mode: vertical-lr;" rowspan="87">Cuidados gerais para com pets</td class="backlog">
    <td class="backlog" style="width: 10px; height: 138px; text-align: center; writing-mode: vertical-lr;" rowspan="20">Usuário</td class="backlog">
    <td class="backlog" style="width: 10px; height: 69px; text-align: center; writing-mode: vertical-lr;" rowspan="20">Perfil</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo poder <b>realizar cadastro</b> para ter <b>acesso a aplicação</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar model de usuário.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para registro de novos usuários.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de cadastro.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição POST para usuário.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo <b>alterar meus dados</b> para <b>manter o perfil atualizado</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para atualização de usuários.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de perfil.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de atualização de dados do usuário.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição PUT para usuário.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo <b>realizar login</b> para <b>ter acesso ao app</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint de autenticação de usuário.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de login.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar da service de requisição POST para login.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Armazenar de maneira local o token de autenticação do usuário .</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo <b>apagar meus dados</b> para <b>remover o perfil</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar confirmação de deleção.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para excluir usuários e todos dados relacionados a sua conta.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Adicionar icone de deleção no perfil.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição DELETE para usuários.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo <b>resgatar minha senha</b> para <b>recuperar o login</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Definir biblioteca de envio de email para recuperação.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Consumir biblioteca de envio de email para recuperação.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar service de requisição para envio  de email para recuperação de senha.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de edição de senha.</td class="backlog">
</tr>

<!-- Epic pet -->
<!-- Feature cadastro -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 10px; height: 460px; text-align: center; writing-mode: vertical-lr;" rowspan="67">Pet</td class="backlog">
    <td class="backlog" style="width: 10px; height: 253px; text-align: center; writing-mode: vertical-lr;" rowspan="12">Cadastro</td class="backlog">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo poder <b>cadastrar meu(s) pet(s)</b> na aplicação para <b>realizar o controle das informaçoẽs dele(s)</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar model de pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para registro de novos pets.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de cadastro de pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição POST para pets.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo poder <b>alterar os dados do(s) meu(s) pet(s)</b> para <b>manter o(s) perfil(is) atualizado(s)</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para atualização de pets.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de perfil de pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de atualização de dados do pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição PUT para pets.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo poder <b>deletar o(s) registro(s) do(s) meu(s) pet(s)</b> para <b>removê-lo(s) do app</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilização de endpoint para deleção pets e todos os dados relacionados a este pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Adicionar icone de deleção no perfil de pets.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar confirmação de deleção.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição DELETE para pets.</td class="backlog">
</tr>

<!-- Feature banho -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 10px; height: 253px; text-align: center; writing-mode: vertical-lr;" rowspan="13">Banho</td class="backlog">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu com <b>usuário</b> desejo poder <b>registrar os banhos do(s) meu(s) pet(s)</b> para <b>manter o controle</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar model de banho.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para registro de novos banhos a determinado pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar visualização de cadastro de banho.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição POST para banho.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="3">Eu como <b>usuário</b> desejo poder <b>acessar o histórico de banho(s) do(s) meu(s) pet(s)</b> para <b>saber quando dar banho novamente</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para recuperar os banhos de um determinado pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição GET para banho.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar visualização do histórico de banho.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="2">Eu como <b>usuário</b> desejo <b>adicionar lembrete sobre o(s) banho(s)</b> para <b>não esquecer dele(s)</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Utilizar dos lembretes nativos do celular do usuário.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar notificação de lembrete de banho.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo <b>deletar o(s) banho(s) do(s) pet(s)</b> para <b>remover a(s) informação(ões)</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para deleção de banhos.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição DELETE para banho.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Adicionar icone de deleção de banho.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar confirmação de deleção.</td class="backlog">
</tr>


<!-- Feature medicaentos -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 10px; height: 253px; text-align: center; writing-mode: vertical-lr;" rowspan="21">Medicamentos</td class="backlog">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo <b>registrar um medicamento</b> para <b>realizar o controle dele</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar model de medicamento.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para registro de novos medicamentos a determinado pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de cadastro de medicamentos.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição POST para medicamento.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo <b>registrar quando o medicamento</b> foi dado para <b>manter o histórico atualizado</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar model de registro de dose de medicação que relacione pet e medicamento.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para registro de novas doses.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de registro de dose.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de POST para dose.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="2">Eu como <b>usuário</b> desejo <b>adicionar um lembrete</b> para <b>não esquecer o horário da administração do medicamento</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Utilizar dos lembretes nativos do celular do usuário.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar notificação de lembrete de dose de medicação dentro do prazo de tratamento.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo poder <b>remover o medicamento</b> para <b>remover as informações</b>. </td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para deleção de medicamentos.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição DELETE para banho.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Adicionar ícone de deleção de medicamento.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar confirmação de deleção.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo poder <b>remover uma dose de medicação registrada</b> para <b>manter o controle da saúde do meu pet atualizado</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para deleção de doses.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição DELETE para dose.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Adicionar ícone de deleção de dose registrada.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar confirmação de deleção.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="3">Eu como <b>usuário</b> desejo poder <b>acessar o histórico de medicações do meu pet</b> para <b>realizar o acompanhamento para com a saúde do meu pet</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para recuperar as doses de um determinado pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição GET para doses de medicação.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar visualização do histórico de medicação.</td class="backlog">
</tr>

<!-- Feature vacinação -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 10px; height: 253px; text-align: center; writing-mode: vertical-lr;" rowspan="11">Carteira de vacina</td class="backlog">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo <b>registrar as vacinas que o pet tomou</b> para <b>manter o dados atualizados.</b></td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar model de vacina.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para registro de vacinas de um determinado pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de registro de vacina.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição POST para vacina.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="3">Eu como <b>usuário</b> desejo <b>visualizar as vacinas do meu pet</b> para <b>realizar o acompanhamento da imunização dele</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para recuperar as vacinas de um determinado pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição GET para vacinas.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar visualização da carteira de vacinação digital.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo <b>apagar as vacinas</b> para <b>remover as informações</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para deleção de vacinas.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição DELETE para vacina.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Adicionar ícone de deleção de vacina registrada.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar confirmação de deleção.</td class="backlog">
</tr>


<!-- Feature veterinária -->
<tr style="height: 23px;">
    <td class="backlog" style="width: 10px; height: 253px; text-align: center; writing-mode: vertical-lr;" rowspan="9">Idas a veterinárias</td class="backlog">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="4">Eu como <b>usuário</b> desejo <b>registrar dados sobre as visitas</b> ao veterinário para <b>manter o registro da saúde do pet</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar model de consulta veterinária.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para registro de consultas de um determinado pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar página de registro de consulta.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição POST para consultas.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="3">Eu como <b>usuário</b> desejo <b>visualizar histórico de visitas</b> ao veterinário para me <b>manter informado</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Disponibilizar endpoint para recuperar as consultas de um determinado pet.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Implementar service de requisição GET para consultas.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar visualização do histórico de consultas.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px;; height: 23px;" rowspan="2">Eu como <b>usuário</b> desejo <b>agendar notificações de retorno</b> a veterinária para que eu possa <b>ser lembrado da futura visita</b>.</td class="backlog">
    <td class="backlog" style="width: 475px; height: 23px;" >Utilizar dos lembretes nativos do celular do usuário.</td class="backlog">
</tr>
<tr style="height: 23px;">
    <td class="backlog" style="width: 475px; height: 23px;" >Criar notificação de lembrete de próxima consulta veterinária a partir da data inserida.</td class="backlog">
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
| RNF12 | A aplicação deve realizar autenticação de usuário |


### Bibliografia

1. Como fazer o Product Backlog. **Project Builder**, 2017. Disponível em: https://www.projectbuilder.com.br/blog/como-fazer-o-product-backlog/ (último acesso em 05/08/2021)
2. VENTURA, Plínio. Epic, Feature e User Story (Épico, Funcionalidade e História de Usuário). **Até o Momento**, 2021. Disponível em https://www.ateomomento.com.br/epic-feature-e-user-story/ (último acesso em 05/08/2021)
3. SCRUM, Metodologia Ágil. Disponível em: https://pt.wikipedia.org/wiki/Scrum_(desenvolvimento_de_software)#Product_Backlog (Último acesso em 05/08/2021)
4. Backlog do Produto. **Stock**. Disponível em: https://unbarqdsw.github.io/2020.1_G12_Stock/#/Modeling/Backlog (Último acesso em 05/08/2021)
5. LEFFINGWELL, D. _Agile Software Requirements_: Lean Requirements Practices for Teams, Programs, and the Enterprise. Addison-Wesley Professional, 2011.
6. Product Backlog V3. **Requisitos Habitica**. Disponível em: https://requisitos-habitica.netlify.app/BacklogV3 (Último acesso em 05/08/2021)