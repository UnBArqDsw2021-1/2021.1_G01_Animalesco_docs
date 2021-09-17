# <center> `Chain of Responsability` e sua utilização no projeto

### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 14/09/2021 |  0.1   | Criação do documento | Durval Carvalho |
| 17/09/2021 |  0.2   | Adição de elementos no texto | Hugo Sobral |
| 17/09/2021 |  1.0   | Revisão do documento | Hugo Sobral |


<div align="justify">

## 1. Introdução

## 1.1. Definição do padrão

O padrão de projeto `Chain of Responsability`, que em tradução livre significa `Cadeia de Responsabilidades`, é um padrão de projeto comportamental com foco na designação correta para uma sequência de tratativas. Padrões comportamentais se preocupam com a atribuição de responsabilidade aos vários objetos que podem compor a solução.

A característica comportamental do padrão `Chain of Responsability`, também chamado de `CoR`, é fornecer um acoplamento fraco entre o emissor da comunicação e os vários candidatos a receptor. A abordagem do `CoR` permite que a solução apresente um fluxo de tratamentos implicito, isto é, os vários receptores da comunicação não apresentam uma forte conexão ou acoplamento, visto que estes não necessariamente vão conhecer a implementação individual de cada um.

A intenção do padrão `Chain of Responsability` é evitar o acoplamento entre o remetente e os diversos receptores, de modo que várias componentes possam receber e tratar a solicitação de acordo com o contexto do envio.

Quando a aplicabilidade do padrão em contextos de API's REST está em pauta, os `Middlewares` surgem como opção comumente utilizada para a implementação dos receptores descritos anteriormente no documento. Para o contexto do `Django REST`, é possível definir diversos `Middlewares` e a devida sequência para tratativas que devem ser realizadas em cada requisição efetuada.

## 1.2. Cenário de uso

Um cenário frequente de uso de `Middlewares` está relacionado com a permissão de acesso, isto é, é comum que, em uma API de um serviço, existam recursos com diferentes níveis de permissão. Desta forma é possível definir que cada usuário somente pode acessar e editar recursos de sua autoria.

Deste modo, para que seja possível implementar uma lógica de de permissão de acesso, o cliente da API deve realizar a autenticação nas requisições de alguma maneira. Como API's REST não armazenam estados, é preciso que a autenticação seja realizada nas próprias requisições. As abordagens mais comuns para solucionar esta questão são: o envio de um [`Access Token Key`](https://auth0.com/docs/security/tokens/access-tokens); o envio de [`JSON Web Tokens`](https://auth0.com/docs/security/tokens/json-web-tokens); ou até mesmo realizar a autenticação por meio da [`Cookie-Based Authentication`](https://auth0.com/docs/users/cookies).

Com tal cenário definido, uma potencial solução seria utilizar uma função ou método de autenticação que faça uso dos dados enviados para a determinação de quem é o usuário que está realizando a comunicação com o servidor. Essa função, inevitavelmente, tem que estar presente em todas as controllers do projeto, tendo em vista que o padrão arquitetural adotado para o BackEnd foi o MVC (com adaptações na camada de View que se torna ViewSet).

Com o propósito de exemplificação, imagine que um cenário expandido do contexto da API do Animalesco: o serviço se tornou um sucesso e atingiu a marca de milhões de requisições por dia. Partindo deste pressuposto, tem-se que a camada de rede de aplicação começou a se tornar um gargalo devido à enorme quantidade de dados trafegados. Desta forma, a equipe de engenheiros definiu que a API deverá comprimir as respostas antes de enviá-las, para que desta forma a quantidade de bytes trafegados seja menor.

Com o novo requisito mapeado, todas as controllers agora precisam fazer uso da função de compressão antes de finalizar o processamento da requisição. Isto implica que todas as controllers existentes devem passar por modificações.

