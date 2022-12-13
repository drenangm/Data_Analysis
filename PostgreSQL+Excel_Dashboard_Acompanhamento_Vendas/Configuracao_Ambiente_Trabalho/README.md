# Configuarcao do ambiente de trabalho - Instalando e configurando o PostgreSQL

Vamos utilizar o SGBD pgAdmin:

![image](https://user-images.githubusercontent.com/79231882/207413115-48eb0068-75cb-4aa0-9694-5522adaaa9f4.png)


Escolhemos a versao mais recente do postgre pgAdmin para Win e clicamos em Packages:

![image](https://user-images.githubusercontent.com/79231882/207413189-24c2c39f-08a6-46b5-aea2-bb96be8da111.png)


Selecionamos os OS que abrigara esta versao:

![image](https://user-images.githubusercontent.com/79231882/207413255-a40c2c95-2cd0-44cb-be80-e1a2c8af1684.png)


Clicamos em download the installer:

![image](https://user-images.githubusercontent.com/79231882/207413314-4aef80ee-8379-433d-98ae-56bb647fef69.png)


Escolhemos a versao mais recente do PostgreSQL, e clicamos nela:

![image](https://user-images.githubusercontent.com/79231882/207413399-ca3467e5-deb1-49d1-a237-ebfbb654e794.png)


Executamos o instalador:

![image](https://user-images.githubusercontent.com/79231882/207413457-e0632aea-20b2-489b-bed7-77f556007979.png)


Selecionamos o que queremos instalar:

![image](https://user-images.githubusercontent.com/79231882/207413523-d2805da8-379b-4199-ad0c-754694cedd33.png)


Definimos o local de armazenamento dos dados:

![image](https://user-images.githubusercontent.com/79231882/207413606-b17fbb78-d30e-45b9-9560-1e68a759020e.png)


Definimos a senha do superuser e selecionamos a porta:

![image](https://user-images.githubusercontent.com/79231882/207413672-54d84549-e375-441c-a531-73413e2ba6aa.png)


Para acharmos o app de execucao do postgre, buscamos ele na barra de ferramentas:

![image](https://user-images.githubusercontent.com/79231882/207413809-cc315d8a-74f6-49bf-84fd-2f44e27a43e4.png)


postgre em execução:

![image](https://user-images.githubusercontent.com/79231882/207413896-18d33348-f310-4f01-90a6-fbd39a315367.png)


**Observação (aprendizado):**

O postgre não funcionou na primeira instalação, pois apresentou problemas de comunicação.

Foi necessario checar na pasta:

![image](https://user-images.githubusercontent.com/79231882/207413989-c9a0cab7-ac4a-4832-8bdb-fdbf525b9c2e.png)


Havia uma pasta do postgre dentro deste diretório. Foi necessário deletá-la para que o postgre funcionasse.

**Fonte da pesquisa: [https://stackoverflow.com/questions/54269796/pgadmin4-postgresql-application-server-could-not-be-contacted](https://stackoverflow.com/questions/54269796/pgadmin4-postgresql-application-server-could-not-be-contacted)**


## Overview do pgAdmin

Vamos explorar as opcoes do postgre:

![image](https://user-images.githubusercontent.com/79231882/207414158-6bd07b14-444d-4951-ac3b-f3ff418ad6a8.png)


Vamos abrir:

Schema → public → Tables:

![image](https://user-images.githubusercontent.com/79231882/207414219-2e80d280-a09b-489b-8f8c-8506843fc19a.png)


Por enquanto nao temos nenhuma tabela disponivel, iremos trabalhar nisso mais a frente.

Vamos ver o query tool:

![image](https://user-images.githubusercontent.com/79231882/207414309-a7dfcd59-0560-469c-95c0-e4b0406f2078.png)


Aqui nos escrevemos nossas queries e quando fizermos nossas consultas ao banco conseguiremos ver os resultados em Data Output:

![image](https://user-images.githubusercontent.com/79231882/207414378-25a41a8c-d9fd-4e83-8f3a-c44485be6c4d.png)


## Configuracao do banco de dados

Diagrama do problema que sera estudado (modelo do banco de dados que sera utilizado):

![image](https://user-images.githubusercontent.com/79231882/207414477-e67ca330-fb54-42a2-b74e-c9b91afe1071.png)


Vamos acessar o menu em:

Databases → postgres → schemas → botao direito e create schema

![image](https://user-images.githubusercontent.com/79231882/207414612-911a13e7-c2e9-4155-b3e2-9e3c87b9bf33.png)


Nessa secao iremos criar os dois schemas visto no diagrama acima (schema sales e schema temp_tables)

Criamos o schema sales:

![image](https://user-images.githubusercontent.com/79231882/207414831-9b752724-255c-45d6-9dc4-4cdd1ec0de8d.png)


Criamos o temp_tables:

![image](https://user-images.githubusercontent.com/79231882/207414895-1117f1c8-2297-46bf-981e-4920221bca05.png)

![image](https://user-images.githubusercontent.com/79231882/207414940-38573b87-93ed-49a8-8aa8-a3f1ef41ccff.png)


Vamos em sales → tables e iremos criar uma table dentro deste schema:

![image](https://user-images.githubusercontent.com/79231882/207415022-7c4c7e29-bcec-466f-82cc-6f4a10667422.png)


Iremos acessar o arquivo (em anexo) “Query-Completa”:

![image](https://user-images.githubusercontent.com/79231882/207415151-47be8cf5-8739-43c9-bef2-9995873eead9.png)


Copiar todas estas queries e colar dentro do schema.

![image](https://user-images.githubusercontent.com/79231882/207415226-eb57aade-dfa2-4707-99bc-93c025f6c4bf.png)


Temos agora 165000 linhas dentro do schema sales (tables), esta sera nossa base de dados que foi gerada como uma copia de uma fonte externa. Noa eh o objetivo abordar a geracao ou modelamento de um banco de dados.



Vamos rodar estes scripts dentro do postgre, para isso clicamos em **F5:**

![image](https://user-images.githubusercontent.com/79231882/207415544-b48f6a37-5076-4665-932c-15937e715214.png)


Vamos ver como as tabelas foram inseridas.

Para isso vamos dar um refresh em sales e temp_tables:

![image](https://user-images.githubusercontent.com/79231882/207415628-8d118295-cdfb-4122-b411-1845faca94b3.png)


Vemos as tabelas criadas em sales e temp_tables:

![image](https://user-images.githubusercontent.com/79231882/207415731-c727cdfd-0dd9-4ac9-9884-36d792c46a64.png)

![image](https://user-images.githubusercontent.com/79231882/207415772-a9d0deee-39f9-4a77-b04f-626e0c8265c3.png)


Aqui podemos ver todas as colunas criadas em uma das tabelas em sales:

![image](https://user-images.githubusercontent.com/79231882/207415898-72d787f9-6707-4c90-9099-09b8f4a06d3f.png)
