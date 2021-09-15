# <center> `Chain of Responsability` e sua utilização no projeto

### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 14/09/2021 |  0.1   | Criação do documento | Durval Carvalho |


<div align="justify">

## 1. Introdução

## 1.1. Definição do padrão

O padrão de projeto `Chain of Responsability`, que em uma tradução livre significa `Cadeia de responsabilidades`, é um padrão comportamental. Padrões comportamentais se preocupam com a atribuição de responsabilidade aos vários objetos que podem compor a solução.

A característica comportamental do padrão `Chain of Responsability` é fornecer um acoplamento fraco entre o emissor da comunicação e os vários candidatos a receptor, possibilitando uma solicitação ser implicitamente tratada, sem o conhecimento dos demais receptores.

A **inteção** do padrão `Chain of Responsability` é evitar o acoplamento entre o remetente e aos vários receptor, possibilitando mais de um objeto a oportunidade de tratar a solicitação, de acordo com o contexto.

O padrão `Chain of Responsability`, quando aplicado no contexto de Backend APIs Web são comumente chamadas de `Middlewares`.

## 1.2. Cenário de uso

Um cenário frequente de uso de `Middlewares` está relacionado com permissão de acesso. É comum que em uma API de um serviço exista recursos com diferentes níveis de permissão, onde cada usuário só pode ver e editar os recursos de sua autoria.

