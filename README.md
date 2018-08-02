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

## Modelo Arquitetural

![Modelo Arquitetural](https://github.com/matheuslins/birocredit/blob/master/imagens/modelo-arquitetural.png)

## Armazenamento

![Armazenamento](https://github.com/matheuslins/birocredit/blob/master/imagens/armazenamento.png)

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

Obs: Apesar de a Base A e a Base B terem propósitos um pouco diferentes. Não vi necessidade de mudar o banco. Afinal, o PostgreSQL trabalhar muito bem em ambas.

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

![Tragego](https://github.com/matheuslins/birocredit/blob/master/imagens/trafego.png)

###### Arquitetura

Para que todos os dados sejam disponibilizados de forma escalável, segura e rápida, será utilizado uma arquitura baseada em API.

###### Comunicação

Uma boa prática na construção de múltiplos micro serviços, é nunca depender de uma comunicação síncrona. O *entrypoint* (ponto de entrada), pode ser disponibilizado através de um protocolo sincrono (HTTP), já que é uma comunicação direta de pedido e resposta, mas os micro serviços se comunicam indiretamente, por isso o ideal é que essa comunicação seja assincrôna.

###### API Geteway

A melhor abordagem para a comunicação *client-to-microservice* é usando uma espécie de orquestrador. A API Geteway, possui algumas vantagem que me fizeram escolher esse padrão. São elas:

- **Controle de acesso**: Através de *API Keys* é possível *trackear* o uso de cada API.
- **Controle de requests**: É possível controlar quantas requisições cada usuário faz para cada API.
- **Análise e Monitoramento**: Entendimento de como as API's estão iniciando e performando.
- **Controle de Cache**: Com esse controle, é possível acelerar o acesso ao dado em cada API.
- **Single Public Endpoint**: Todas as requests dos clientes passam por um único ponto.

Para construção de tal, será usado o [API Umbrella](https://apiumbrella.io/)

###### Micro Serviços

Será utilizado o estilo arquitetural REST. As API's REST estarão disponíveis como micro serviços facilitando a integração com as bases.

Também é importante frizar que uma API REST deve seguir alumas regras para que possa ser considerada REST de fato:

**1 - Oferecer acesso através de recursos**: Através de seus *endpoints* a API precisa oferecer seus recursos onde o cliente possa utilizar operações padrões, ao invés de uma interface de comando especifica.

Não é REST: `/changeTodoList.php?item=35&action=changeTitle&title=new_title`

É REST: `/todolists/7/items/35/`

**2 - Representa recursos por *representations***: No padrão REST, os *endpoints* identificam coisas e não formatos. Para que a comunicação entre diferentes plataformas aconteça, os recursos precisam ser disponibilizados em *endpoints* do mesmo padrão, e quem decide o tipo de formato é o cliente. Os formatos desejados pelo cliente são passados no cabeçalho da *request* usando a técnica de [negociação de conteúdo](https://en.wikipedia.org/wiki/Content_negotiation).

Não é REST:

- `browser: /showTodoList.php?format=html`
- `application: /showTodoList.php?format=json`

É REST: 

- `browser: “I want /todolists/7/, please give me HTML.”`
- `application: “I want /todolists/7/, please give me JSON.”`

**3 - Mensagem auto descritivas**: O sistema REST deve ser capaz de interpretar qualquer mensagem isoladamente.

Se tivermos a seguinte conversa:

 - **msg1** - `/search-results?q=cars`
 - **msg2** - `/search-results?page=2`
 - **msg3** - `/search-results?page=3`

e isolarmos a `msg2` ou a `msg3`, não é possível saber de qual recurso se trata. Está claro que é desejável acessar a página 2 ou 3, porém não se sabe de que.

No estilo REST, mesmo se isolarmos a chamada 2 ou 3, claramente da para saber de qual recurso se trata.

 - **msg1** - `/search-results?q=cars`
 - **msg2** - `/search-results?q=cars&page=2`
 - **msg3** - `/search-results?q=cars&page=3`

**Conectar os Rercursos através de Links**: Quando entramos em um site que nunca vimos antes, usamos links para navegar e não precisamos modificar a url para tal. Quando falamos de conectar os recursos com links, estamos nos referindo à *hyperlinks*

Não é REST:

```
/cars/7/

{
  "name": "My cars",
  "items": [35, 36]
}
```

É REST:
```
/cars/7/

{
  "name": "My cars",
  "items": ["/cars/7/items/35/", "/cars/7/items/36/"]
}
```

Utilizarei o [Django Rest Framework](http://www.django-rest-framework.org/) para a criação das API's.

###### Message queue (MQ)

Como a comunicação entre os micro serviços será assincrona, vou precisar de um *broker* para enfileirar todas as mensagens vindas das API's. O maior ganho ao usar um MQ é a alta escalabilidade.

Será utilizado o [RabbitMQ](http://www.rabbitmq.com) para tal.

### Micro Serviço 1
### Micro Serviço 2
### Micro Serviço 3


## Disponibilidade dos dados

![Disponibilidade dos dados](https://github.com/matheuslins/birocredit/blob/master/imagens/disponibilidade-dos-dados.png)

## Tecnologias Usadas
## Referências


###### 1 - [Microservice architecture: All the best practives you need to know](https://codingsans.com/blog/microservice-architecture-best-practices)

###### 2 - [Conheça o particionamento de dados (Sharding) no MongoDB!](http://db4beginners.com/blog/sharding-no-mongodb/)

###### 3 - [How to build a cloud-based SaaS application](https://usersnap.com/blog/cloud-based-saas-architecture-fundamentals/)

###### 4 - [PostgreSQL - Data Integrity](http://www.dbexperts.net/postgresql/integrity)

###### 5 - [Top 5 SQL Databases](https://dzone.com/articles/top-5-sql-databases)

###### 6 - [Top 4 NoSQL Databases](https://dzone.com/articles/top-4-nosql-databases)

###### 7 - [What is an API and how it differs from REST API?](https://www.quora.com/What-is-an-API-and-how-it-differs-from-REST-API#)

###### 8 - [What is a REST API?](https://www.quora.com/What-is-a-REST-API)

###### 9 - [Communication in a microservice architecture](https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/architect-microservice-container-applications/communication-in-microservice-architecture)

###### 10 - [Asynchronous communication with message queue](https://codeblog.dotsandbrackets.com/asynchronous-communication-with-message-queue/)