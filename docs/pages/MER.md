# <center> Entidade Relacionamento

#### Histórico de Versão

|    Data    | Versão |      Descrição       |     Autor(es)     |
| :--------: | :----: | :------------------: | :---------------: |
| 12/08/2021 |  0.1   | Criação do documento | Daniela Soares  |
| 12/08/2021 |  0.2   | Revisão do documento | João Vitor Lopes |

## 1 Introdução
<div align="justify">
O Modelo de Entidade-Relacionamento (ME-R) é baseado na percepção do mundo real que consiste em um conjunto de objetos básicos chamados ENTIDADES e nos RELACIONAMENTOS entre estes objetos.
O ME-R foi desenvolvido para facilitar o projeto de banco de dados, permitindo a especificação de um esquema de “negócio”, onde tal esquema representa a estrutura lógica geral do Banco de Dados (BD).

## 2 Modelo Entidade Relacionamento

SISTEMA APP ANIMALESCO – Descrito pelas Entidades USUARIO, PET, BANHO, MEDICAMENTOS, CARTEIRAVACINA, VISITASVETERINARIO, PESO, ALTURA.

### 2.1 Entidades e atributos
#### 2.1.1 Entidade USUARIO
Representa os usuarios que deseja manter no sistema APP Animalesco. A ocorrêcia da entidade usuario terá associado os seguintes atributos: **idUsuario**, **nome**, **email**, **senha**.

#### 2.1.2 Entidade PET
Representa os pets que deseja manter no sistema APP Animaslesco. A ocorrência da entidade pet terá associado os seguintes atributos: **idPet**, **nome**, **dataNascimento(idade)**, **peso**, **altura**, **especie**, **raca**, **sexo**.

#### 2.1.3 Entidade BANHO
Representa os banhos registrados no sistema APP Animalesco. A ocorrência da entidade banho terá associado os seguintes atributos: **idBanho**,  **dataBanho**, **horaBanho**, **banhoCasa**, **banhoPetShop**.

#### 2.1.4 Entidade MEDICAMENTOS
Representa os medicamentos registrados no sistema APP Animalesco. A ocorrência da entidade medicamentos terá associado os seguintes atributos: **idMedicamentos**, **nomeMedicamento**, **dataInicio**, **dataFinal**, **perioAplicacao(periodicidadeHoras)**.


#### 2.1.5 Entidade CARTEIRAVACINA
Representa as carteiras de vacinação registradas no sistema APP Animalesco. A ocorrência da entidade carteiraVacina terá associado os seguintes atributos: **idCarteira**,**nomeVacina**, **dataDose**, **dataRepetirDose**.

#### 2.1.6 Entidade VISITASVETERINARIO
Representa as visitas ao veterinario registradas no sistema APP Animalesco. A ocorrência da entidade visitasVeterinario terá associado os seguintes atributos: **idVisitas**, **dataVisita**, **descricao**.

#### 2.1.7 Entidade PESO
Representa o peso registrado no sistema APP Animalesco. A ocorrência da entidade peso terá associado os seguintes atributos: **idPeso**, **idPet**, **pesoPet**, **dataPesagem**.

#### 2.1.8 Entidade PESO
Representa o altura registrado no sistema APP Animalesco. A ocorrência da entidade altura terá associado os seguintes atributos: **idAltura**, **idPet**, **alturaPet**, **dataMedicao**.

### 2.2 Relacionamentos

#### 2.2.1 USUARIO - tem – PET
Um usuário pode ter vários pets, mas um pet não pertencer a vários usuários. **Cardinalidade: n : m**.

#### 2.2.2 PET - toma – BANHO
Um pet pode tomar vários banhos, mas um  um banho não  pode limpar vários pets. 
**Cardinalidade: n : m**.

#### 2.2.3 PET - toma -  MEDICAMENTOS
Um pet pode tomar vários medicamentos, assim como um medicamento pode pertencer a vários pets. **Cardinalidade: n : m**.

#### 2.2.4 PET - tem – CARTEIRAVACINA
Um pet pode ter várias carteiras de vacinas mas uma carteira de vacina não pode ter  vários pets. **Cardinalidade: n : m**.

#### 2.2.5 PET - faz -  VISITASVETERINARIO
Um pet pode fazer várias visitas ao veterinario mas uma visita é realizada por apenas um pet. **Cardinalidade: n : m**.

#### 2.2.6 PET - ter – PESO
Um pet não pode ter varios pesos, assim como um peso não pode pertencer a vários pet. **Cardinalidade: n : m**.

#### 2.2.6 PET - ter – ALTURA
Um pet não pode ter varias alturas, assim como uma altura não pode pertencer a vários pet. **Cardinalidade: n : m**.

</div>


<p align='center'>
    <img src='https://raw.githubusercontent.com/UnBArqDsw2021-1/2021.1_G01_Animalesco_docs/71-EntidadeRelacionamento/docs/assets/images/mer.png'>
    <figcaption align='center'>
        <b>Figura 1: Diagrama de Entidade Relacionamento</b>
        <br>
        <small>Autora: Daniela Soares, 2021.</small>
    </figcaption>
</p>
