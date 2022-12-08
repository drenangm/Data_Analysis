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



Vamos clicar em um delas para ver seu conteudo:

![image](https://user-images.githubusercontent.com/79231882/206515863-777c04c0-0295-4aee-9f4d-ae08958525dd.png)


Podemos ver que no webscrapping feito pelo Power BI eh disponibilizado um arquivo HTML, poderiamos extrai-lo, salvar em algum lugar e continuar um outro tipo de trabalho de analise:

![image](https://user-images.githubusercontent.com/79231882/206515948-c3da20fa-3c40-4937-8c83-9f2bad649f29.png)


Vamos trabalhar com a tabela 1:

![image](https://user-images.githubusercontent.com/79231882/206516022-285c0496-7aa2-4158-a823-bca523717635.png)


Os campos desta tabela estao carregados:

![image](https://user-images.githubusercontent.com/79231882/206516096-a00ff0e1-539a-4867-9016-e0ca04d5d68f.png)


Mas os dados extraidos terao alguns problemas, ja podemos ver que ele extrai as colunas com um nome generico, o que indica que ele nao conseguiu extrair o titulo das colunas.

Para verificar o que significa cada uma das colunas devemos ir no lado esquerd e clicar em Tabela:

![image](https://user-images.githubusercontent.com/79231882/206516174-f17509e2-1f2f-49d9-8edd-e15381060293.png)


Ja podemos ver que na primeira linha consta o cabecalho de cada coluna mais a frente faremos as correcoes:

![image](https://user-images.githubusercontent.com/79231882/206516253-b2a3ce86-ecbd-40a4-8aae-67b506f9f8a1.png)


Como o Power BI nao foi capaz de identificar os cabecalhos de cada coluna teremos que ajustar manualmente. 

Voltamos a visualizacao e clicamos em Transformar Dados:

![image](https://user-images.githubusercontent.com/79231882/206516330-afb3f7f8-e74d-4e24-8526-350ef04f88fc.png)


O Power Query sera aberto para que possamos editar:

![image](https://user-images.githubusercontent.com/79231882/206516389-09917fd5-72de-4f37-9787-c76323989980.png)


Basta clicarmos em usar a primeira linha como cabecalho:

![image](https://user-images.githubusercontent.com/79231882/206516463-89c43384-64ec-497f-8902-f59c76b38ef5.png)


Para modificacoes mais basicas como essa o Power BI pode ser uma otima opcao, considerando que se usassemos uma linguagem como Python ou R levasse muito mais tempo para fazermos isso.

Se observarmos mais atentamente veremos que o Power BI tambem nao identificou corretamente os tipos de dados de cada coluna:

![image](https://user-images.githubusercontent.com/79231882/206516526-12e4f794-3806-4204-b648-78d2aaa7eb2b.png)


Vamos clicar em Fechar e Aplicar e ver o efeito disso antes de fazermos qualquer transformacao.

Vamos criar um grafico de linhas:

![image](https://user-images.githubusercontent.com/79231882/206516645-49184381-7a0f-4dda-85f7-130d207f0965.png)


Vamos verificar o valor de fechamento de acordo com a Data. Inserimos as Datas no eixo X e Close em Valores (eixo Y):

![image](https://user-images.githubusercontent.com/79231882/206516713-d26e59ab-4e2c-4464-a44d-8f59cb830d18.png)


Temos um grafico que nao corresponde com as variacoes nos precos de fechamento das acoes a cada dia.

Como identificou Close como texto ele nao permite realizar somatorio, como podemos ver esta opcao nao disponivel aqui:

![image](https://user-images.githubusercontent.com/79231882/206516802-f23f48f4-ecb4-4daa-af4d-afeeb624f8c3.png)


Vamos voltar em Transformar Dados. Vamos clicar em Close (em seu tipo de dado) e escolher alterar para decimal:

![image](https://user-images.githubusercontent.com/79231882/206516869-fcf1bd10-596d-43ad-a716-9faf6cb26677.png)


Coluna alterada, importante observar que sobrescrevemos os dados existentes:

![image](https://user-images.githubusercontent.com/79231882/206516959-0f6e3e2b-3b91-4c4c-bcc7-f728134cc115.png)


Caso tivessemos cometido algum erro, bastava clicar neste “X” para desfazer esta acao:

![image](https://user-images.githubusercontent.com/79231882/206517028-fd6be080-7c69-412a-8cef-7ea570881f0f.png)


Apos tentar aplicar aparecera esta mensagem de erro:

![image](https://user-images.githubusercontent.com/79231882/206517097-6a5ce2d2-d55f-4052-a020-efab9cc91b0e.png)


Vemos que na linha 101 ele nao conseguiu converter texto para numero decimal:

![image](https://user-images.githubusercontent.com/79231882/206517158-79f328df-f3cb-4e71-aea1-ffed05e52716.png)

![image](https://user-images.githubusercontent.com/79231882/206517197-8d740009-0276-40b9-a3cf-7e1b6d178baf.png)


Clicamos em remover linhas com erros. Nao perderemos nenhum dado com esta acao, pois esta a linha apenas contem a definicao de cada coluna:

![image](https://user-images.githubusercontent.com/79231882/206517282-554994c7-d2d4-4190-8602-5393462a0b3d.png)


Fechamos e aplicamos a transformacao. 

Agora podemos ver que temos a opcao soma para a variavel do eixo Y disponivel, clicamos la:

![image](https://user-images.githubusercontent.com/79231882/206517363-4cdcca9d-70ea-4df7-86ce-915b937b62b1.png)


E ai temos nossa serie temporal com os precos das acoes da AMD ao longo do tempo:

![image](https://user-images.githubusercontent.com/79231882/206517476-6c12e5ed-71cc-4a1d-a2af-bd1291999b64.png)

Podemos ver que as acoes da AMD vem caindo ao longo deste ano.


Mas sera que o grafico esta correto? Essa informacao realmente bate com o que vem ocorrendo com o preco de fechamento das acoes da AMD?

Algo chama a atencao em nossos dados. Podemos ver que o campo de Data nao apresenta hierarquia, o que eh padrao no Power BI quando ele detecta um campo de Data:

![image](https://user-images.githubusercontent.com/79231882/206517600-05ba5569-cccb-47cd-9b7c-aa11afd485d9.png)


Vamos voltar ao Power Query. Vemos que a coluna a Data esta identificada como uma string e isso nao esta correto:

![image](https://user-images.githubusercontent.com/79231882/206517699-5ae9ddff-e23f-466d-ae31-947cef7c54bc.png)


Vamos substituir a coluna Data para tipo Data:

![image](https://user-images.githubusercontent.com/79231882/206517831-bebdb442-d074-4172-a358-1c1643723fac.png)

![image](https://user-images.githubusercontent.com/79231882/206517883-cd183fdf-d238-4faa-b1d8-6b826c766ae4.png)


Fechamos e aplicamos a transformacao. Veremos o mesmo que obtivemos com o campo Close:

![image](https://user-images.githubusercontent.com/79231882/206517956-4aec6be6-25b9-4fc8-854a-69e7aa03b22c.png)

Isso era esperado porque esta linha possui apenas textos em cada uma das colunas.

Removeremos esta linha:

![image](https://user-images.githubusercontent.com/79231882/206518057-a2780cb3-9037-4e84-a0d0-0872606fe7b5.png)

![image](https://user-images.githubusercontent.com/79231882/206518089-8c2c0868-2cb3-4662-8778-03bfb5b83ae4.png)


Nosso grafico parece correto agora. Tambem observamos que apos a transformacao temos agora uma hierarquia no campo Data, o que esta correto:

![image](https://user-images.githubusercontent.com/79231882/206518152-993f6e12-317e-4e30-9445-8a8273326ebc.png)


Vamos retornar ao power query. Faremos as seguintes alteracoes:

- open: muda para decimal
- high: muda para decimal
- low: muda para decimal

Apos aplicado veremos a mesma mensagem de erro. Vamos corrigi-la da mesma forma:

![image](https://user-images.githubusercontent.com/79231882/206518255-48713dbb-7754-41b2-bd16-d7db9edab5ca.png)

Podemos ver que nossos campos foram alterados (possui um sinal de somatorio), indicando que podemos fazer calculos com este campos:

![image](https://user-images.githubusercontent.com/79231882/206518323-693e5fbf-5477-4aab-9ba5-e57ed5a1fe55.png)


Vamos pegar a coluna de cotacao maxima, minima e de abertura e levar para o nosso grafico:

![image](https://user-images.githubusercontent.com/79231882/206518407-86af96d2-f0a2-4eb7-9990-2d45d3f93840.png)


Vamos formatar nosso grafico neste menu:

![image](https://user-images.githubusercontent.com/79231882/206518509-74a36486-e118-432a-a63a-52569ee65692.png)

Alteramos e configuramos o titulo desta visualizacao:

![image](https://user-images.githubusercontent.com/79231882/206518582-9d7cd431-4706-46c4-b23e-5beedaacdeff.png)


Da forma como o grafico foi construido neste momento ele representa informacoes estaticas. 

O Power BI baixa os dados, os coloca em uma especie de buffer e entao alimenta o grafico. Caso abrissemos o grafico amanha teriamos apenas um grafico mostrando a evolucao das cotacoes ate o dia em que ele foi gerado.

As atualizacoes nao sao feita sem que seja feita uma configuracao. 

Ao passarmos o mouse sobre a Tabela e clicarmos nos 3 pontos a direita abre-se um menu suspenso:

![image](https://user-images.githubusercontent.com/79231882/206518667-c1517757-204d-4a4c-b13b-b0ab07dbd28f.png)


Quando clicamos em atualizar dados ele ira atualizar com esta acao manual:

Podemos clicar em analise incremental:

![image](https://user-images.githubusercontent.com/79231882/206518750-f48a5601-7de3-4fee-961d-7c05f48c2e8b.png)


Abre-se esta tela:

![image](https://user-images.githubusercontent.com/79231882/206518830-3ec55833-e86f-40a5-add2-48b66f0f4b12.png)

Vemos que esta opcao nao eh oferecida para o Power BI desktop:

![image](https://user-images.githubusercontent.com/79231882/206518935-ca21c1e5-02c2-4225-846a-f43523a40c18.png)

Para fazer esta acao teriamos que ter acesso ao Power BI Server. Publicariamos este grafico na nuvem e a partir de la acionariamos esta opcao de atualizacao incremental (a atualizacao somente pode ser feita no ambiente cloud, a Microsoft bloqueia esta acao no desktop).


![image](https://user-images.githubusercontent.com/79231882/206519018-0ecea146-860d-44b1-900f-75b9ade1669e.png)
