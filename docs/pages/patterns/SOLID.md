# <center> Princípios `S.O.L.I.D.`

### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 20/09/2021 |  0.1   | Escrita do documento | Hugo Sobral |
| 20/09/2021 |  1.0   | Revisão do Documento | Durval Carvalho |


<div align="justify">

## 1. Introdução

SOLID, termo definido por Robert C. Martin, é um acrônimo para os 5 princípios que regem o desenvolvimento e o projeto de sistemas computacionais orientados a objetos [3]. Tais diretrizes estabelecem boas práticas que, quando seguidas e implementadas de maneira correta, geram como consequência direta a produção de um sistema computacional robusto e que apresenta uma boa manutenibilidade a medida em que o projeto cresce.

Os 5 princípios SOLID são:

- **S**: Single-Responsibility Principle, em tradução livre **Princípio da Responsabilidade-Única**;
- **O**: Open-closed Principle, em tradução livre **Princípio Aberto-fechado**;
- **L**: Liskov Substituition Principle, em tradução livre **Princípio da Substituição de Liskov**;
- **I**: Interface Segregation Principle, em tradução livre **Princípio da Segregação de Interfaces**;
- **D**: Dependency Inversion Principle, em tradução livre **Princípio da Inversão de Dependências**.

Este documento se propõe a fornecer uma breve introdução e contextualização acerca de cada um dos princípios e, a partir das definições estabelecidas, traçar a utilização destes durante o desenvolvimento do código do projeto Animalesco.


## 2. Princípio da Responsabilidade-Única

O Princípio da Responsabilidade-Única surge a partir do pressuposto:

> Uma classe deve apenas ter uma, e somente uma, razão para ser modificada, o que implica que a classe deve ter apenas uma tarefa. [1]

Se uma classe tem muitas responsabilidades, esta aumente exponencialmente a possibilidade de inserção de *bugs* no código, visto que, ao alterar qualquer uma das responsabilidades da classe existe a chance de alterar o funcionamento de outra tarefa devido ao alto acoplamento.

Este princípio tem como objetivo separar os comportamentos a partir de responsabilidades específicas, para que a identificação e tratativa de comportamentos inesperados possa ser realizada de uma maneira mais objetiva e coesa. [2]


## 3. Princípio Aberto-fechado

O Princípio Aberto-fechado surge a partir do pressuposto:

> Objetos ou entidades devem estar abertos à extensão mas não à modificação. [2]

Caso surja a necessidade de se incluir mais funcionalidades, métodos ou comportamentos em uma classe já existente, a abordagem ideal é incluir novas funções para a realização destes comportamentos e não modificar as já existentes.

Este princípio tem como objetivo realizar extensões de uma classe pai, sem que esta tenha seus comportamentos alterados, em métodos declarados dentro do escopo de classes filhas. Desta forma, é possível evitar a injeção de bugs no projeto, já que os módulos que já fazem uso da classe pai não irão enxergar diferenças. [2]

## 4. Princípio da Substituição de Liskov

O Princípio da Substituição de Liskov surge a partir do pressuposto.

> Suponha que q(X) seja uma propriedade comprovada para objetos de X e que são tipadas como T. Logo, q(Y) deve ser uma propriedade que também seja comprovada para objetos de Y e que são tipadas como S, neste caso S é um substituto para T. [1]

Quando uma classe filha não performa os mesmos comportamentos da classe pai, tem-se um forte indício de um código com presença de *bugs*. Isto é, uma classe filha não deve ter seu escopo de responsabilidade fortemente alterado, a partir da perspectiva da classe pai. É esperado que componentes derivados de uma classe apresentem somente extensões de comportamentos, e não comportamentos diferentes.

Este princípio tem como objetivo reforçar a consistência do código por meio da garantia de classes pai e filhas podem ser usadas no mesmo contexto sem que estas injetem erros na execução do código. [2]


## 5. Princípio da Segregação de Interfaces

O princípio da Segregação de Interfaces surge a partir do pressuposto:

> Um módulo que consume uma interface nunca deve ser obrigado a implementar ou depender de métodos que este não usa. [1]

