# <center> Diagrama de Implementação

### Histórico de Versão

|    Data    | Versão |      Descrição       |     Autor(es)     |
| :--------: | :----: | :------------------: | :---------------: |
| 18/08/2021 |  0.1   | Criação do documento | Vinícius Oliveira |
| 18/08/2021 |  0.2   | Introdução e Objetivo| Vinícius Oliveira |
| 19/08/2021 |  0.3   | Inclusão do diagrama | Vinícius Oliveira |
| 20/08/2021 |  0.4   | Melhoria do tópico de introdução | Durval Carvalho |
| 20/08/2021 |  1.0   | Melhoria do tópico de Objetivo | Durval Carvalho |
| 13/10/2021 |  1.1   | Ajuste no diagrama de acordo com as anotações da professora | Leonardo Gomes |

<div align="justify">

## 1. Introdução

Um diagrama de implantação (_deployment diagram_) representa a topologia física do sistema e, opcionalmente, os componentes que são executados nessa topologia. É possível afirmar que esse diagrama apresenta o mapeamento entre os componentes de software e hardware utilizados pelo sistema. [4]

Por meio desse diagrama é possível retratar as unidades de tecnologias presentes no sistema, especialmente hardware, sendo os processadores e armazenamento de massa as unidades mais comum representadas. O diagrama de implantação também é capaz de modelar como o software será distribuído pelas unidades de tecnologias escolhidas, a partir de sobreposição de componentes de softwares e suas interconexões no diagrama. [4]

Os dois elementos base desse diagrama de implantação são os nós e as conexões. Os nós são unidades físicas que simbolizam uma recurso computacional e normalmente possui uma memória e uma capacidade de processamento. Exemplos de nós são: Processadores, Dispositivos de rede, Sensores, Roteadores, dentre outros. [4]

Os nós estão ligados uns ao outros através de conexões. As conexões representam os mecanismos de comunicação entre os nós, podendo ser meios físicos (cabo coaxial, fibras óticas e outros) ou protocolos de comunicação (TCP/IP, HTTP, HTTPS, e outros). [3]

Graficamente, os nós são representados por cubos. Geralmente o nome e o tipo de nó são definidos no interior do cubo. Já as conexões são representadas como retas que ligam dois cubos. Geralmente a descrição da conexão fica centralizada logo acima do meio da reta. [3]

O diagrama de implementação é uma diagrama descrito pela notação UML (Unified Modeling Language). A função deste diagrama é identificar os servidores como nós do diagrama e a rede que relaciona os nós. O diagrama descreve a implementação física de informações geradas pelo programa de software em componentes de hardware  [1].

## 2. Objetivo

Uma vez que a aplicação que será desenvolvida envolve vários sistemas de software independentes (sistemas gerenciadores de bancos de dados, sistemas de envio de emails, sistemas mobile, dentre outros), e são tais sistemas utilizam plataformas de hardware dedicadas, é importante compreender as características dessas plataformas, assim como o modo que a comunicação será feita.

Desse modo, foi escolhido a elaboração de um diagrama de implementação que irá ajudar compreender o modo como todas esses componentes interagem entre si, compondo a aplicação.

## 3. Diagrama de Implementação

O diagrama foi desenvolvido de acordo com a proposta do grupo Animalesco.

### Diagrama versão 2

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/diagrama-implementacao/diagrama-implementacao-v2.png'>
    <figcaption align='center'>
        <b>Figura 1: Diagrama de implementação, segunda versão</b>
        <br>
        <small>Autor: Leonardo da Silva Gomes, 2021.</small>
    </figcaption>
</p>

### Diagrama versão 1

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/diagrama-implementacao/diagrama-implementacao.png'>
    <figcaption align='center'>
        <b>Figura 2: Diagrama de implementação</b>
        <br>
        <small>Autor: Vinícius Rodrigues Oliveira, 2021.</small>
    </figcaption>
</p>

## 4. Bibliografia

- [1] O que é um diagrama de implementação? **Lucidchat**. Disponível em: https://www.lucidchart.com/pages/pt/o-que-e-diagrama-de-implementacao-uml (último acesso em 18/08/2021)

- [2] Diagramas de Implementação. **IMB**. Disponível em: https://www.ibm.com/docs/pt-br/rsas/7.5.0?topic=topologies-deployment-diagrams (último acesso em 18/08/2021)

- [3] Page, J. M. Fundamentos do Desenho Orientado a Objeto com UML. ISBN: 1243-9;

- [4] Bezerra, E. Princípios de Análise e Projeto de Sistemas com UML. ISBN: 8535-2;

<div>
