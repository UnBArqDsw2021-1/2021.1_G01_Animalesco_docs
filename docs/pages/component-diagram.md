# <center> Diagrama de Componentes

### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 12/08/2021 |  0.1   | Estudo do Diagrama de Componente | Durval Carvalho |
| 12/08/2021 |  0.2   | Análise de quais seriam os principais componentes do sistema | Durval Carvalho |
| 13/08/2021 |  0.3   | Escrita do tópico de introdução | Durval Carvalho |
| 13/08/2021 |  0.4   | Criação do diagrama | Durval Carvalho |
| 13/08/2021 |  0.5   | Validação de alguns pontos do diagrama com a professora | Durval Carvalho |
| 13/08/2021 |  0.6   | Evolução do diagrama com as melhorias citadas pela professora | Durval Carvalho |
| 13/08/2021 |  0.7   | Criação da v1.0 do diagrama de componentes | Durval Carvalho |
| 13/08/2021 |  0.8   | Escrita do tópico de Introdução e Metodologia | Durval Carvalho |
| 13/08/2021 |  1.0   | Escrita do tópico de Conclusão | Durval Carvalho |
| 16/08/2021 |  1.1   | Revisão do Documento | Leonardo Gomes |
<!-- TODO: Melhor detalhar os  -->

<div align="justify">

## 1. Introdução

Durante a execução de um projeto se software, é raro pular diretamente dos requisitos de um sistema para suas classes e funções. Na grande maioria das vezes, é proveitoso analisar o sistema como um todo para definir quais são os componentes de mais alto nível. E com base na visão de alto nível do sistema, é possível estabelecer uma arquitetura que atenda ao projeto. Além disso, essa prática de análise permite a compreensão antecipada de quais serão as dependências entre os vários subsistemas e submódulos do projeto. Desse modo, o projetista será capaz de definir os principais componentes de alto nível que serão gerenciáveis, reutilizáveis e trocáveis, uma vez que o fluxo de troca de informação já está bem definido. [1]

O diagrama UML de componente apresenta uma metodologia e uma sintaxe de modelagem que permite uma análise dos componentes de alto nível do sistema. De acordo com o Russ Miles e Kim Hamilton, em seu livro Learning UML 2.0, um componente é uma parte do sistema que é encapsulada, reutilizável e substituível. É possível compreender os componentes como "blocos de lego", onde cada bloco possui um determinado encaixe que vários outros blocos podem "se encaixar". Quando vários blocos "estão encaixados" entre si esse conjunto de bloco pode ser compreendido como um bloco maior. [1]

Essa abordagem modular, onde o sistema é visto como um conjunto de blocos trabalhando juntos, possibilita o desenvolvimento com menor acoplamento, o que por sua vez facilita na manutenção e na reutilização de blocos em contextos diferentes. [1]

## 2. Metodologia

Para a diagramação do diagrama de componentes do projeto animalesco, foi necessário tomar algumas decisões.

A primeira grande decisão tomada na diagramação foi a de aumentar o nível de detalhamento das componentes que lidam com regras de negócio.

A segunda  grande decisão foi a de diminuir o nível de detalhamento de algumas partes do diagrama e a de aumentar o nível de detalhamento das partes que envolve regras de negócios. Essa decisão foi tomada pois as partes que lidão com regras de negócios tem maior probabilidade de sofrer mudanças e logo devem ser melhor compreendidas. Dessa forma, pode ser visto que o maior detalhamento está no no grande componente de backend.

Outra decisão tomada foi a de não representar as conexões triviais, para assim evitar a poluição do diagrama. A primeira classe de conexões "escondidas" foi as conexões com o componente de persistência (todos os componentes se comunicam com os bancos de dados). A segunda classe de conexões "escondida" foi a comunicação com o componente de roteamento. O componente de roteamento é responsável por mapear a comunicação do frontend com um módulo ou funcionalidade específica. Desse modo, tal componente está conectado com todos os demais componentes, e a representação de tais conexões iria diminuir a compreensibilidade do diagrama.

