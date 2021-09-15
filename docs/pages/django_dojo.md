# <center> DOJO de Django

### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 13/09/2021 |  0.1   | Criação do documento | Durval Carvalho |
| 15/09/2021 |  0.2   | Reformulação do documento | Hugo Sobral |
| 15/09/2021 |  1.0   | Revisão do documento | Hugo Sobral |


<div align="justify">

## 1. Introdução

O cenário que fez necessária a criação de um treinamento específico para a tecnologia [Django REST](https://www.django-rest-framework.org/), um *framework* *python* para a criação de API's REST, iniciou com a troca de tecnologia *BackEnd* do projeto. Uma vez tomada a decisão de troca, de *Node.JS* para *Django REST*, o time mapeou a imprescimbilidade da confecção de um material de treinamento para que os membros da equipe menos familiarizados com a tecnologia pudessem alcançar um nível adequado de autonomia para a execução das tarefas.

Desta forma, o integrante da equipe que apresentava o maior domínio com a ferramenta, o Durval Carvalho, se propôs a criar um tutorial guia para exemplificar os primeiros passos com a tecnologia. Tomou-se o cuidado para escolher um cenário real de desenvolvimento para a criação do material, isto é, para que o tutorial fosse de real utilidade, é necessário que um cenário palpável de desenvolvimento fosse utilizado.  

## 2. Metodologia

Para o vídeo de exemplo, o fluxo de desenvolvimento do item do backlog de autenticação de usuário foi gravado e comentado, de acordo com o formato *Live Coding*, definido por Wang C. e Cook P. como a utilização do ato de programar em si como um mecanismo de expressão e comunicação [3]. A autenticação de usuário esta descrita nas issues [#109](https://github.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/issues/109) e [#107](https://github.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/issues/107) do [repositório de documentação](https://github.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs) do projeto no github.

Uma vez que uma das grandes dificuldades do grupo é a de encontrar um horário em que todos os membros estejam disponíveis para reuniões, foi definido que o DOJO fosse realizado de maneira assíncrona, e que o "instrutor" do DOJO estivesse disponível para responder dúvidas e para fornecer auxílio durante as primeiras sprints de desenvolvimento de código.

A partir deste cenário, foram levantados os seguintes tópicos que foram abordados na execução do DOJO:

* Explicar a estrutura de um projeto Django e seus principais módulos.
* Criar um modelo para a entidade Animals.
* Criar e aplicar as migrações dos modelos para o banco de dados.
* Explicar a utilização do ORM do Django.
* Criar um painel administrativo para os modelos criados.
* Definir e criar um serializador de JSON para os modelos criados.
* Criar uma ViewSets (controllers do django) para os modelos criados.
* Criar um roteador (os endpoints do django) para as ViewSets criadas.
* Mostrar a utilização da API criada.

Com isto, foram criados 2 vídeos: um para explicar o framework de desenvolvimento web, *Django*; e outro para desenvolver o cenário do DOJO.

## 3. Resultados

#### 3.1. Explicação da estrutura de diretórios do Django
<p align='center'>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/JpjeA3HYdBY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

#### 3.2. DOJO de Django Rest Framework
<p align='center'>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RKfpL83BjOI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

## 4. Conclusão

A utilização do Django REST Framework vem se mostrando uma boa escolha, devido a alta dinamicidade e produtividade que a ferramenta foi capaz de prover à equipe. Além disso, a disponibilização dos vídeos e a disponibilidade do membro instrutor aos demais integrantes do projeto se mostrou uma boa combinação, visto que a equipe de desenvolvimento BackEnd apresentou um bom andamento das tarefas desde que o framework foi adotada como tecnologia de desenvolvimento.

## Bibliografia

- [1] Django: The web framework for perfectionists with deadlines. Disponível em: https://www.djangoproject.com/. Acesso em: 13 de setembro de 2021.

- [2] Django REST framework is a powerful and flexible toolkit for building Web APIs. Disponível em: https://www.django-rest-framework.org/. Acesso em: 13 de setembro de 2021.

- [3] Wang G. & Cook P. (2004) "On-the-fly Programming: Using Code as an Expressive Musical Instrument"

</div>
