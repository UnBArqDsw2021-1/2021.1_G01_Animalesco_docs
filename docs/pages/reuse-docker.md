# <center> Reutilização pelo Docker

#### Histórico de Versão
|    Data    | Versão | Descrição            | Autor(es)       |
| :--------: | :----: | :------------------: | :-------------: |
| 11/10/2021 |  0.1   | Criação do documento | Vinicius Oliveira |


<div align="justify">

## Docker

O Docker é uma plataforma Open Source que facilita a criação e administração de ambientes isolados. Ele possibilita o empacotamento de uma aplicação ou ambiente dentro de um container, se tornando portátil para qualquer outro host que contenha o Docker instalado. A ideia do Docker é subir apenas uma máquina, ao invés de várias. E, nessa única máquina, você pode rodar várias aplicações sem que haja conflitos entre elas. [1]

Para o presente projeto, o uso Docker tem grande importância, ele é utilizado como uma das formas de reutilização. O Docker serve para facilitar o dia a dia dos desenvolvedores e profissionais de infra, criando, de forma simplificada, um ambiente onde possam trabalhar alinhados com sua equipe e infraestrutura de servidores e fique simples criar e re-utilizar containers com “serviços” pré-configurados, simples de alterar e que possam ser versionados e mantidos através de simples arquivos de configuração. [2] 
Ele possui muitos hot spots, e alguns frozen spots, ambos estão sendo utilizados em nossa aplicação. Utilizamos o Docker Compose para orquestrar os containers do Docker.

### Frozen Spots:
* Formatação do arquivo;
* Nome dos arquivos.

### Hot Spots:
* Imagem para construir o container;
* Dependências;
* Comandos que o container executa ao iniciar;
* Network;
* Variáveis de ambiente.


O arquivo do dockerfile é utilizado para criação de nossas imagens, permitindo definir um ambiente personalizado e próprio para o projeto. Abaixo temos como foi estruturado esse arquivo no projeto.

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/reuse-docker/dockerfile.png'>
  <figcaption align='center'>
      <b>Figura 1: Arquivo dockerfile backend</b>
      <br>
  </figcaption>
</p>

O arquivo do docker-compose.yml é o orquestrador de containers do Docker, nesse arquivo descrevemos a infraestrutura como código e como ela vai se comportar ao ser iniciado. Abaixo temos como foi estruturado esse arquivo no projeto.

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/reuse-docker/docker1.png'>
  <figcaption align='center'>
      <b>Figura 2: Arquivo docker-compose backend</b>
      <br>
  </figcaption>
</p>

<p align='center'>
  <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/main/docs/assets/pages/reuse-docker/docker2.png'>
  <figcaption align='center'>
      <b>Figura 3: Arquivo docker-compose backend</b>
      <br>
  </figcaption>
</p>

## Bibliografia

* [1] TreinaWeb. No final das contas: o que é o Docker e como ele funciona? - Marylene Guedes. Disponível em <https://www.treinaweb.com.br/blog no-final-das-contas-o-que-e-o-docker-e-como-ele-funciona> (Último acesso em 11/10/2021)

* [2] School of Net. Entenda para que serve o Docker - Erik Figueiredo. Disponível em <https://blog.schoolofnet.com/para-que-serve-o-docker/> (Último acesso em 11/10/2021)

</div>
