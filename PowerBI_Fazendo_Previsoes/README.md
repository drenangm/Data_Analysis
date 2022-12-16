# Fazendo previsoes com o Power BI

Iremos configurar o Power BI para fazer previsões em séries temporais.

O link abaixo foi usado como fonte de dados para extração dos dados que foram carregados diretamente no Power BI:

https://finance.yahoo.com



O Power BI permite que possamos fazer previsoes mas ele nao eh uma ferramenta de machine learning, ele eh uma ferramenta de analise de dados que permite a construcao de visualizacoes e analise de dados com uso de dashboards. 

Mas a Microsoft vem ao longo do tempo incorporando funcionalidades que permitem fazer previsoes em dados, especialmente em series temporais.

De fato, a Microsoft incorporou o modelo ARIMA para dentro do Power BI que, de forma limitada, permite fazer este tipo de analise em series temporais.


Neste projeto temos uma previsao da cotacao de acoes de uma empresa, no caso, utilizamos cotacao da American Airlines.  

Fizemos a importacao da URL abaixo para o Power BI, clicando em historical data:

![image](https://user-images.githubusercontent.com/79231882/206531452-5ad90460-33eb-44cb-a07e-54928a8e9081.png)


Copiamos a URL:

![image](https://user-images.githubusercontent.com/79231882/206531530-854ff54d-9a23-4a4d-a282-b0b7d279aafe.png)


E fazemos uma conexao a esta URL la no Power BI que fara o webscrapping desta pagina:

![image](https://user-images.githubusercontent.com/79231882/206531654-7111afbf-7c28-495a-b47d-fa7e8ec5c788.png)

![image](https://user-images.githubusercontent.com/79231882/206531770-e3f03b48-12ec-446b-a85e-422f67601bea.png)


Vemos as tabelas que ele carregou:

![image](https://user-images.githubusercontent.com/79231882/206531837-18dbf4ce-57f8-42df-9752-c9d458997866.png)


Vamos trabalhar com a tabela 1:

![image](https://user-images.githubusercontent.com/79231882/206531921-8f13d5f1-d7af-4301-848d-cd77493f1d80.png)


Transformamos os dados para os padroes adequados:

![image](https://user-images.githubusercontent.com/79231882/206531993-b826db0f-a289-460d-b504-9d7850126d91.png)


Adicionamos o grafico de linhas, ficaremos com este aspecto. No eixo X adicionamos as datas e no Y a cotacao ajustada.

Importante que para o eixo X editamos para que a data seja inserida sem hierarquia, adicionamos somente as datas:

![image](https://user-images.githubusercontent.com/79231882/206532078-6740470f-1a07-4dee-97df-09fc240f6a85.png)



Apos alguns ajustes ficamos com este aspecto no grafico:

![image](https://user-images.githubusercontent.com/79231882/206532126-9ad12e71-70e2-4ba4-9778-8949694e2760.png)


Lembrando que uma serie temporal eh um fenomeno que ocorre ao longo do tempo. 

Aqui no nosso problema o fenomeno eh variavel a “Adj Close”. 

Agora vamos direto configurar a previsao:

![image](https://user-images.githubusercontent.com/79231882/206532202-62c3eede-3edb-48d7-980a-4fc3c5c03d6b.png)


Primeiro item: comprimento da previsao ou horizonte da pevisao:

→ Quanto maior for o horizonte mais dificil se tornara fazer a previsao.

→ Configuramos nossa previsao para que seja feita em unidades de Meses, que eh a escala mais adequada a este proposito. 

→ Ignoramos os ultimos 2 meses, que significa que ao colocarmos o horizonte de previsao em 3 meses na pratica o Power BI ira pegar os ultimos 3 meses de data e faz a previsao. Mas queremos comparar a previsao do Power BI com o valor real da cotacao, para termos uma nocao do desempenho nas previsoes. Por isso ele ira tracar a linha azul, com os dados reais com um mes de diferenca para as previsoes. Teremos no periodo de 3 meses a previsao e nos 2 meses iniciais deste periodo poderemos ver uma janela comparativa entre real e previsto.

![image](https://user-images.githubusercontent.com/79231882/206532365-c4e85cd9-49f9-42c4-af04-21457a8beb9b.png)


Vemos que mesmo ele tendo errado a previsao, o Power Bi manteve a previsao no intervalo destacado dentro do intervalo de confianca.

Quando alteramos o intervalo de confianca para 75% o modelo mostra-se bem menos preciso:

![image](https://user-images.githubusercontent.com/79231882/206532455-26a7978f-3b22-438e-b4b9-f03bdedb61d4.png)


Quando aumentamos o intervalo de confianca, como consequencia aumentamos os limites inferiores e superiores, logo fica um pouco mais facil termos as previsoes posicionadas dentro desta faixa. Porem quando fazemos isso deixamos o modelo mais abrangente e os valores de previsao poderao ficar mais distantes dos valores reais. 

→ com relacao a sazonalidade sozemos que vamos utilizar 30 pontos de dados para um calculo de sazonalidade:

![image](https://user-images.githubusercontent.com/79231882/206532562-afcd20d7-beb6-4324-9ca4-8f7f9cb1c14a.png)

![image](https://user-images.githubusercontent.com/79231882/206532641-7aa5d9a4-9825-44b1-bba5-b040a67619ee.png)


O que temos de configuracao disponivel para as previsoes eh o que foi mostrado ate aqui. 

Esta ferramenta eh bem mais limitada que opcoes que temos em Python ou R para analisar series temporais. O proposito do Power BI eh outro. 

Observa-se que a Microsoft vem ao longo do tempo adicionando funcionalidades ao Power BI, porem nao vem transformando ele em uma ferramenta de machine learning. O pocionamento que percebemos eh que ele permaneca como uma ferramenta de self service BI.

