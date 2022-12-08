# Usando grafico customizado no Power BI

Vamos criar um gráfico customizado no Power BI, o Candlestick Chart, e como interpretá-lo.

## Fonte de Dados:

O link abaixo foi usado como fonte de dados para extração dos dados que colocamos em uma planilha Excel que será carregada no Power BI.

[https://finance.yahoo.com](https://finance.yahoo.com/)


Definicao do candlestick chart:

[https://www.investopedia.com/trading/candlestick-charting-what-is-it/](https://www.investopedia.com/trading/candlestick-charting-what-is-it/)


Quando houver algum tipo de diuvida sobre um grafico, existe um site que possui explicacao sobre a grande maioria deles:

[https://datavizcatalogue.com/](https://datavizcatalogue.com/)


Vamos criar um candlestick chart, mas o Power BI nao oferece este tipo de grafico na versao desktop.

Se clicarmos em obter mais visuais ele ira solicitar um endereco de email corporativo ou de estudante porque ele ira solicitar o Power BI Server:

![image](https://user-images.githubusercontent.com/79231882/206527398-ed750bfb-0c9a-4e8e-960b-97a98c2778f1.png)


Existe uma opcao, podemos ir em:

[https://appsource.microsoft.com/en-us/marketplace/apps?product=power-bi-visuals](https://appsource.microsoft.com/en-us/marketplace/apps?product=power-bi-visuals)


Especificamente, existe uma opcao para os candlesticks para uso no Power BI:

[https://appsource.microsoft.com/en-us/product/power-bi-visuals/WA104380952?tab=Overview](https://appsource.microsoft.com/en-us/product/power-bi-visuals/WA104380952?tab=Overview)

![image](https://user-images.githubusercontent.com/79231882/206527532-87fa8f03-3b4d-43d0-a29e-3c5cf34642a8.png)


Para experimentar esta solucao, devemos clicar em Download Sample. Sera baixado um arquivo do Power BI.

Apos feito o download, basta abrirmos o arquivo:

![image](https://user-images.githubusercontent.com/79231882/206527672-e365bc12-3934-46f2-8dbb-7f9e6df6f504.png)


Aqui consta o icone do candlestick:

![image](https://user-images.githubusercontent.com/79231882/206527747-addfe8fb-6be9-4e72-8ba1-a3d005506541.png)


Explorando demais solucoes que podem ser agregadas ao Power BI basico.

Vamos clicar em transformar dados dentro do nosso candlestick chart:

![image](https://user-images.githubusercontent.com/79231882/206527892-1c4c1a62-522c-4e6f-a7ef-ec0705120546.png)


Veremos uma mensagem de erro devido a referencia desconhecida para o fonte de dados:

![image](https://user-images.githubusercontent.com/79231882/206527954-ed953d9b-9e0c-4530-a9ea-64c7f5d79414.png)

![image](https://user-images.githubusercontent.com/79231882/206527975-d222248c-073c-4fae-848f-28b34125b8b6.png)

Isso eh esperado, pois a referencia esta em relacao ao local da pessoa que desenvolveu a aplicacao.


Vamos ver uma versao customizada do candlestick chart. Iremos plugar nossos dados do arquivo em anexo:

![image](https://user-images.githubusercontent.com/79231882/206528142-c37c368c-dcf9-406f-bad9-2cb3f0668166.png)


Carregamos os dados (arquivo .csv):

![image](https://user-images.githubusercontent.com/79231882/206528213-58af6093-eb8e-40e5-8c5b-d8bb94f4bf35.png)


Esses sao os dados que inserimos em cada eixo para montagem do grafico:

![image](https://user-images.githubusercontent.com/79231882/206528403-9c8a86dc-f339-4cd8-bf19-926e99eaccb1.png)









