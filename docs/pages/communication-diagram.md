# <center> Diagrama de Comunicação

### Histórico de Versão

|    Data    | Versão |      Descrição       |     Autor(es)     |
| :--------: | :----: | :------------------: | :---------------: |
| 14/08/2021 |  0.1   | Estudo do Diagrama de Comunicação | Leonardo Gomes |
| 15/08/2021 |  0.2   | Análise dos objetos a serem utilizados | Leonardo Gomes |
| 15/08/2021 |  0.3   | Criação do diagrama de comunicação da criação do pet | Leonardo Gomes |
| 15/08/2021 |  0.4   | Criação do diagrama de comunicação do calendário do pet | Leonardo Gomes |
| 16/08/2021 |  0.5   | Criação do documento | Leonardo Gomes |
| 16/08/2021 |  0.6   | Adição da Bibliografia | Leonardo Gomes |
| 16/08/2021 |  0.7   | Escrita do tópico Introdução | Leonardo Gomes |
| 16/08/2021 |  0.8   | Escrita do tópico Metodologia | Leonardo Gomes |
| 16/08/2021 |  1.0   | Escrita da conclusão e adição dos diagramas | Leonardo Gomes |
| 13/10/2021 |  1.1   | Ajuste no diagrama de comunicação relacionado ao calendário | Leonardo Gomes |

<div align="justify">

## 1. Introdução

O **diagrama de comunicação**, também conhecido como **diagrama de colaboração**, é um diagrama dinâmico que mostra a interação entre os objetos usando setas e mensagens. Esse é um diagrama de sequência simples sem mecanismo de estrutura, utiliza interações e fragmentos combinados para sua composição. [3]

O objetivo desse diagrama é capturar o comportamento de um determinado cenário, mostrando os objetos e mensagens trocadas entre eles e enfatiza a ordem estrutural das mensagens. [1] O diagrama, além de mostrar a troca de mensagens entre os objetos, demonstra os seus relacionamentos. Esse diagrama tem muita semelhança com o diagrama de sequência, já que ambos mostram a interação entre os objetos, entretanto esse tem como enfasê o contexto do sistema, enquanto o de sequẽncia se caracteriza enfatiza o decorrer do tempo. [2]

## 2. Metodologia

Em relação a diagramação do diagrama de comunicação, foi feitas algumas decisões, que foi levada em consideração o diagrama de sequẽncia.

A principal decisão foi os nomes das mensagens e objetos utilizados, sendo eles espelhos de alguns objetos que estão no diagrama de sequẽncia, já que ambos são diagramas de objeto, onde os objetos são mostrados juntamente com seus relacionamentos.

Para a criação do diagrama deve ser ter conhecimento de três conceitos fundamentais: **frame**, **lifeline**, **message**.

### 2.1. Frame

É uma borda retangular que delimita e nomeia o diagrama. O nome deve ficar na parte superior direita do diagrama.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/communication-diagram/frame.png'>
    <figcaption align='center'>
        <b>Figura 1: Representação de um frame</b>
        <br>
        <small>Disponível em: https://www.uml-diagrams.org/communication-diagrams.html#sequence-expression</small>
    </figcaption>
</p>


### 2.2 Lifeline

Lifeline é a especificação do nome do elemento que representa um participante na interação, nesse sentido é importante citar que o lifeline representa **apena uma** entidade.


<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/communication-diagram/lifeline.png'>
    <figcaption align='center'>
        <b>Figura 2: Representação de um lifeline</b>
        <br>
        <small>Disponível em: https://www.uml-diagrams.org/communication-diagrams.html#sequence-expression</small>
    </figcaption>
</p>

### 2.3 Message

Message é representado como uma linha no diagrama de comunicação, possui uma seta na parte superior da linha com uma [expressão de sequẽncia](https://www.uml-diagrams.org/communication-diagrams.html#sequence-expression). A seta indica a direção da comunicação.


<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/communication-diagram/message.png'>
    <figcaption align='center'>
        <b>Figura 3: Representação de uma message</b>
        <br>
        <small>Disponível em: https://www.uml-diagrams.org/communication-diagrams.html#sequence-expression</small>
    </figcaption>
</p>

## 3. Diagramas de comunicação

Para a criação desse diagrama foi utilizado [Lucid](https://lucid.app/).

### 3.1 Diagrama versão 2
#### Criação do pet

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/communication-diagram/createPet.png'>
    <figcaption align='center'>
        <b>Figura 4: Diagrama de comunicação da criação do pet</b>
        <br>
        <small>Autor: Leonardo Gomes</small>
    </figcaption>
</p>

#### Calendário do pet

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/communication-diagram/pet-V2.png'>
    <figcaption align='center'>
        <b>Figura 5: Diagrama de comunicação do calendário do pet, versão 2</b>
        <br>
        <small>Autor: Leonardo Gomes</small>
    </figcaption>
</p>


### 3.2 Diagrama versão 1
#### Criação do pet

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/communication-diagram/createPet.png'>
    <figcaption align='center'>
        <b>Figura 5: Diagrama de comunicação da criação do pet</b>
        <br>
        <small>Autor: Leonardo Gomes</small>
    </figcaption>
</p>

#### Calendário do pet

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/communication-diagram/pet.png'>
    <figcaption align='center'>
        <b>Figura 6: Diagrama de comunicação do calendário do pet</b>
        <br>
        <small>Autor: Leonardo Gomes</small>
    </figcaption>
</p>

## 4. Conclusão

Nesse documento podemos ter uma sintese do contexto do sistema sinalizando os principais objetos e sua comunicação.

Com os dois diagramas dinâmicos cirados conseguimos poderemos ter uma maior facilidade e alinhamento em relação ao desenvolvimento, ou seja, tendo impacto diretamente na qualidade do produto.

## Bibliografia

- [1]. ENGENHARIA DE SOFTWARE Prof. Ricardo Rodrigues Barcelar MODELAGEM DE SISTEMAS ORIENTADA A OBJETOS COM UML. Disponível em: https://docplayer.com.br/7303694-Engenharia-de-software-prof-ricardo-rodrigues-barcelar-http-www-ricardobarcelar-com-br.html. (Último acesso em 15/08/2021)
- [2]. Linguagem de Modelagem Unificada Em Português. Disponível em: http://www.etelg.com.br/paginaete/downloads/informatica/apostila_uml.pdf (Último acesso em 15/08/2021)
- [3]. Activity Diagrams. Disponível em: https://www.uml-diagrams.org/communication-diagrams.html. (Último acesso em 15/08/2021)
- [4]. Diagrama de comunicação. **Stock App**. Disponível em: https://unbarqdsw.github.io/2020.1_G12_Stock/#/Modeling/Diagrams/Comunicacao?id=diagramas-vers%c3%a3o-2. (Último acesso em: 15/08/2021)

<div>
