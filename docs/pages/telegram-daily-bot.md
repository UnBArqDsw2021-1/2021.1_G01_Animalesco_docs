# <center> Configuração da Daily de Bots

#### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 16/08/2021 |  0.1   | Pesquisa das ferramentas de automatização | Durval Carvalho |
| 16/08/2021 |  0.2   | Definição do uso da plataforma IFTTT | Durval Carvalho |
| 17/08/2021 |  0.3   | Configuração do Applet escolhido | Durval Carvalho |
| 17/08/2021 |  0.4   | Teste se a configuração funcionou no horário correto | Durval Carvalho |
| 18/07/2021 |  1.0   | Criação do documento de relatório | Durval Carvalho |


<div align="justify">

### 1. Introdução

Em uma organização que adote abordagens ágeis em seus processos é comum a prática de pequenas reuniões, para que assim seja feito um acompanhamento das atividades realizadas.

No livro SCUM, A arte de fazer o dobro do trabalho na metade do tempo, Jeff Sutherland, denominam essas pequenas reuniões como `Dailies`. Além das reuniões diárias, os autores definem um conjunto de 4 regras que tais reuniões devem atender, sendo elas:

* As reuniões não devem durar mais de 15 minutos.
* Todos os membros da equipe devem participar
* A reunião deve ser feita em pé, para gerar um desconforto que incentiva a curta duração da reunião.
* Cada membro presente na reunião deve responder 3 perguntas, sendo delas:
    * O que fiz ontem para ajudar a equipe a concluir a sprint?
    * O que vou fazer hoje para ajudar a equipe a concluir a sprint?
    * Quais dificuldades estou enfrentando no momento?


### 2. Adaptação das dailies para o nosso contexto

Devido ao fato do projeto está sendo desenvolvido sem o encontro presencial dos membros do projeto, devido a pandemia de SARS-CoV-2 no Brasil, essa dinâmica de dailies foi adaptada para o nosso contexto.

A dinâmica de reunião síncrona e presencial foi adaptada para ser um dinâmica assíncrona e remota. Para isso foi criado um canal de comunicação do Telegram, onde os membros deviam preencher um boilerplate de mensagem no seguinte formato:

```
<NOME DA PESSOA>

O que eu fiz: <TEXTO DESCRITIVO>

O que eu pretendo fazer: <TEXTO DESCRITIVO>

Impedimentos: <TEXTO DESCRITIVO>
```

Dessa forma, todos os dias, geralmente às 12pm o líder do grupo (Hugo Sobral) notifica o grupo que a dinâmica da Daily iria começar.

Nas primeiras semanas essa dinâmica funcionou muito bem, porém devido a esquecimentos coletivos o canal de comunicação caiu em desuso chegando ao ponto de ninguém enviar o relatório de Daily durante uma semana inteira. O que impactou na tarefas coletivas, gerando retrabalho.


### 2. Solução encontrada

Para solucionar o problema dos membros não lembrarem da dinâmica de Daily, foi proposto e configurado um bot para enviar mensagens de lembrete todos os dias úteis às 12pm.

Para isso foi escolhido a plataforma [IFTTT](https://ifttt.com/), sigla essa que significa `If This Then That`. Essa é uma plataforma de automatização que possui várias integrações com várias ferramentas que a comunidade desenvolveu e disponibilizou para uso público.

Nessa plataforma, foi escolhido a rotina existente chamada `Automatically post a daily reminder to a Telegram chat` ([link](https://ifttt.com/applets/SBbs278z-automatically-post-a-daily-reminder-to-a-telegram-chat)). Essa rotina foi configurada para a seguinte mensagem de segunda à sexta no canal criado para as dailies:

```
It's 12 AM, and you all know what this means. Daily time!! 🕺💃🕺💃
```

### 3. Resultados obtidos

Após a configuração do bot de lembrete das dailies o grupo se mostrou engajado novamente na dinâmica de daily. Todos os membros voltaram a participar diariamente, e assim se espera que o comunicação diária consiga antecipar potenciais problemas que possam surgir.


<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/telegram-daily-bot/daily-bot-telegram.png'>
    <figcaption align='center'>
        <b>Figura 1: Captura de tela do bot notificando a daily e os membros respondendo ao chamado.</b>
        <br>
        <small>Autor: Durval Carvalho.</small>
    </figcaption>
</p>


### Bibliografia

1. Sutherland, J. A arte de fazer o dobro do trabalho na metade do tempo.

2. Site do IFTTT. Disponível em: https://ifttt.com/

3. Applet "Automatically post a daily reminder to a Telegram chat". Disponível em: https://ifttt.com/applets/SBbs278z-automatically-post-a-daily-reminder-to-a-telegram-chat

</div>