Expandindo ainda mais o nosso cenário: o aplicativo se tornou um verdadeiro sucesso, e agora existem usuários maliciosos interagindo com a API. Um de nossos engenheiros detectou que nossos endpoints estão sofrendo ataques de força bruta, isto é, milhares de tokens, cookies e chaves de acesso são enviados aleatoriamente. Deste modo, o nosso especialista em segurança propôs a utilização de uma lógica de [`Rate Limiting`](https://www.cloudflare.com/learning/bots/what-is-rate-limiting/) e [`IP Restriction`](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-resource-policy-access/), onde os recursos possuem uma margem de acesso por usuário (por exemplo 5 requisições por segundo) e IPs que estiverem frequentemente ultrapassando os limites são bloqueados.

Com mais este novo requisito mapeado, a alteração de toda a camada das controllers se faz novamente necessária, já que todas as requisições da API agora devem atender à quantidade máxima de requisições por segundo definida pelo engenheiro de segurança.

Caso esta abordagem continue sendo utilizada, toda nova alteração de código que for mapeada vai gerar uma grande quantidade de retrabalho, além de que as controllers virão a apresentar uma quantidade maior de lógicas externas do que internas, o que dificulta no fator de compreensão das regras de negócios intrínsecas a cada controller.

Uma outra abordagem; mais limpa, elegante e eficiente; que pode ser utilizada é a remoção de toda a lógica externa das controllers e utilizar o padrão `Chain of Responsability` na camada anterior as controllers, isto é, fazer uso dos `Middlewares` para cada uma das verificações.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/chain-of-responsability/camadas.png'>
    <figcaption align='center'>
        <b>Figura 1: Diagrama ilustrando a interação entre a camada de controllers e a camada Chain of Responsability</b>
        <br>
        <small>Autor: Durval Carvalho, 2021.</small>
    </figcaption>
</p>

A camada, aqui chamada de `Chain of Responsability`, nada mais é do que várias funções encadeadas, que irão processar as requisições e as respostas que entram e saem da camada de controllers. As requisições podem ser barradas antes mesmo de chegar nas `controllers` caso uma destas falhe durante a lógica de autenticação, por exemplo. A partir desta abordagem também é possível injetar novos dados na requisição, como o ID do usuário que foi autenticado. Da mesma forma, as respostas que saem da camada de `controllers` podem ser processadas, onde uma pontencial compressão de dados seria realizada, antes de enviar para o autor da requisição.

<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/patterns/chain-of-responsability/internal-chain.png'>
    <figcaption align='center'>
        <b>Figura 2: Diagrama ilustrando a interação entre aos vários componentes da camada Chain of Responsability</b>
        <br>
        <small>Autor: Durval Carvalho, 2021.</small>
    </figcaption>
</p>

Um exemplo real de um Middleware para um projeto que utiliza o [framework Django](https://www.djangoproject.com/) é o código abaixo:

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

Como pode ser visto, as classes `Middlewares` do `Django` não são acopladas umas às outras, ou seja, não possuem nenhum tipo de referência crusada. Desse modo, para que exista uma corrente de responsabilidade o `Framework Django` utiliza uma classe chamada `BaseHandler`, responsável por aplicar os `Middlewares` na requisição que acabou de chegar nos servidor, e assim que a resposta for criada pela `controller`, reaplicar os `Middlewares`, mas agora na ordem inversa, na resposta.

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

As pesquisas e os diagramas feitos nesse documento terão a serventia de apresentar o padrão, explicar suas premissas básicas e apresentar o modo de utilização com a ferramenta Django.

Dessa forma, é possível concluir que a elaboração desse documento irá agregar valor ao nosso projeto.

## Bibliografia

- [1] Refactoring Guru, Chain of Responsibility. Disponível em: https://refactoring.guru/pt-br/design-patterns/chain-of-responsibility (Último acesso em 14/09/2021).

- [2] Source Making, Chain of Responsibility. Disponível em: https://sourcemaking.com/design_patterns/chain_of_responsibility (Último acesso em 14/09/2021).

- [3] Erich Gamma ... [et al.]. Padrões de projeto - Soluções reutilizáveis de software
orientado a objetos. Tradução Luiz A. Meirelles Salgado. Bookman, 2007.

- [4] Django Project, Middleware. Disponível em: https://docs.djangoproject.com/en/3.2/topics/http/middleware/ (Último acesso em 15/09/2021).

</div>