Outra decisão do diagrama foi a de utilizar _tags_ para representar alguns módulos do sistema. As principais _tags_ utilizadas e seus respectivo significados foram:
* «sistema» - Representa um sistema em execução um hardware independente (servidor ou smartphone)
* «subsistema» - Representa um sistema em execução um servidor compartilhado com outros sistemas (servidor ou smartphone)
* «módulo» - Representa os módulos que pode existir dentro de um componente

Outra notação utilizada na diagrama foi a utilização de "núvens" para representar alternativas. A maioria as núvens estão relacionadas a serviços. Por exemplo, o componente que lida com o envio de emails possui núvens ao seu redor com as alternativas de serviços que podem realizar a integração com o módulo.


## 3. Diagrama de Componentes

O diagrama construído pode ser acessado através da [plataforma Draw.IO](https://app.diagrams.net/). Basta fazer o download do arquivo do diagrama e carregá-lo da plataforma. O arquivo do diagrama está disponível no seguinte link: https://github.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/tree/main/docs/assets/pages/component-diagram

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/component-diagram/diagrama-de-componentes.jpg'>

    <figcaption align='center'>
        <b>Figura 1: Imagem do diagrama de componentes</b>
        <br>
        <small>Fonte: Durval Carvalho</small>
    </figcaption>
</p>

## 3.1. Explicação dos principais componentes

Nesse tópico será explicado resumidamente as principais funcionalidades de cada componente e suas principais conexões com os demais componentes e serviços.

### 3.1.1. Componente de exportação

Esse é o componente responsável por obter dados dos demais componentes e gerar um relatório que será enviado por email.

Como pode ser visto no diagrama, esse serviço utiliza a interface de vários componentes do sistema para obter as informações do relatório e por fim utiliza o componente de envio de emails para finalizar o envio do relatório.


### 3.1.2. Componente de Autorização e Autentificação

Esse é o componente responsável por controlar quem acessar e o que acessa na API do backend. Neste componente irá agrupar toda a lógica de controle de acesso através do uso de _middlewares_.

Como pode ser visualizado no diagrama, toda a comunicação passa por esse componente.

### 3.1.3. Componente de roteamento

Esse é o componente responsável por conectar todos os componentes internos do backend com as requisições do frontend. Neste componente será mapeado as requisições (_endpoint_ das apis) com as várias controladoras que utilizam os demais componentes.

Esse é um componente chave que possui conexões com todos os demais componentes, porém, visando não diminuir a compreensibilidade do diagrama, tais conexões não foram ilustradas.

### 3.1.4. Componente de alertas e notificações

Esse é o componente responsável por emitir notificações para o frontend. Assim, esse componente irá grupar toda a lógica de comunicação com o aplicativo ou com a sessão web. Além de agrupar as várias potenciais integrações com serviços de notificações que podem ser contratados.

### 3.1.5. Componente de tarefas periódicas

Esse é o principal componente do sistema. As principais funcionalidades que mais agregam valor ao nosso produto estão contidas nesse componente. Dessa forma, os demais componentes desse sistema utilizam ou dão suporte as funcionalidades desse componente (emissão de emails, emissão de notificações e emissão de relatórios).

Por ser um componente de extrema importância, esse é o único componente que detalha seus módulos internos, para assim facilitar a compreensão do diagrama.

## 5. Conclusão

Após todo o processo de estudo, análise e diagramação, foi adquirido uma maior compreensão do sistema e de como suas partes se comunicam.

Uma vez com o diagrama de componentes definido, a probabilidade do desenvolvimento de um produto altamente modularizado e testável aumenta, tendo impacto direto na qualidade da solução como um todo.

## Bibliografia

- [1] Miles, R; Hamilton, K. Learning UML 2.0 - A Pragmatic Introdution to UML. Publicado em Abril de 2006, ISBN-10: 0-596-00982-8, ISBN-13: 978-0-59-600982-3

- [2] Component Diagram Tutorial. Disponível em: https://online.visual-paradigm.com/diagrams/tutorials/component-diagram-tutorial/. Acesso em: 13 de agosto de 2021.

- [3] Mobile Application Component Diagram. Disponível em: https://www.conceptdraw.com/examples/mobile-application-component-diagram. Acesso em: 13 de agosto de 2021.

</div>
