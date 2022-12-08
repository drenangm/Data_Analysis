# Conectando em um banco de dados Oracle e gerando visualizacoes


Para fazermos a conexao ao banco de dados Oracle com o Tableau precisamos te-lo instalado na nossa maquina ou em servidor ao qual precisaremos ter acesso (via um DBA ou pessoa que administra o banco de dados) por meio de:

- nome do servidor

- nome do servico

- porta

- usuario

- senha


Vamos utilizar o Tableau Desktop, pois eh ele que permite conexao ao banco de dados.

No menu de selecao fomos em “to a server” e selecionamos Oracle:

![image](https://user-images.githubusercontent.com/79231882/206534272-d4159b26-f0b8-4ac9-b6e5-0d7fda4d94f9.png)


Digitamos os dados do banco de dados:

![image](https://user-images.githubusercontent.com/79231882/206534366-4a75a432-8625-45fb-a23c-fceaacbba278.png)


Conectamos ao banco de dados em que pdemos ver do lado esquerdo as tabelas as quais o usuario possui acesso:

![image](https://user-images.githubusercontent.com/79231882/206534415-81364c66-70f2-45c5-91e1-5630e8801630.png)


Pegamos uma das tabelas e arrastamos para a area de trabalho (Customer ID):

![image](https://user-images.githubusercontent.com/79231882/206534510-07f4b926-138d-4337-acc3-1b2b4681a9f8.png)

![image](https://user-images.githubusercontent.com/79231882/206534541-5f2e8119-9d37-48fd-b759-0301585e7642.png)



Clicamos em Sheet1 para abrir uma nova workspace.

![image](https://user-images.githubusercontent.com/79231882/206534593-c4959f8d-caf6-49c5-8d8b-cbe940867c21.png)


Podemos ver todas as dimensoes e medidas reconhecidas pelo Tableau.

A partir daqui ja estamos conectados ao banco, basta iniciar o trabalho de elaboracao da visualizacao.

Vamos criar uma visualizacao em que iremos ver o Salario por Estado Civil. Carregamos para a coluna Marital Status e para a linha Salary:

![image](https://user-images.githubusercontent.com/79231882/206534649-b8bba423-d395-4c66-ae86-47b8263beb15.png)


Podemos inserir uma outra variavel tambem, vamos trazer o Sexo:

![image](https://user-images.githubusercontent.com/79231882/206534715-5a2d0694-3ecf-48be-a3c1-4760e8c64f7b.png)

