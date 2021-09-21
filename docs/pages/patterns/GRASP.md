# <center> `GRASP's` utilizados no projeto

### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 19/09/2021 |  0.1   | Escrita da introdução | Hugo Sobral |
| 19/09/2021 |  0.2   | Escrita do Especialista | Hugo Sobral |
| 19/09/2021 |  0.3   | Escrita da Alta Coesão e Baixo Acoplamento | Hugo Sobral |
| 20/09/2021 |  0.4   | Escrita do Controlador | Hugo Sobral |
| 20/09/2021 |  0.5   | Finalização do documento | Hugo Sobral |
| 20/09/2021 |  1.0   | Revisão do Documento | Durval Carvalho |



<div align="justify">

## 1. Introdução

GRASP é um acrônimo para **General Responsability Assignment Software Patterns**, que em tradução livre significa **Padrões de Software para Atribuições Gerais de Responsabilidades**. Para a compreensão dos GRASP's, é primeiro necessário a contextualização da abordagem em mais alto nível, esta chamada de **Responsability-Driven-Development**, ou simplesmente **RDD**, que em tradução livre significa **Projeto Guiado por Responsabilidades**.

Larman define que o **RDD** é uma maneira de pensar em projetos de Orientação a Objetos que inclui a abstração de comportamentos entre os diferentes módulos do sistema. O *RDD* é baseado em duas grandes camadas de abstração, a camada de *conhecer*, relacionada com instâncias e comunicações internas do código, e a camada de *fazer*, relacionada com os comportamentos e métodos implementados pelos diferentes módulos. A partir do **RDD**, tem-se que os GRASP's são um conjunto pragmático de princípios básicos que fornecem um referencial sólido para a programação orientada a objetos. [1]

Desta forma, é válido afirmar que os GRASP's buscam oferecer um guia bem estruturado para soluções de software que se baseiam no paradigma da Orientação a Objetos. Como consequência direta da utilização dos padrões dentro de um projeto de software, tem-se a produção de uma base de código robusta e que apresenta um enorme fator de adaptabilidade diante de novas necessidades de projeto, de negócio ou, simplesmente, futuras mudanças planejadas para o código. Um código que segue as diretrizes propostas pelos GRASP's apresenta uma ótima organização entre os diferentes módulos; uma fácil manutenção e, por fim; uma boa capacidade de compreensão por diferentes desenvolvedores. [2]

Os GRASP são descritos pelos seguintes tópicos:

- GRASP Criador;
- GRASP Especialista;
- GRASP da Alta Coesão;
- GRASP do Baixo Acoplamento;
- GRASP Controlador;
- GRASP do Polimorfismo;
- GRASP da Invenção Pura;
- GRASP da Indireção;
- e, por fim, GRASP de Variações Protegidas.

Neste documento, serão abordados os tópicos **Especialista**; **Controlador** e; **Alta Coesão** e **Baixo Acoplamento**.


## 2. Especialista

### 2.1 Definição

O padrão especialista é um dos princípios mais básicos dentro dos 9 GRASP's existentes. O GRASP especialista abrange as camadas de *conhecer* e *fazer* dentro do escopo do RDD. O Especialista traz à tona a ótica do questionamento de quais são as camadas que devem conhecer umas às outras e quão a direção deste conhecimento [1]. Isto é, uma classe X pode instanciar uma classe Y sem que esta tenha de fato contato com a camada implementada em X.

Este GRASP implica em um caminho pragmático para a decisão da arquitetura do sistema: [3]

- Primeiro deve-se pensar em quais são as informações necessárias para se concluir uma tarefa obrigatória do sistema;
- Após este mapeamento das informações, é preciso avaliar qual é a camada que concentra o maior conhecimento acerca da tarefa em específica;
- Com os módulos agora mapeados e levantados, aquele que possuir o maior conhecimento da tarefa é o forte candidato para especialista.

### 2.2 Utilização

A partir da definição do padrão, vamos analisar o exemplo específico para o **app** de animais dentro da API do Animalesco. A estrutura de arquivos da pasta de animais pode ser visualizada na próxima imagem.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/grasp/animals_folder.png'>
    <figcaption align='center'>
        <b>Figura 1: Estrutura de arquivos da entidade de animais na camada Backend</b>
        <br>
        <small>Autor: Hugo Sobral, 2021.</small>
    </figcaption>
</p>

Como evidenciado na imagem, existem 10 arquivos python no diretório e cada um deles possui uma responsabilidade específica. Estes são

- ```init.py```, responsável por instanciar o módulo python no projeto;
- ```admin_actions.py```, responsável por definir e implementar quais são as possíveis ações que um usuário administrador pode efetuar nas entidades;
- ```admin.py```, responsável por configurar o usuário administrador dentro do dashboard de administração do Django;
- ```apps.py```, responsável por definir as configurações da entidade de animais no projeto;
- ```models.py```, responsável por criar o modelo de dados que armazena as informações de um animal dentro do Animalesco;
- ```permissions.py```, responsável por definir as permissões de acesso relativas a animais;
- ```serializers.py```, responsável por definir como será feita a transformação para transmissão dos dados por meio da API;
- ```tests.py```, responsável pela implementação dos testes;
- ```urls.py```, responsável por mapear os endpoints para cada um dos métodos HTTP disponíveis;
- ```views.py```, responsável por definir quais são os métodos e como os dados são tratados em cada um deles, funcionando como a controller da entidade.

