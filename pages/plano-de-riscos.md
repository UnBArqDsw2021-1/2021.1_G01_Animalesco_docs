# <center> Plano de Riscos

#### Histórico de Versão

|    Data    | Versão |      Descrição       |     Autor(es)     |
| :--------: | :----: | :------------------: | :---------------: |
| 27/07/2021 |  0.1   | Criação do documento | João Vitor Farias |
| 28/07/2021 |  0.2   | Criação da versão inicial da documentação dos riscos | Hugo Sobral e João Vitor Farias |
| 28/07/2021 |  1.0   | Revisão do texto do documento e inclusão da bibliografia | Hugo Sobral |

<div align="justify">

## Introdução

O planejamento do gerenciamento dos riscos é o documento responsável pela identificação e mapeamento dos possíveis riscos que podem vir a surgir durante o tempo de execução do projeto. O processo de gerenciamento dos riscos se inicia com a identificação e categorização dos fatores que, por diversos motivos, podem apresentar obstáculos e impecilhos para o pleno desenvolvimento das atividades e tarefas do projeto.

Desta forma, o objetivo deste documento se concentra na identificação e exposição desses fatores de risco para o Projeto Animalesco.

<br/>

### Categoria dos riscos

Conceitualmente, os riscos podem ser definidos em diferentes categorias que se ramificam a partir da natureza destes. Estas categorias estão descritas na seguinte lista:

- **Técnico:** Os riscos técnicos abordam os requisitos, tecnologia, complexidade, confiabilidade e qualidade.

- **Externo:** Os riscos externos são relativos ao cliente, mercado ou ambiente.

- **Organizacional:** Os riscos organizacionais abordam as dependências do projeto, recursos e priorização.

- **Gerenciamento de projetos:** Os riscos de gerenciamento do projeto abordam a estimativa, planejamento, controle e a comunicação.

<br/>

### Análise quantitativa

#### Probabilidade

| Probabilidade | Intervalo | Peso |
| :-----------: | :-------: | :--: |
|  Muito baixa  |  0 a 15   |  1   |
|     Baixa     |  16 a 35  |  2   |
|     Média     |  36 a 50  |  3   |
|     Alta      |  51 a 65  |  4   |
|  Muito alta   | 66 a 100  |  5   |

#### Impacto

|   Impacto   |                  Descrição                  | Peso |
| :---------: | :-----------------------------------------: | :--: |
| Muito baixa |              Pouco Expressivo               |  1   |
|    Baixo    |                Pouco impacto                |  2   |
|    Médio    |                Impacto Médio                |  3   |
|    Alto     |               Grande impacto                |  4   |
| Muito alto  | Impacto impede o desenvolvimento do projeto |  5   |

#### Prioridade

A prioridade determina a urgência que medidas devem ser tomadas para resolver o risco, e é calculada com base no **impacto** e na **probabilidade**.

|       I/P       | **Muito baixa** | **Baixa** | **Média** | **Alta** | **Muito alta** |
| :-------------: | :-------------: | :-------: | :-------: | :------: | :------------: |
| **Muito baixo** |        1        |     2     |     3     |     4    |        5       |
|    **Baixo**    |        2        |     4     |     6     |     8    |       10       |
|    **Médio**    |        3        |     6     |     9     |    12    |       15       |
|    **Alto**     |        4        |     8     |    12     |    16    |       20       |
| **Muito alto**  |        5        |    10     |    15     |    20    |       25       |

#### Nível de prioridade

| Prioridade  | Intervalo |
| :---------: | :-------: |
| Muito baixa |   1 a 5   |
|    Baixa    |  6 a 10   |
|    Média    |  11 a 15  |
|    Alta     |  16 a 20  |
| Muito alta  |  21 a 25  |

<br/>

## Documentação dos riscos

### Riscos técnicos

| ID | Risco | Consequência | Impacto | Probabilidade | Prioridade |
| -- | ----- | ------------ | ------- | ------------- | ---------- |
| RST01 | Limitação técnica | Demora no desenvolvimento do projeto | Alto | Média | Média |
| RST02 | Má gestão dos requisitos | Desenvolvimento falho do produto | Muito alto | Baixa | Baixa |
| RST03 | Baixa qualidade do software | Comprometimento da confiabilidade e integridade do software | Muito alto | Média | Média |


### Riscos organizacionais

| ID | Risco | Consequência | Impacto | Probabilidade | Prioridade |
| -- | ----- | ------------ | ------- | ------------- | ---------- |
| RSO01 | Má priorização das tarefas  | Confusão e consequente ineficiência na divisão de trabalho | Alto | Alta | Alta |
| RSO02 | Mudança de escopo | Necessidade de replanejamento e repriorização do projeto | Muito Alto | Baixa | Baixa |

### Riscos de gerenciamento de projeto 

| ID | Risco | Consequência | Impacto | Probabilidade | Prioridade |
| -- | ----- | ------------ | ------- | ------------- | ---------- |
| RSGP01 | Comunicação ineficiente entre os membros da equipe | Falta de alinhamento entre o time de desenvolvimento | Médio | Média | Média |
| RSGP02 | Desistência de membros | Sobrecarga de trabalho para o restante da equipe | Alto | Média | Média |
| RSGP03 | Falta de compatilidade entre horários dos membros | Dificuldade para a realização de eventos síncronos entre a equipe | Alto | Baixa | Baixa |
| RSGP04 | Baixa Produtividade da equipe | Atraso nas entregas da disciplina | Alto | Média | Média |


### Risco externo

| ID | Risco | Consequência | Impacto | Probabilidade | Prioridade |
| -- | ----- | ------------ | ------- | ------------- | ---------- |
| RSE01 | Mudança na modalidade de ensino do semestre | Impacto na organização remota da equipe | Muito alto | Muito baixa | Muito baixa |


## Bibliografia

1. Plano de Gerenciamento de Riscos. **Banquinha-Web**. Disponível em https://desenhosoftware-2018-2.github.io/wiki/gerenciamentoRiscos (Último acesso em 28/07/2021).

2. Plano de Riscos. **SpaceShooter**. Disponível em https://github.com/DesenhoMaster2017/SpaceShooter/wiki/Plano-de-Riscos (Últimmo acesso em 28/07/2021).

3. CONTROLE DE RISCOS. **A Monitoria**. Disponível em https://2019-2-arquitetura-desenho.github.io/wiki/dinamica_seminario_II/controle_riscos/ (Último acesso em 28/07/2021).

4. Plano de Gerenciamento de Riscos. **Conecta-Ensina**. Disponível em https://github.com/fga-eps-mds/2020.1-Conecta-Ensina-Wiki/blob/master/docs/plano_de_gerenciamento_de_riscos.md (Último acesso em 28/07/2021).

</div>