Desse modo, para que seja possível implementar uma lógica de de permissão de acesso, o cliente dessa API deve se autenticar de alguma maneira, seja mandando um [`Access Token Key`](https://auth0.com/docs/security/tokens/access-tokens), [`JSON Web Tokens`](https://auth0.com/docs/security/tokens/json-web-tokens), ou até mesmo por meio de [`Cookie-Based Authentication`](https://auth0.com/docs/users/cookies).

Com tal cenário definido, uma potencial solução seria utilizar uma função ou método de autentificação, onde seria os dados de autenticação são usados para descobrir quem é o usuário. Essa função teria que ser utilizada em todas controllers do projeto.

Expandindo mais o nosso cenário. O serviço dispobilizado via API se tornou um sucesso e atingiu a marca de milhões de requisições por dia, e a camada de rede de aplicação começou a se tornar um gargalo, devido aos vários dados trafegados. Desse modo, a equipe de engenheiros definiu que a API deveria comprimir as respostas antes de enviá-las, para assim reduzir a quantidade de bytes trafegados.

Com o novo requisito, todas as controllers agora precisam utilizar a função de compressão antes de finalizar a o processamento da requisição, sendo necessário alterar todo as controllers existentes.

Expandindo mais o nosso cenário. A nossa API se tornou um verdadeiro sucesso, e agora existem usuários maliciosos interagindo com a nossa API. Um de nossos engenheiros detectou que nossos endpoints estão sofrendo ataques de força bruta, onde milhares de tokens, cookies e chaves de acesso são tentados aleatoriamente. Desse modo, o nosso especialista em segurança propós a utilização de uma lógica de `[Rate Limiting](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/)` e `[IP Restriction](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-resource-policy-access/`, onde os recursos possuem uma margem de acesso por usuário (por exemplo 5 requisições por segundo) e IPs que estiverem frequentemente ultrapassando os limites são bloqueados.

Dessa forma, com os novos requisitos, é novamente necessário alterar todos as controllers do projeto para assim utilizar as funções disponibilizadas pelo engenheiro de segurança.

Caso essa abordagem continue sendo utilizada, com a evolução do projeto, logo todas as controllers vão está com mais lógicas externa do que interna, o que dificulta a compreensão das lógicas de negócios da controllers e futuras manutenções.

A outra abordagem que pode ser utilizada é remover toda a lógica externa das controllers e utilizar o padrão `Chain of Responsability` na camada anterior as controolers.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/chain-of-responsability/camadas.png'>
    <figcaption align='center'>
        <b>Figura 1: Diagrama ilustrando a interação entre a camada de controllers e a camada Chain of Responsability</b>
        <br>
        <small>Autor: Durval Carvalho, 2021.</small>
    </figcaption>
</p>

Dessa forma, a camada, aqui chamada de `Chain of Responsability`, nada mais é do que várias funções encadeadas, que irá processar as requisições e as respostas que entram e saem da camada de controllers. As requisições podem ser barradas antes de chegar nas `controllers` caso falhe uma lógica de autenticação por exemplo, e também pode injetar novos dados na requisição, como o ID do usuário que foi autenticado. Da mesma maneira, as respostas que saem da camada de `controllers` podem ser processadas, onde uma pontencial compressão de dados seria realizada, antes de enviar para o autor da requisição.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/chain-of-responsability/internal-chain.png'>
    <figcaption align='center'>
        <b>Figura 2: Diagrama ilustrando a interação entre aos vários componentes da camada Chain of Responsability</b>
        <br>
        <small>Autor: Durval Carvalho, 2021.</small>
    </figcaption>
</p>

Um exemplo real de um middleare para um projeto que utiliza o [framework Django](https://www.djangoproject.com/) é o código abaixo:

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/chain-of-responsability/middleware_example.png'>
    <figcaption align='center'>
        <b>Figura 3: Exemplo de um Middleware em um projeto Django</b>
        <br>
        <small>Autor: Durval Carvalho, 2021.</small>
    </figcaption>
</p>

Como pode ser visto, os `Middlewares` de projetos djangos herdam da classe `MiddlwareMixin`. Um programador `Django` somente precisa definir o código `core` do `Middleware`, ou seja, as funções `process_request` e `process_response`.

Após a implementação do Middleware, cabe ao programador `Django` registar o novo middleware no `settings` do projeto, especificando uma posição na "cadeia de responsabilidade" (`Chain of Responsability`).

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/chain-of-responsability/middleware_settings.png'>
    <figcaption align='center'>
        <b>Figura 4: Registro de um Middleware em um projeto Django</b>
        <br>
        <small>Autor: Durval Carvalho, 2021.</small>
    </figcaption>
</p>

Como pode ser visto, as classes `Middlewares` do `Django` não são acopladas uma as outras, ou seja, não possuem nenhum tipo de referência crusada. Desse modo, para que exista uma corrente de responsabilidade o `Framework Django` utiliza uma classe chamada `BaseHandler`, responsável por aplicar os `Middlewares` na requisição que acabou de chegar nos servidor, e assim que a resposta for criada pela `controller`, reaplicar os `Middlewares`, mas agora na ordem inversa, na resposta.

Desse modo, uma diagramação do padrão de projeto `Chain of Responsability` utilizado pelo `Django` poderia ser descrito da seguinte maneira:

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/chain-of-responsability/django-uml-chain-of-responsability.jpg'>
    <figcaption align='center'>
        <b>Figura 5: Diagrama UML simplificado do padrão `Chain of Responsability` implementado pelo Django</b>
        <br>
        <small>Autor: Durval Carvalho, 2021.</small>
    </figcaption>
</p>

Como pode ser visto no diagrama acima, todos os `Middlewares` da aplicação herdam da classe `MiddlewareMixin`, que por sua vez fazem parte da composição da classe `BaseHandler`, sendo essa a classe interna do Django responsável por aplicar os `Middlewares` na ordem definida na lista definida do arquivo `settings.py`.

## 2. Utilização no projeto

Conforme foi explicado no tópico anterior, o Django possui um mecanismo robusto para a utilização de `Middlewares`, cabendo aos programadores Django somente implementar as subsclasses de `MiddlewareMixin` e registrar no módulo `settings.py`.

Dessa forma, a estrutura do projeto para utilização de Middlewares irá funcionar da seguinte maneira:

1. Cada app do projeto que tem a necessidade de criar um middleware deverá criar um arquivo `middlewares.py` e implementar o `Middleware` herdando da classe `MiddlewareMixin`.

2. Após a implementação, o `Middleware` criado deverá ser registrado no arquivo `settings.py` do projeto.


<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/chain-of-responsability/django-middleware-packages.jpg'>
    <figcaption align='center'>
        <b>Figura 6: Diagrama de pacotes simplificado ilustrando os principais componentes utilizados na `Chain of Responsability` do Django</b>
        <br>
        <small>Autor: Durval Carvalho, 2021.</small>
    </figcaption>
</p>

## 3. Conclusão

Conforme foi explicado nesse documento, o padrão de projeto `Chain of Responsability`, quando aplicado no contexto de APIs Web são comumente chamados de `Middlewares`, é um padrão bastante poderoso, que possibilita a utilização de um código menos acoplado, mais robusto e consequentemente de melhor manutenção.

Uma vez que o nosso projeto utiliza o Framework de desenvolvimento Django, é seguido o padrão já definido da ferramenta, para a criação e utilização de `Middlewares`.

As pesquisas e os diagramas feitos nesse documento terá a serventia de apresentar o padrão, explicar suas premissas básicas e apresentar o modo de utilização com a ferramenta Django.

Dessa forma, é possível concluir que a elaboração desse documento irá agregar valor ao nosso projeto.

## Bibliografia

- [1] Refactoring Guru, Chain of Responsibility. Disponível em: https://refactoring.guru/pt-br/design-patterns/chain-of-responsibility (Último acesso em 14/09/2021).

- [2] Source Making, Chain of Responsibility. Disponível em: https://sourcemaking.com/design_patterns/chain_of_responsibility (Último acesso em 14/09/2021).

- [3] Erich Gamma ... [et al.]. Padrões de projeto - Soluções reutilizáveis de software
orientado a objetos. Tradução Luiz A. Meirelles Salgado. Bookman, 2007.

- [4] Django Project, Middleware. Disponível em: https://docs.djangoproject.com/en/3.2/topics/http/middleware/ (Último acesso em 15/09/2021).

</div>