Desta forma, pode-se dizer que cada um dos arquivos dentro de um projeto Django é especialista em uma tarefa específica para a construção de uma API REST.

## 3. Controlador

### 3.1 Definição

O GRASP Controlador propõe que, dentro de um projeto orientado a objetos, um componente específico para lidar com as requisições dos diferentes atores do sistema deve existir[4]. Este padrão indica que, paralelamente à camada de lógica de negócios, UI e processamento de dados, uma camada puramente responsável pelo controle dos eventos gerados pelo sistema deve estar implementada. Desta forma, os arquivos controladores funcionam como pontos que concentram e delegam as atividades para os módulos corretos [3].

### 3.2 Utilização

Dentro do padrão definido pelo **Django Rest Framework**, a camada das controllers está presente em cada um dos **apps** produzidos na API. Isto é, para cada entidade do sistema, existe um arquivo responsável pelo mapeamento das requisições relacionadas com àquela entidade.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/grasp/vaccines_folder.png'>
    <figcaption align='center'>
        <b>Figura 2: Estrutura de arquivos da entidade de vacinas na camada Backend</b>
        <br>
        <small>Autor: Hugo Sobral, 2021.</small>
    </figcaption>
</p>

Na imagem acima, é possível observar a estrutura de arquivos de um **app** no **Django REST**. Vamos a uma análise mais detalhada do arquivo ```views.py```.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/grasp/views_file.png'>
    <figcaption align='center'>
        <b>Figura 3: Arquivo controlador</b>
        <br>
        <small>Autor: Hugo Sobral, 2021.</small>
    </figcaption>
</p>

O arquivo ```views.py``` apresenta a implementação da classe ```VaccineViewSet``` que herda da classe ```ModelViewSet```. Toda a lógica para como os dados devem ser recuperados e como estes devem ser retornados por meio de ```QuerySets``` está definido na classe ```ModelViewSet```. Neste arquivo estão todas as configurações necessárias para determinar a forma com que o framework vai receber, tratar e direcionar as requisições efetuadas.

## 4. Alta Coesão e Baixo Acoplamento

### 4.1 Definição

Para definir o princípio do Baixo Acoplamento, antes é preciso definir em termos palpáveis o que é acoplamento: Larman define o acoplamento como uma métrica para mensurar o quão fortemente conectado se encontra o estado de um código específico, isto é, o quão dependente a camada de *conhecer* está entre os diversos componentes do sistema [1]. A partir disso, o princípio do baixo acoplamento fornece a visão necessária para a decisão da melhor forma de implementação que satisfaça:

- a menor dependência entre as classes;
- menor impacto por mudanças em classes existentes;
- maior potencial de reutilização de código.

A Alta Coesão surge como um princípio avaliativo para ser implementado em conjunto com o princípio do Baixo Acoplamento. A partir da Alta Coesão é possível realizar as medidas necessárias na camada de responsabilidades de cada um dos componentes do sistema, isto é, a partir da diretriz da Alta Coesão é possível determinar se diferentes elementos estão fortemente conectados ou altamente atrelados na camada de *conhecimento*.


### 4.2 Utilização

Ao utilizarmos os padrões já estabelecidos pelo _framework Django REST_, já estamos utilizando as práticas da Alta Coesão e Baixo acoplamento, visto que cada um dos arquivos tem sua própria responsabilidade e seus próprios métodos definidos. Desta forma, a própria ferramenta já proporciona um nível adequado de conexão entre os componentes do código.

## 5. Conclusão

Após todo o conteúdo explicitado neste documento, é possível evidenciar a importância dos padrões de projeto GRASP dentro da construção da base de código do projeto, isto é, é capaz de se identificar quais são as atribuições e responsabilidades de cada um dos componentes presentes no código.

## Bibliografia

- [1] Larman, C. 2005. Applying UML and Patterns – An Introduction to Object-Oriented Analysis and Design and Iterative Development 3rd ed. New Jersey.

- [2] Desenvolvimento com qualidade com GRASP. **DevMedia**. Disponível em <https://www.devmedia.com.br/desenvolvimento-com-qualidade-com-grasp/28704> (Último acesso em 20/09/2021).

- [3] What are General Responsibility Assignment Software Patterns?. **Kapuscik, J.**, **GitConnected**. Disponível em <https://levelup.gitconnected.com/what-are-general-responsibility-assignment-software-patterns-6ad9635a44da>

- [4] Understanding the GRASP Design Patterns. **Koopmans, R.** Disponível em <https://medium.com/@ReganKoopmans/understanding-the-grasp-design-patterns-2cab23c7226e> (Último acesso em 20/09/2021).

- [5] SERRANO, Milene. Arquitetura e Desenho de Software AULA – GRASP – PARTE I. 36 slides <https://aprender3.unb.br/pluginfile.php/897140/mod_label/intro/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GRASP%20BASE%20Parte%20I%20-%20Profa.%20Milene.pdf> (Último acesso em 20/09/2021).

- [6] SERRANO, Milene. Arquitetura e Desenho de Software AULA – GRASP_A - COMPLEMENTAR – PARTE I. 66 slides https://aprender3.unb.br/pluginfile.php/897140/mod_label/intro/Arquitetura%20e%20Desenho%20de%20Software%20-%20Aula%20GRASP_A%20-%20Profa.%20Milene%20-%20Complementar.pdf> (Último acesso em 20/09/2021).

</div>