Quando uma classe é forçada a performar ações e comportamentos que não são úteis para o seu contexto específico, todo o processo de codificação das camadas que não são utilizadas é caracterizado com um baixo valor ao projeto e, ademais, este pode ser o responsável pela inserção de *bugs* no código. Uma módulo deve apenas apresentar métodos que são necessários para o cumprimento dos requisitos da camada. [2]

Este princípio tem como objetivo separar uma série de ações em blocos menores para que, desta forma, as classes do projeto possam executar somente as tarefas necessárias para o contexto individual destas.


## 6. Princípio da Inversão de Dependências

O Princípio da Inversão de Dependências surge a partir do pressuposto:

> Entidades devem depender de abstrações, não de conceitos concretos. Isto é, a camada de alto-nível de especificação do projeto não deve depender dos módulos e conceitos de baixo-nível, e sim de abstrações acerca das funcionalidades. [1]

Este princípio afirma que uma classe não deve ser acoplada conceitualmente com as ferramentas necessárias para a sua implementação. A abordagem ideal é que esta esteja ligada com interfaces que são capazes de realizar a comunicação entre a camada de alto e baixo nível. Desta forma, nem a classe e nem a interface devem conhecer a implementação da camada de baixo-nível, entretanto, a camada de baixo-nível deve conhecer a interface para que esta possa realizar as implementações de acordo com a comunicação esperada. [2]

Este princípio tem como objetivo reduzir as dependências das camadas de alto nível de abstração do código.


## 7. Utilização dos princípios SOLID

Dentro da camada de BackEnd do projeto, existe uma série de padrões e formatações de códigos adotadas que evidenciam a utilização dos princípios ```S.O.L.I.D.``` no contexto da codificação do Animalesco.

A primeira camada de exemplo evidenciada, o Princípio Aberto-fechado que pode ser visto no arquivo [```admin_actions.py```](https://github.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_BackEnd/blob/7a867adc46330703bdaf42d41493b65e8e197430/src/animals/admin_actions.py#L3). Neste arquivo são definidas funções extras à classe de ```Admin```, definida no arquivo [```admin.py```](https://github.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_BackEnd/blob/main/src/animals/admin.py), para o gerenciamento de entidades dentro do contexto de animais no projeto.

Já o Princípio da Responsabilidade-Única pode ser evidenciado por meio da estrutura de arquivos de cada um dos **apps** dentro do contexto do **Django REST framework**. Por padrão, tem-se 10 arquivos por entidade que apresentam um, e somente um, propósito, estes são:

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

O Princípio da Segregação de Interfaces pode ser evidenciado por meio das sobrescritas efetuadas dentro do arquivo de [```views.py```](https://github.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_BackEnd/blob/main/src/animals/views.py) no contexto de animais. Ao se analisar os trechos de código:

```python
def perform_create(self, serializer):
    specie = get_object_or_404(Specie, pk=self.kwargs["specie_pk"])
    serializer.save(specie=specie)
```

e

```python
def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
```

podemos observar a implementação e modificação de métodos, já disponibilizados pelas classes pai do próprio *framework*, que seriam utilizados de maneira específica e necessitavam de um comportamento específico devido à dependência destes métodos. Este mesmo exemplo também serve como evidência da utilização do Princípio da Substituição de Liskov.

## 8. Conclusão

A partir do apresentado neste documento, é possível traçar a importância de uma arquitetura limpa para uma implementação de código que seja de fácil manutenção e simples evolução. Os princípios SOLID apresentam um valor imensurável para o alinhamento da equipe e para a produção de códigos limpos.


## Bibliografia

- [1] SOLID: The First 5 Principles of Object Oriented Design. **Digital Ocean**. Disponível em <https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design> (Último acesso em 20/09/2021)

- [2] The S.O.L.I.D Principles in Pictures. Thelma U. **backticks & tildes**. Disponível em <https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898> (Último acesso em 20/09/2021)

- [3] Martin, R. C. 2017. Clean Architecture: A Craftsman's Guide to Software Structure and Design
</div>
