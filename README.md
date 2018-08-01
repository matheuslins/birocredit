# Biro Credit

## O problema

Os sistemas monolíticos não dão mais conta da demanda atual. Temos uma abundância de dados complexos que precisam ser processados de forma confiável, rápida e escalável. Esse é um dos problemas que empresas (com sistemas antigos) possuem.

## A Solução

Muitas empresas estão migrando seus softwares da MA(Monolithic Architecture) para a MSA(Microservices-Styled Architecture), um estilo de arquitetura baseada em microserviços. Algumas vantagem dessa mudança são:

 - **Escalabilidade**: É fácil escalar
 - **Fácil Mantenabilidade**: Como o problema é dividido em pequenas partes, permite que cada time de programadores trabalhe em diferentes componentes.
 - **Os problemas se isolam**: É possivel encontrar o problema mais rápido.
 - **Integração e Entrega Continua**: Está ligado ao modelo de entrega ágil, quanto mais rápido entregar, mais rápído corrigimos erros (Feedbak Contínuo) 
 - **Variedade nas linguages de programação**: A aplicação não fica dependente de apenas uma linguagem.

Baseado nisso, foi criado o seguinte modelo arquitetural

### Modelo Arquitetural

- [Imagem do modelo]

## Armazenamento

Um bom sistema de gerenciamento de dados (SGBD) deve fornecer mecanismos que auxiliam sua segurança. Um SGBD seguro oferece:

 - **Integridade**: Os dados precisam ser protegidos por qualquer alteração impŕopria ou não autorizada;
 - **Disponibilidade**: Os dados precisam estar disponíveis a todo momento para usuários e sistemas que estão autorizados à acessa-los;
 - **Confidenciabilidade**: Como o próprio nome já diz, o acesso aos dados precisa ser confiável, ou seja, assegura que o dado só pode ser concedido a quem tem concessão.

#### Base A

Esta base contém dados extremamente sensíveis e deve ser protegida com os maiores níveis de segurança, por outro lado, não precisa ser tão performática.

Banco de dados escolhido: PostgreSQL.

O PostgreSQL é um banco robusto que possui vários recursos. O principal motivo que me fez escolher este banco para esta base foi integridade. Quando se refere a integridade dos dados, o PostgreSQL prover várias técnicas avançadas para tal.

 - **Checkpoints**: Para a gravação de dados em massa, o banco armazena temporariamente os dados na memória RAM. Como a mesma é volátil, existe um grande risco do dado se perder na transição. Os checkpoints forçam todas as transações concluidas a serem gravadas da RAM para o disco.
 - **Write-Ahead Logging (WAL)**: Todas as mudanças são gravadas somente após o registro no log. Esta técnica garante que se ocorrer alguma falha no meio da transição, seja possível recuperar o banco usando o log. Essa recuperação é conhecida REDO.
 - **Transaction Logging**: Além de serem gravadas no banco, todas as modificações de transações (Insert, Delete, Update e etc) são gravadas no log. Essa duplicidade de informação reduz a perda de dados por falha de hardware ou queda de energia.
 - **Triggers**: O usuário do banco pode escrever gatilhos que garantem a integridade referencial das tabelas.
 - **Commit/Rollback**: Certas funções de banco de dados requerem o agrupamento de transações de modo que, se qualquer parte de uma função falhar, toda a função falhe. Um exemplo disso é a transferência bancária. Caso o insert falhe, é dado um *rollback* na função e nenhum valor é movimentado.
 - **Sistemas de papéis (ROLES)**: O PostgreSQL gerencia as permissões através deste sistema. Basicamente cada usuário possui um papel que está associado a um grupo de permissões.
 - **SSL**: Permite conexões criptografadas na comunicação cliente/servidor

#### Base B

A base B também possui dados críticos, porém, ao contrário da Base A, o acesso precisa ser mais rápido. Além disso, esta base é usada para a extração de dados por meio de algoritmos de aprendizado de máquina.

Banco de dados escolhido: PostegreSQL

Nesta base a performance é mais crucial que na base A, além disso, é preciso se preocupar com a integridade (já que também possui dados cŕiticos). Escolhi usar PosgreSQL pois é um banco que além de seguro, performa muito bem quando se trata de velocidade de leitura e escrita.

Outra opção seria usar um banco NoSQL já que são bem mais performáticos do que o PostgreSQL (baseado no modelo DBMS). Porém neste caso, além da velocidade é preciso também garantir a segurança. Como os NoSQL's não possuem uma segurança tão robusta quanto os DBMS's, decidi usar o mesmo da Base A.

Obs: Apesar de serem base de dados com propósitos um pouco diferentes. Não vi necessidade de mudar o banco. Afinal, o PostgreSQL trabalhar muito bem em ambas.

#### Base C

Esta base não possui nenhum tipo de dado crítico, mas em compensação precisa ter o acesso extramentente rápido. Tem como principal funcionalidade restrear eventos relacionados a um determinado CPF. Como essa ação é mais corriqueira, a velociadade na consulta e a disponibilidade dos dados são extramamente importantes.

Banco escolhido: MongoDB

A escolha do MongoDB se dar por várias razões. São elas:
- É um banco orientado a documento, o que facilita a consulta.
- É altamente performático
- Possui uma grande disponibilidade
- É facilmente escalável
- Possui o recurso de particionamento de dados, o que facilita a escalabilidade horizontal

## Tráfego

O tráfego é composto por sistemas com duas diferentes arquiteturas: micro-serviços e nano-serviços. Por isso são baseados em API's construídas com micro-framework.


## Disponibilidade dos dados
## Tecnologias Usadas
## Referências


###### 1 - [Microservice architecture: All the best practives you need to know](https://codingsans.com/blog/microservice-architecture-best-practices)

###### 2 - [Conheça o particionamento de dados (Sharding) no MongoDB!](http://db4beginners.com/blog/sharding-no-mongodb/)

###### 3 - [How to build a cloud-based SaaS application](https://usersnap.com/blog/cloud-based-saas-architecture-fundamentals/)

###### 4 - [PostgreSQL - Data Integrity](http://www.dbexperts.net/postgresql/integrity)

###### 5 - [Top 5 SQL Databases](https://dzone.com/articles/top-5-sql-databases)

###### 6 - [Top 4 NoSQL Databases](https://dzone.com/articles/top-4-nosql-databases)
