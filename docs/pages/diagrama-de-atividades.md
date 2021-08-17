# <center> Diagrama de Atividades

### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 16/08/2021 |  0.1   | Confecção inicial do documento | Hugo Sobral |
| 16/08/2021 |  0.2   | Inclusão do diagrama de cadastro de pets | Hugo Sobral |
| 16/08/2021 |  0.3   | Inclusão do diagrama de cadastro de usuários | Hugo Sobral |
| 16/08/2021 |  0.4   | Inclusão do diagrama de banhos de pets | Hugo Sobral |
| 16/08/2021 |  0.5   | Inclusão do diagrama de medicação de pets | Hugo Sobral |
| 16/08/2021 |  0.6   | Inclusão do diagrama de cartão de vacinação de pets | Hugo Sobral |
| 16/08/2021 |  1.0   | Escrita da metodologia, desenvolvimento de cada um dos diagramas e escrita da conclusão | Hugo Sobral |

<div align="justify">

## 1. Introdução

A UML (***Unified Modeling Language***, **Linguagem de Modelagem Unificada** em tradução livre) é uma notação gráfica para modelagem de contextos de software que atende ao paradigma de Orientação a Objetos. Dentro dos diagramas descritos pela notação, destacam-se as descrições de detalhamento dos contextos estrutuais (também chamados de estáticos); comportamentais (também chamados de dinâmicos); organizacionais (diagrama que se responsabilida por descrever os pacotes da solução computacional); e os anotacionais (também chamados de explicativos).

Dentro da gama dos diagramas dinâmicos, destaca-se o **Diagrama de Atividades**. O **Diagrama de Atividades** se responsabiliza por descrever um fluxo de atividades que representam a utilização da solução computacional em um determinado contexto. Isto é, o Diagrama de Atividades descreve o caminho seguido a partir de uma determinada ação, com foco nos procedimentos, regras de negócio e fluxo de trabalho. Tal descrição pode se utilizar de elementos gráficos da notação UML para descrever condições, ações e estados.

## 2. Metodologia

Para a confecção do diagrama de atividades, fez-se necessário a modularização da utilização da aplicação em diversos contextos para que, desta forma, cada fluxo de atividades pudesse ser melhor descrito e para que cada diagrama pudesse ser analisado de maneira independente.

Os fluxos idealizados foram:
- Cadastro de usuário
- Cadastro de pets
- Banhos do pet
- Controle de medicações do pet
- Cartão de vacinação digital do pet
- Visitas ao consultório veterinário

Vale ressaltar que cada diagrama foi divido em 3 instâncias, estas são as camadas do usuário; do *frontend* e do *backend*. Cada camada representa a instância de determinada ação, isto é, em qual nível comportamental uma determinada ação acontece na aplicação. A camada do usuário descreve todas as atividades desempenhadas a nível da pessoa que utiliza o Animalesco. Por sua vez, a camada do *frontend* engloba todas as atividades desempenhadas pela solução computacional que está em contato direto com o usuário. Por fim, a camada do *backend* representa todas as atividades que estão descritas nas regras de negócio e lógicas de processamento da aplicação.

## 3. Diagrama de Atividades

### 3.1 Cadastro de usuário

O fluxo de cadastro de usuário descreve o caminho percorrido pelo usuário ao executar a tarefa de registro de nova conta na aplicação.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/diagrama_de_atividades/cadastro_de_usuario-atividades.png'>
    <figcaption align='center'>
        <b>Figura 1: Diagrama de atividades - cadastro de usuário</b>
        <br>
        <small>Autor: Hugo Sobral.</small>
    </figcaption>
</p>

### 3.2 Cadastro de pets

O fluxo de cadastro de pets descreve o caminho percorrido pelo usuário, este já deve estar devidamente cadastrado na aplicação, ao executar a tarefa de registrar um pet na aplicação. Vale ressaltar que um usuário pode registrar diversos pets.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/diagrama_de_atividades/cadastro_de_pet-atividades.png'>
    <figcaption align='center'>
        <b>Figura 2: Diagrama de atividades - cadastro de pet</b>
        <br>
        <small>Autor: Hugo Sobral.</small>
    </figcaption>
