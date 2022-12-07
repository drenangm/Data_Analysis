# Fonte de Dados

Usaremos dados reais disponíveis publicamente. O download do dataset pode ser feito no link abaixo:

[https://www.kaggle.com/mishra5001/credit-card](https://www.kaggle.com/mishra5001/credit-card)

Este conjunto de dados contém informações de inadimplentes de cartão de crédito com base nos respectivos atributos! Vamos construir um dashboard para detectar eventuais fraudes no uso de cartão de crédito.

O dataset será fornecido a você junto com os demais scripts do mini-projeto.

# Construcao da data app

Vamos criar uma funcao para carregamento dos dados:

![image](https://user-images.githubusercontent.com/79231882/202486369-e21ebace-9a87-4f8a-afa3-3b3e983c279e.png)


Definiremos a pagina em que sera acessada a nossa aplicacao contendo o dashboard:

![image](https://user-images.githubusercontent.com/79231882/202486434-de2fc05e-8c02-4b81-bd14-3d160cfe1ca6.png)


Salvamos ate aqui. Quando isto eh feito automaticamente o H2O Wave detecta.

Acessamos a pagina que estamos criando para testar:

![image](https://user-images.githubusercontent.com/79231882/202486583-e3db1671-f642-4cf6-9bd7-71af238b95aa.png)


Por enquanto ela nao contem nada desenvolvido.


Vamos submeter o primeiro elemento visual a pagina.

Vamos criar o cabecalho do cartao:

![image](https://user-images.githubusercontent.com/79231882/202486717-fbb1b425-6c51-4de0-8b31-86b2604fcedb.png)



- Box siginifica as coordenadas em que o card estara posicionado.

Para vermos as atualizacoes sendo incoporadas a pagina precisamos incluir o codigo abaixo:

![image](https://user-images.githubusercontent.com/79231882/202486821-450e0c96-1803-48d0-92c7-a9672547e04c.png)


Aguardamos alguns instantes e vemos a pagina sendo atualizada:

![image](https://user-images.githubusercontent.com/79231882/202487086-33bf6836-2d93-49cc-99c2-ffb4d2327fa8.png)


Vamos adicionar os graficos ao dashboard.

Vamos comecar adicionando um grafico de barras com uma serie de efeitos.

Quando passamos o mouse sobre as barras vemos uma interatividade em que mostra um cartao suspenso com os dados numericos que estao nas barras.

Comecamos preparando os dados fatiando as colunas que queremos para  este grafico:
![image](https://user-images.githubusercontent.com/79231882/202487215-19b86bfd-d1ae-4509-8c14-2fb25d196af0.png)


Construcao do grafico.

Um ponto importante quando passamos as coordenadas de posicao de um objeto grafico temos a seguinte denominacao:
![image](https://user-images.githubusercontent.com/79231882/202487289-9667319f-b310-4dfa-b013-549ac48b991d.png)

No exemplo da figura acima:

1: coluna

3: linha

4: largura

4: altura

![image](https://user-images.githubusercontent.com/79231882/202487459-e2f6a473-04cf-4be8-8d0f-600f8c807978.png)

Aplicacao ate o momento:
![image](https://user-images.githubusercontent.com/79231882/202487542-84e94cfe-bff3-43dc-a6ce-f55ce868662d.png)


Vamos construir um grafico de dispersao em que iremos mostrar os clientes x escolaridade:
![image](https://user-images.githubusercontent.com/79231882/202487623-646fdeb0-d7b8-4fa9-ac2e-ea64f08a66e7.png)

![image](https://user-images.githubusercontent.com/79231882/202487681-d481552f-95cc-4d1e-8b33-0e8afd158a21.png)


E criamos o grafico 3, que mostrara o total de rendimentos por total de credito com grafico de bolhas.

Aqui queremos observar se ha discrepancia entre renda e credito concedido.
![image](https://user-images.githubusercontent.com/79231882/202487801-d4165290-4916-4a46-b9f1-e413210691ab.png)
![image](https://user-images.githubusercontent.com/79231882/202488147-83ce3a1c-1b76-42a6-84d6-5c32210f4513.png)

No grafico criado, podemos observar possiveis indicios de fraudes, pois podemos ver alguns outliers indicando incompatibilidade entre renda x credito:

![image](https://user-images.githubusercontent.com/79231882/202488217-34eccef2-24fa-40e3-a4aa-37347117a781.png)


Vamos adicionar um grafico de barras empilhadas (stacked bar). Nele iremos plotar o total de rendimentos por tipo de rendimento e status familiar.


Um stacked bar eh bastante adequado para plotarmos um grafico que requer tres informacoes.
![image](https://user-images.githubusercontent.com/79231882/202488322-6017ce69-7c88-47b2-850e-79b202c4b8c3.png)

![image](https://user-images.githubusercontent.com/79231882/202488374-92355a3a-cbd1-4498-8619-17434f9947de.png)


Construiremos mais 4 graficos.

Grafico 5: Gráfico de Total de Rendimentos Por Tipo de Empréstimo (Gráfico de Linha)
![image](https://user-images.githubusercontent.com/79231882/202488471-7575b27c-711a-4836-9051-eef998648286.png)


Grafico 6: Gráfico de Total de Rendimentos Por Tipo de Rendimento e Estado Civil (Gráfico de Área)
![image](https://user-images.githubusercontent.com/79231882/202488548-117ffa41-9004-44e5-a605-5df9a413dbea.png)


Grafico 7: Gráfico de Total de Rendimentos Por Tipo de Empréstimo (Gráfico de Linha Step)
![image](https://user-images.githubusercontent.com/79231882/202488633-ff089d62-f41d-4c28-8457-a9b74ffd4956.png)


Grafico 8: Gráfico de Total de Rendimentos Por Tipo de Residência (Gráfico de Barras)
![image](https://user-images.githubusercontent.com/79231882/202488711-5dc7cc79-29ce-421d-91a4-83de474ef710.png)


Layout completo com a inclusao dos 4 graficos adicionais:
![image](https://user-images.githubusercontent.com/79231882/202488806-95ace841-987e-418f-b497-e2e532c0461f.png)


Importante formatar em algum lugar um esboco para construcao da visao do dashboard, observando a proporcao entre os graficos para posiciona-los da melhor forma possivel no layout de visualizacao.

![image](https://user-images.githubusercontent.com/79231882/202488999-0b0a3d8c-0afa-4469-be54-412ef3310ed3.png)

