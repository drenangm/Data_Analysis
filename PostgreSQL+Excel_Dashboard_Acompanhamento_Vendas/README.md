# Definicao do Problema

Criar um dashboard de vendas com os principais indicadores de desempenho e com o principais drivers dos resultados do mes.


## Modelo do dashboard com os resultados que deverao ser gerados:

![image](https://user-images.githubusercontent.com/79231882/207404071-68e64922-0a8e-41ea-a9bb-3147c97fce53.png)

- **Grafico com a receita:** mostra a evolucao da receita e do ticket medio dos veiculos comprados no ecommerce. Nele eh possivel vermos se ha crescimento mes a mes e se isso eh um efeito do ticket medio, ou seja, as pessoas estao adquirindo veiculos mais caros e com isso ha impacto de crescimento na receita. No exemplo, o ticket vem se mantendo estavel mas a receita vem seguindo uma tendencia de crescimento gradual, possivelmente existe outro fator relacionado ao crescimento de receita.

- **Grafico com os Leads:** mostra a evolucao do numero de leads mes a mes e da conversao deles no funil de vendas, ou seja, qual foi a conversao de lead pra contrato pago no funil. Vemos uma evolucao bastante expressiva de leads chegand no topo do funil e tambem vimos um efeito combinado do aumento da conversao destes leads, ou seja, pro mesmo numero de leads entrando no topo do funil temos um maior numero de vendas sendo realizadas.

- **Grafico com o mapa de vendas por Estado:** pode-se observar uma grande predominancia do volume de vendas no Estado de SP.

- **Grafico com o comparativo de vendas por marcas no mes (top 5 com numero absoluto)**

- **Grafico com o numero de vendas por loja no mes (top 5 lojas)**

- **Grafico com o mapeamento do numero de vendas ocorridas por dias da semana**


Em resumo, o dashboard mostra:

→ dois graficos que mostram o desempenho do ecommerce mes a mes

→ quatro graficos que mostram os principais drivers de crescimento de vendas no ultimo mes

 Nos arquivos existe um template contendo o dashboard acima, sem os dados plugados ainda.

Os dados serao gerados conforme formos construindo as queries.

![image](https://user-images.githubusercontent.com/79231882/207404831-c456d158-9c18-4802-aff3-468e4f1d43f3.png)


Na aba resultados temos varias caixas no formato dos resultados que iremos puxar para o dashboard. Estes resultados irao atualizar automaticamente o dashboard:

![image](https://user-images.githubusercontent.com/79231882/207404930-3a70058f-e138-43fb-89fa-baa76b556af6.png)


Na aba queries ficarao documentadas as queries que serao desenvolvidas neste projeto:

![image](https://user-images.githubusercontent.com/79231882/207405020-866e7e86-44da-4580-9dbf-3f24e0466504.png)

Iremos criar uma query contendo: receita, leads, conversao e ticket medio mes a mes

Iremos criar uma tabela contendo as seguintes colunas:

- mes

- leads (#)

- vendas (#)

- receita (k, R$)

- conversao (%)

- ticket medio (k, R$)


**Query 1:**

Vamos comecar selecionando a tabela sales.funnel e as variaveis visit_page_month e sua respectiva contagem, iremos agrupar e ordenar por visit_page_month, mas esta coluna ainda nao existe, precisaremos calcular ela.

Para calcular iremos utilizar o recurso DATE_TRUNC. Transformaremos o date_trunc para date para removermos o horario do formato da data.

![image](https://user-images.githubusercontent.com/79231882/207405270-70918063-76b9-4336-9860-90ebce2392f8.png)

![image](https://user-images.githubusercontent.com/79231882/207405320-0459967a-0593-4d27-a75e-a9a6169948a1.png)


Com isso resolvemos as colunas mes e leads.


Pra calcularmos o numero de vendas e a receita gerada com as vendas iremos puxar da tabela sales.funnel a data de pagamento (paid_month) e contaremos quantos pagamentos foram feitos naquele mes (contamos todos os paid_date naquele periodo).

Tambem precisaremos criar uma coluna com o calculo da receita gerada no mes mas para isso precisaremos puxar alguns dados que estao na tabela sales.products. Vamos fazer um JOIN com esta tabela.

A receita sera calcula atraves de uma funcao agregada, no caso a funcao soma. Nela faremos a soma dos precos multiplicados pelo valor percentual adicionado dos descontos concedidos, ou seja, “1+discount”.

Na existe uma coluna chamada “paid_month”, iremos cria-la. Vamos mais uma vez utilizar o DATE_TRUNC.

Mas queremos contabilizar receitas somente quando o pagamento tiver sido realizado, para isso iremos incluir um filtro com o WHERE em que iremos chamar apenas as linhas em que a data de pagamento forem diferentes de null.

![image](https://user-images.githubusercontent.com/79231882/207405474-6dada347-7c25-4fd6-9768-60aafb5c1f15.png)

![image](https://user-images.githubusercontent.com/79231882/207405534-e76737aa-55b3-48b3-a646-7c818356fdcf.png)


Para fazer o calculo dos valores que irao para as colunas conversao e ticket medio precisaremos dividir o page_count pelo visit_page_count o que significa que sera necessario juntar as duas queries anteriores.

Podemos fazer isso atraves de uma sub-query .

Iremos pegar a query de contagem de visitas mensais ao ecommerce e transforma-la em uma sub-query:

![image](https://user-images.githubusercontent.com/79231882/207405660-1670e772-e87b-4a9f-9732-af97f26f17df.png)

Chamaremos a sub-query criada de leads:

![image](https://user-images.githubusercontent.com/79231882/207405784-bebdb01e-9cfe-4c8e-b5f5-132e4c4f63a9.png)


E a outra query, que sera convertida em uma nova sub-query, sera nomeada como payments:

![image](https://user-images.githubusercontent.com/79231882/207405873-2fc4a89e-2df0-4f84-b1ab-9b70d38e4b89.png)

Sub-query:

![image](https://user-images.githubusercontent.com/79231882/207405978-82831890-a683-4665-8436-df9d6e135990.png)

Agora com estas duas sub-queries criadas poderemos chama-las em uma query posterior, em que iremos fazer um JOIN entre leads e payments pelas colunas visit_page_month de leads e paid_month de payments.

Na query iremos selecionar as colunas visit_page_month, visit_page_count (ambas da tabela leads), coluna paid_count da tabela payments. 


Continuando no SELECT, iremos selecionar mais tres colunas que serao calculadas: 

- receita, que teremos que fazer um calculo apenas para converte-la na unidade de milhares

- conversao, que esta representada pela divisao entre o paid_count (convertido para numero decimal) e visit_page_count (tambem convertido para decimal)

- ticket medio, que eh a receita dividido pelo numero de vendas dentro do mes, iremos pegar de payments a receita e dividir pelo paid_count, pegaremos este resulta e dividiremos por mil para ajustar a unidade


A query ficara da seguinte forma:

![image](https://user-images.githubusercontent.com/79231882/207406141-6f9a219c-964a-4aba-bfc1-5e0c3638bfb3.png)


E a query completa ficara assim:

![image](https://user-images.githubusercontent.com/79231882/207406278-e0fc379e-782c-4076-88f2-f3187aa5146f.png)


Resultado da query:

![image](https://user-images.githubusercontent.com/79231882/207406377-d4c3bb54-830f-4357-bd21-bdd73ac05f6c.png)


Conseguimos fazer a query 1, que gera os graficos 1 e 2. Ela tem 5 colunas e 12 linhas. 

Vamos pegar o resultado desta query e copiar e colar na aba de resultados.

Mas antes vamos clicar na parte do postgre que faz a copia:

![image](https://user-images.githubusercontent.com/79231882/207406487-1d381785-dd73-4d12-90e0-d2726c656d9a.png)

Na aba resultados no excel:

![image](https://user-images.githubusercontent.com/79231882/207406533-d5c15709-edd3-455c-a7a4-d4e8639b21b5.png)


Demos CTRL+C na tabela que criamos e damos CTRL+V na area da primeira tabela do primeiro grafico:

![image](https://user-images.githubusercontent.com/79231882/207406617-edf38792-83b6-4a01-be7c-702910014046.png)


Conferimos o dashboard como ficou:

![image](https://user-images.githubusercontent.com/79231882/207406699-f454f5e6-3c94-40b3-874a-b22dd08de11d.png)


Vemos que todos os dados foram preenchidos nos graficos 1 e 2, com os dados que geramos no postgres.

No primeiro grafico pudemos constatar que o no ticket medio na vem exercendo influencia sobre a receita, por ela vem crescendo de forma independente a variacao (ou nao) do ticket medio.

No segundo podemos observar que o numero de leads vem crescendo acompanhando tambem pelo crescimento da conversao destes leads, ou seja, os leads crescente vem ajudando a aumentar o numero de vendas de veiculos. Isto vem tornando o produto mais atrativo aos clientes.

Para fechar esta primeira parte iremos copiar esta query e cola-la na aba “Queries” do excel”

![image](https://user-images.githubusercontent.com/79231882/207406880-639e2fad-c732-46da-8b04-d7838df48899.png)


**Query 2:** Estados que mais venderam 


Colunas: pais, estado, vendas (#)


Pra montar o graficos do top 5 Estados que mais venderam, precisaremos montar uma query que retorne as seguintes colunas: pais, estado e numero de vendas.

Pra isso precisaremos cruzar os dados da sales.funnel com a sales.customers.

Apos fazer o JOIN entre esta duas tabelas iremos selecionar:

- qual o pais em que os clientes mora, mas nao temos esta informacao na tabela mesmo ja tendo esta certeza, portanto iremos adicionar esta informacao a nossa selecao, este eh um artificio que precisaremos utilizar para que o grafico que iremos gerar no dashboard fique adequado

- puxaremos a coluna estado de sales.customers

- faremos uma contagem de pagamentos vinda de sales.funnel, chamaremos esta coluna de vendas, em que so serao contabilizadas as vendas que se concretizaram no ultimo mes


Teremos que incluir um filtro em que paid_date tera que estar entre o primeiro e o ultimo dia do mes.

Precisaremos agrupar isso pelas colunas que nao sao agregadas, ou seja, pais e estado (precisamos lembrar que nao podemos agrupar nada que possui valores agregados).

**Observacao: no filtro WHERE colocamos a condicao de capturar os dados de Agosto/21, que eh o ultimo mes que consta nesta base de dados.**

![image](https://user-images.githubusercontent.com/79231882/207407093-1df04265-66b1-45d7-b2c2-c51720090b84.png)

![image](https://user-images.githubusercontent.com/79231882/207407143-8c8b5905-7c3c-49e2-b95b-2d981708cebf.png)


Esta query gera o grafico 3, em que eh mostrado o mapa com as vendas dos top 5 Estados com maior volume de vendas.

Copiamos para a segunda tabela no excel:

![image](https://user-images.githubusercontent.com/79231882/207407216-9690ddfb-0363-4449-8aee-74984466f4f2.png)

Veremos o grafico:

![image](https://user-images.githubusercontent.com/79231882/207407290-0a377e91-ffa3-4be2-a401-ba550bda57a1.png)


**Query 3:** vamos construir o grafico que gera as top 5 marcas mais vendidas no mes

Colunas: marca, vendas (#)

Para fazer esta query precisaremos juntar os dados das vendas realizadas la da sales.funnel e da marca do veiculo, que vem da sales.products

Vamos fazer um JOIN entre a tabela sales.funnel e a sales.products. Nesta juncao iremos selecionar a marca do produto, faremos um agrupamento pelas marcas e ordenaremos pelo numero de vendas com limite de 5.

Como queremos resultado apenas do ultimo mes, colocaremos no WHERE a condicao de filtrar somente o periodo de Agosto.

![image](https://user-images.githubusercontent.com/79231882/207407382-0390d9f3-15df-4e96-8f24-09c7488d57e0.png)

![image](https://user-images.githubusercontent.com/79231882/207407421-e5069227-b6a9-4ee4-8afc-f727d2511fc6.png)


Vamos enviar o resultado para o excel:

![image](https://user-images.githubusercontent.com/79231882/207407467-d6d58502-08d6-4c1c-9057-99678b817ba3.png)


E ver como ficou o grafico no dashboard:

![image](https://user-images.githubusercontent.com/79231882/207407526-aa806bca-2837-4dd1-8deb-d6a324dc0a5f.png)


Podemos ver o ranking das marcas mais vendidas no mes.

E migramos a query para a area de documentacao dentro do excel:

![image](https://user-images.githubusercontent.com/79231882/207407607-4941ecaa-e182-4739-897d-20d86955a113.png)


**Query 4:** vamos levantar as cinco lojas que mais venderam no mes

Colunas: loja, vendas (#)

As unicas diferencas em relacao a ultima query eh que iremos fazer um JOIN entre tabelas diferentes, no caso faremos entre a sales.funnel e a sales.stores

![image](https://user-images.githubusercontent.com/79231882/207407735-dbc2b32b-060d-43c0-b8c8-5cb00a4122a3.png)

![image](https://user-images.githubusercontent.com/79231882/207407793-652bd231-2e90-42f4-95e2-ea8f6f64593f.png)


Vamos enviar o resultado la para o excel:

![image](https://user-images.githubusercontent.com/79231882/207407857-699dcea9-22bd-46d6-b2de-f69ea38ba23b.png)


Grafico gerado no dashboard:

![image](https://user-images.githubusercontent.com/79231882/207407954-e08c088f-11cb-4dbe-a687-df0ff94310cf.png)


Codigo SQL migrado para documentacao:

![image](https://user-images.githubusercontent.com/79231882/207408037-58092ac1-0d21-4df5-99e1-c3e48d518969.png)


**Query 5:** iremos contabilizar o numero de visitas no mes ao site do ecommerce

Colunas: dia_semana, dia da semana, visitas (#)


A diferenca entre as colunas dia_semana e dia da semana eh que dia_semana sera um numero que vai de 0 a 6 (representando de domingo (0) a sabado (6)) e dia da semana sera um texto indicando exatamente o dia da semana.


Agora temos todos os dados na mesma tabela por isso nao precisaremos fazer nenhum tipo de JOIN.

Para pegarmos as informacoes de dia_semana, iremos utilizar a funcao EXTRACT com “dow”.

Para os dias da semana iremos utilizar o CASE WHEN em que colocamos as condicoes logicas para retorno e uma string com o nome do dia da semana.

Por ultimo faremos um count do numero de visitas. 

A razao de termos criado uma coluna “adicional” com o indice correspondente ao dia da semana foi para termos uma melhor ordenacao, sem ela uma ordenacao seguiria a ordem alfabetica das strings com os nomes dos dias e nao ofereceria a ordem correta, ficando estranho quando migrarmos a informacao para o excel.

![image](https://user-images.githubusercontent.com/79231882/207408269-50ba9878-a455-4ce3-a610-abaa085e5605.png)

![image](https://user-images.githubusercontent.com/79231882/207408314-97c88602-3c73-4f95-98c9-d622cd3f299e.png)

Migramos o resultado para o excel:

![image](https://user-images.githubusercontent.com/79231882/207408391-cfed6179-a724-4d6d-9a60-daa057666c55.png)

E checamos o dashboard:

![image](https://user-images.githubusercontent.com/79231882/207408461-2b57c997-b495-494b-8cbf-26b11d768e8b.png)


E documentamos a query:

![image](https://user-images.githubusercontent.com/79231882/207408530-abcedf82-ab4c-4749-a3d5-a8015c0dba3b.png)


Vemos que segunda e terca-feira sao os dias com maior movimentacao no site e, gradativamente, o movimento vai caindo ao longo da semana.


### Resolucao parte 2 - Graficos


Vamos entender como os graficos foram montados no dashboard.


Para o primeiro graficos, Receitas x Ticket Medio, precisaremos de 3 colunas:

- coluna Mes

- coluna Receita

- coluna Ticket Medio


Selecionamos cada uma delas com CTRL:

![image](https://user-images.githubusercontent.com/79231882/207408653-5fe45ca5-3182-42ca-ac8b-a8d12b3f8942.png)


Vamos em INSERT e LINE (para escolhermos o grafico de linhas (com a selecao feita):

![image](https://user-images.githubusercontent.com/79231882/207408736-f62bc3a6-c063-40ed-b13e-d6757e5fd9ce.png)

![image](https://user-images.githubusercontent.com/79231882/207408772-62e10787-5328-456d-9886-1ba498a7f937.png)


Ficaremos um grafico parecido ao que temos abaixo, mas vamos melhora-lo:

![image](https://user-images.githubusercontent.com/79231882/207408841-0c6a4b39-621d-4340-8bb9-96c62c7d85f7.png)


Clicamos com o botao direito nele e escolhemos a opcao “change chart type”:

![image](https://user-images.githubusercontent.com/79231882/207408899-9345f7c7-6338-4bc9-be46-79856329d264.png)


Selecionamos a opcao combo a esquerda da selecao:

![image](https://user-images.githubusercontent.com/79231882/207408967-7bdc8f56-1cd3-40d6-87df-797b6197f23f.png)


Selecionamos o secondary axis na caixa de selecao para adicionarmos o ticket medio ao grafico:

![image](https://user-images.githubusercontent.com/79231882/207409048-27c23bcd-c772-447b-a541-588314f242f7.png)


Ele ficara como abaixo:

![image](https://user-images.githubusercontent.com/79231882/207409119-ee787844-2aef-41c4-87f1-71ccac7dde27.png)


Formatamos o titulo para Receitas e clicamos nas barras para formatar elas:

→ editamos o gap entre elas para 100%

![image](https://user-images.githubusercontent.com/79231882/207409230-62d37395-5e74-4ce4-9865-684f4b3144ef.png)


→ adicionamos os labels em cada barra

![image](https://user-images.githubusercontent.com/79231882/207409298-1c025ec1-063f-4ba9-b477-6d2b1eafe539.png)


Vamos editar a linha do teicket medio, selecionamos ela e vamos acessar o menu de formatacao do lado direito:

![image](https://user-images.githubusercontent.com/79231882/207409448-e4d20d0b-e62f-498c-8a50-873b6e340691.png)


Editamos a cor e clicamos em chart elements para adicionarmos os labels:

![image](https://user-images.githubusercontent.com/79231882/207409565-d9375d54-a204-4df2-b6a0-681b0e167540.png)


Tambem configuramos o posicionamento dos labels e adicionamos uma cor de fundo:

![image](https://user-images.githubusercontent.com/79231882/207409676-1b224c49-7c0e-4112-99e8-20cc1a3dfded.png)


Vamos formatar a area do grafico, clicamos na area dele, vamos ao menu do lado direito e jogamos a legenda para cima:

![image](https://user-images.githubusercontent.com/79231882/207409763-c7a41082-3a19-463f-93de-03d69fb26de2.png)


Alteramos a cor da area do grafico para um cinza claro e adicionamos bordas arredondadas (fillet):

![image](https://user-images.githubusercontent.com/79231882/207409911-d2c08bee-9510-4f2f-bace-00fa454c138d.png)


Ficamos com esta versao final do grafico:

![image](https://user-images.githubusercontent.com/79231882/207409993-c2864180-7788-4fbc-9296-adf8658c482f.png)


Para o **grafico 2**, contendo os leads nos copiaremos o grafico anterior e nos ajustaremos os dados que alimentarao este grafico.

Clicamos nas barrinhas azuis e arrastamos os dados para a serie correspondente a Leads, assim como o titulo:

![image](https://user-images.githubusercontent.com/79231882/207410069-52553c50-19e3-4801-8ffc-e9232bff9065.png)


Na linha iremos trocar o ticket medio para conversao:

![image](https://user-images.githubusercontent.com/79231882/207410138-dd09482a-01f3-4af6-99fb-2d495bc69822.png)


Mas o grafico ficou desformatado, para reformatar clicaremos no primeiro grafico e damos CTRL+C, depois vamos ao segundo grafico e clicamos em colar especial (formato):

Ficamos com esta versao final do grafico:

![image](https://user-images.githubusercontent.com/79231882/207410221-b3a08ded-6d99-4714-9655-091bb122b3b6.png)


Vamos ao grafico 3 com as top 5 marcas mais vendidas, vamos na tabela e selecionar os dados:

![image](https://user-images.githubusercontent.com/79231882/207410310-a8f8c231-ef43-4a84-9850-4af5acb7dc7e.png)


Vamos selecionar o grafico de barras na horizontal em 2D:

![image](https://user-images.githubusercontent.com/79231882/207410384-93ad8cdd-74cf-4444-b611-75e5635bda35.png)


Esta eh a versao final do grafico, em que apenas mudamos a cor de fundo da area do grafico, a cor dos labels e posicionamento deles em inside end:

![image](https://user-images.githubusercontent.com/79231882/207410455-c98ab0bf-a263-4ed3-92e5-f75b3f06bcb9.png)


**O grafico 4** com as top 5 lojas possui a mesma formatacao, somente iremos puxar os dados que fazem parte dele:

Grafico formatado:

![image](https://user-images.githubusercontent.com/79231882/207410523-3d3bcc95-2bda-4465-8e1b-c8c794b50f7e.png)


**Grafico 5**, eh um grafico de barras porem na vertical.

Vamos selecionar os dados deste grafico (nao selecionamos a primeira coluna):

![image](https://user-images.githubusercontent.com/79231882/207410607-4cb24d21-b08e-42c9-ae3b-bb95c9e7e4aa.png)


Vamos em insert e selecionamos o grafico de barras na vertical:

![image](https://user-images.githubusercontent.com/79231882/207410681-2c85ed6e-0566-4700-8cfa-dcbe239fe3ba.png)


Grafico finalizado:

![image](https://user-images.githubusercontent.com/79231882/207410763-ff892310-a145-46ef-8198-e45dc0eb2f4f.png)


**Observacao:** Como minha versao do excel, no momento em que estava gerando esta visualizacao nao tem a opcao de construir grafico de Mapas (eh possivel fazer no Power BI) eu montei um grafico de barras na vertical:

![image](https://user-images.githubusercontent.com/79231882/207410967-364e4b4b-24e0-40db-bf26-efd78a619b14.png)