</p>

### 3.3 Banhos do pet

O fluxo de banhos do pet descreve o caminho percorrido pelo usuário ao executar a tarefa de registrar um banho de um determinado pet, este já deve estar cadastrado e vinculado ao usuário na aplicação.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/diagrama_de_atividades/banhos-atividades.png'>
    <figcaption align='center'>
        <b>Figura 3: Diagrama de atividades - banhos do pet</b>
        <br>
        <small>Autor: Hugo Sobral.</small>
    </figcaption>
</p>

### 3.4 Controle de medicações do pet

O diagrama de controle de medicações do pet descreve o fluxo de atividades que é percorrido através da utilização do aplicativo para o controle das medicações que um determinado pet precisa tomar. Nota-se que, no diagrama, existe mais de uma possibilidade para a chegada no fim do fluxo, visto que nem sempre a funcionalidade de iniciar um novo tratamento será utilizada e, para estes casos, apenas a visualização do histórico de medicações engloba as atividades percorridas pelo software.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/diagrama_de_atividades/controle_medicacao-atividades.png'>
    <figcaption align='center'>
        <b>Figura 4: Diagrama de atividades - controle de medicação do pet</b>
        <br>
        <small>Autor: Hugo Sobral.</small>
    </figcaption>
</p>

### 3.5 Cartão de vacinação digital do pet

O diagrama do cartão de vacinação descreve o fluxo de atividades percorrido pelo software ao executar tarefas relacionadas com o registro e controle de doses de vacinas de um determinado pet. 

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/diagrama_de_atividades/cartao_vacinacao-atividades.png'>
    <figcaption align='center'>
        <b>Figura 5: Diagrama de atividades - cartão de vacinação digital do pet</b>
        <br>
        <small>Autor: Hugo Sobral.</small>
    </figcaption>
</p>

### 3.6 Visitas ao consultório veterinário

O diagrama de visitas ao consultório veterinário descreve o fluxo de atividades percorrido pelo usuário ao executar a tarefa de registrar uma nova consulta veterinária de um determinado pet.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/diagrama_de_atividades/consultas_vet-atividades.png'>
    <figcaption align='center'>
        <b>Figura 6: Diagrama de atividades - visitas ao consultório veterinário</b>
        <br>
        <small>Autor: Hugo Sobral.</small>
    </figcaption>
</p>

## 4. Conclusão

Ao se realizar o estudo e confecção dos diagramas de atividades relacionadas ao projeto animalesco, foi-se capaz de criar insumos relevantes para a melhor compreensão do Animalesco a níveis comportamentais. Estes insumos servem de base não apenas para o alinhamento da equipe para com o projeto de software, mas também para a devida melhoria incremental da modelagem do [**Backlog**](pages/backlog-do-produto.md) e para a confecção da modelagem por meio dos diagramas de caso de uso.

## Bibliografia

1. Activity Diagrams. **UML Diagrams**. Disponível em: https://www.uml-diagrams.org/activity-diagrams.html (Último acesso em 16/08/2021)

2. SERRANO, Milene. Arquitetura e Desenho de Software AULA - MODELAGEM UML ESTÁTICA. 55 slides. Disponível em:  https://aprender3.unb.br/pluginfile.php/897132/mod_label/intro/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20Modelagem%20UML%20Est%C3%A1tica%20-%20Profa.%20Milene.pdf (Último acesso em 16/08/2021)

3. SERRANO, Milene. Arquitetura e Desenho de Software AULA - MODELAGEM UML DINÂMICA. 28 slides. Disponível em: https://aprender3.unb.br/pluginfile.php/897133/mod_label/intro/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20Modelagem%20UML%20Din%C3%A2mica%20-%20Profa.%20Milene.pdf (Último acesso em 16/08/2021)

4. "O que é diagrama de atividades UML?". **Lucidchart**. https://www.lucidchart.com/pages/pt/o-que-e-diagrama-de-atividades-uml (Último acesso em 16/08/2021)

5. Diagrama de atividade. **Wikipédia**. Disponível em: https://pt.wikipedia.org/wiki/Diagrama_de_atividade (Último acesso em 16/08/2021)

</div>