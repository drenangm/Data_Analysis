Vamos construir uma visualização para análise de dados financeiros. Daremos ênfase ao processo de extração de dados e tratamento e transformação dos dados que, conforme você verá nas aulas, tem impacto direto no processo de análise.

## Fonte de Dados:

O link abaixo será usado como fonte de dados direto no Power BI:

[https://finance.yahoo.com/quote/AMD/history?p=AMD](https://finance.yahoo.com/quote/AMD/history?p=AMD)


Com o Power BI aberto, comecaremos salvando o projeto:

![image](https://user-images.githubusercontent.com/79231882/206514894-7654a40d-db36-4ca2-95d6-140aef107f84.png)


Vamos criar uma visualizacao de dados finaceiros em tempor real.

Vamos extrair os dados financeiros do portal Yahoo Finance:

[https://finance.yahoo.com/quote/AMD/history?p=AMD](https://finance.yahoo.com/quote/AMD/history?p=AMD)

![image](https://user-images.githubusercontent.com/79231882/206515155-570ffeef-ec23-4656-b6f5-afd9782b1c70.png)

Podemos fazer o download de uma tabela com o historico contendo as cotacoes das acoes aqui:

![image](https://user-images.githubusercontent.com/79231882/206515245-76a5ac8d-45db-4841-bb95-d8026e21ced2.png)

Mas vamos acessar diretamente a URL la no Power BI, para que posssamos configurar o refresh automatico e termos uma busca das cotacoes em tempo real.

Vamos copiar esta URL e clicar em Obter Dados:

![image](https://user-images.githubusercontent.com/79231882/206515338-1215afe5-1235-4f1c-8b0e-0be79f741d70.png)

Digitamos a URL na caixa:

![image](https://user-images.githubusercontent.com/79231882/206515404-94664133-f135-41ee-931e-a80e4af3b42c.png)

Escolhemos tippo de conexao Anonima (sem usuario e senha) e clicamos em conectar:

![image](https://user-images.githubusercontent.com/79231882/206515537-bef877c7-d2d7-47b0-843e-9d07de78cae2.png)


Aparecera a exibicao abaixo, em que o Power BI foi ate a pagina HTML, fez o webscrapping, extrai uma serie de tabelas contendo dados e exibe-as para nos:

![image](https://user-images.githubusercontent.com/79231882/206515662-2337194b-aaa6-46ab-a1df-98cb189da276.png)





















