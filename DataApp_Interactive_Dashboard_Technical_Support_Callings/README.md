# Explicação sobre como foi construído o dashboard

Este projeto usaremos o Dash, que juntamente como o framework Flask permitirá construir um Dashboard Interativo 100% via web.  Os dados usados neste projeto são fictícios, mas representam exemplos de chamados de suporte. Os dados podem ser coletados de sistemas de atendimento de suporte.


O dashboard foi construído fazendo uso da biblioteca Dash e foi implementada por meio da construcao de um app.

Utilizaremos tambem a extensao dash bootstrap components.

![image](https://user-images.githubusercontent.com/79231882/203078978-0e220199-f5f3-4983-94ca-c5e9957b66ce.png)


Alem de outras caracteristicas, permitira que possamos alterar o tamanho da pagina web mantendo o layout. Isso permite que o layout se ajuste ao mais diversos dispositivos  (celular, monitores grandes, desktops, etc).

![image](https://user-images.githubusercontent.com/79231882/203079078-77c1256c-86a4-4960-b4e1-e485cedb3ebd.png)


Os arquivos bootstrap e custom.styles contem alguns arquivos em CSS que serao colocados na aplicacao.


O arquivo JSON mapeamento_campos_dataset serve para fazer o mapeamento entre os nomes das colunas do arquivo de dados e os nomes das colunas na nossa aplicacao no dashboard.

Isso sera feito porque queremos oferecer ao usuario do dashboard a oportunidade de alterar os labels.  

Por exemplo: existe uma coluna chamada “data_criacao” em que o usuario nao deseja utilizar este nome, ele prefere utilizar “data_abertura”. Com isso permitimos que o usuario possa fazer este tipo de alteracao.


O conjunto de dados esta no arquivo dataset (dados ficticios).


Os arquivos app_element_git, constant_git, data_operations_git e navbar_git foram desenvolvidos em Python e contem barra de navegacao, operacoes de dados, arquivo com algumas constantes (alguns termos nao serao alterados na aplicacao, servindo como uma especie de dicionario) e mais um arquivo com elementos da app.


Tambem existe um arquivo “__init__.py” completamente vazio, indicando que esta pasta é um modulo Python, ou um pacote Python com uma serie de funcoes modularizadas.


Temos tambem os arquivos dashboard_git, overview_git e settings_git que contem os modulos em python com scripts para cada uma das tres paginas que farao parte da aplicacao.


Na nossa aplicacao nao existem arquivos html e css, quem ira construir a aplicacao sera o Dash. Iremos abrir funcoes desenvolvidas em Python, iremos indicar o que queremos e na hora em que executar o programa o Dash monta as paginas html que compõem a aplicacao.


Temos o arquivo [app_git.py](http://app_git.py) para fazer a execucao da aplicacao e o [dataapp_git.py](http://dataapp_git.py) que é o ponto de partida. A partir dele chamamos os demais modulos e assim a aplicacao é executada.


Faremos uma execucao previa do dashboard para nos familiarizarmos com as funcionalidades que ele ira fornecer:
![image](https://user-images.githubusercontent.com/79231882/203081147-0d4d4489-3d5f-4eb6-a8bd-3d157e48e9f9.png)


Copiamos o endereco fornecido pela aplicacao:
[http://0.0.0.0:3000/](http://0.0.0.0:3000/)


A aplicacao não funcionou no endereço indicado pela aplicacao> este endereco foi inserido dentro de um parametro da funcao run_server, parametro host.


Iremos editar para o endereco 127.0.0.1 e ver se funciona.


![image](https://user-images.githubusercontent.com/79231882/203081277-fdfd9e33-9c6a-4d17-a24a-3b9efb7aa3cb.png)


![image](https://user-images.githubusercontent.com/79231882/203081673-cedacd2e-3dc5-42cb-a2c3-03a007f5c47b.png)


Aplicacao em funcionamento no endereco http://127.0.0.1:3000/:

![image](https://user-images.githubusercontent.com/79231882/203081790-90b5be8d-e55d-4c12-a497-3d105381e51a.png)

No menu lateral a esquerda ao acessarmos a pagina de help, é retornado um erro:
![image](https://user-images.githubusercontent.com/79231882/203081900-2aa5aa96-d38d-4579-8e15-52147a783f9f.png)


É desta forma que a app foi desenvolvida, não há problema aqui, isso faz parte da app. A pagina de help não foi desenvolvida.


Nas legendas laterais do grafico de Chamados de Suporte podemos fazer a selecao das opcoes que queremos que aparecam no grafico:


![image](https://user-images.githubusercontent.com/79231882/203082002-9dad4701-2203-4e3c-81a7-5ee0f53be93c.png)


No caso, selecionamos apenas as 3 primeiras.

O mesmo pode ser feito para os graficos de rosca e de pizza abaixo:

![image](https://user-images.githubusercontent.com/79231882/203082090-5393eca5-d29a-41f1-9182-3b1ecd1d2fcb.png)


![image](https://user-images.githubusercontent.com/79231882/203082156-cd781b31-038f-4641-a8b0-544cdb26ca0a.png)

Em Visao Geral podemos tambem fazer seleçõess. Abaixo fizemos seleção de chamados do colaborador 68:

![image](https://user-images.githubusercontent.com/79231882/203082288-b3aca0a3-2dfa-4db7-9cdc-a08846ee9d66.png)

E tambem para chamados atendidos, chamamos para o colaborador 09:

![image](https://user-images.githubusercontent.com/79231882/203082380-c22e6873-6704-4214-9fc5-45d95f0e9ec9.png)

Em configuracoes podemos mudar o formato de Data e mudar o Titulo da Coluna:

![image](https://user-images.githubusercontent.com/79231882/203082505-7498a360-77a4-4863-b8ba-d00de3da5442.png)


Se alterarmos o “Mapeado Para” para um nome de coluna de nossa preferencia, o arquivo JSON que possibilita esta edicao é alterado, guardando a mudanca e sua correspondencia com o dataset de origem. 


Vamos comecar a construir o dataapp_git.py. 

Começaremos com as bibliotecas que iremos utilizar.

![image](https://user-images.githubusercontent.com/79231882/203082657-a7e186df-012e-4590-9775-adad14707e28.png)

Em seguida fazemos a leitura dos arquivos de configuração das constantes:
![image](https://user-images.githubusercontent.com/79231882/203082851-dd8a524a-742c-4abf-b94e-1469acf47598.png)

Aqui trazemos tudo que nao sera alterado ao longo da execução da aplicação.

Em seguida usamos a funcao Div do Dash que simplesmente permite configurarmos uma divisão HTML em nosso dashboard:

![image](https://user-images.githubusercontent.com/79231882/203083202-6ad679e2-7178-4411-a564-b08314fbf2ca.png)


Em seguida fazemos o mesmo para configuracao da secao do layout:
![image](https://user-images.githubusercontent.com/79231882/203083294-f6779a4e-bcb3-4686-be0f-023094237112.png)

Depois temos uma funcao “display_page” que faz um callback com Dash.

Essa função verifica a pagina que estamos carregando (dashboard, overview ou settings). 

Em cada uma das paginas chamaremos a funcao modularizada get_layout (associada a cada um dos modulos).

Dentro do diretorio temos desenvolvidas as três paginas, em cada um destes modulos das paginas temos uma funcao get_layout

Vemos que o help esta dentro do laço “else” que nao esta desenvolvido. Ele sera tratado com codigo HTML. Usamos H1 para o titulo, Hr para a linha e o P para o paragrafo.

![image](https://user-images.githubusercontent.com/79231882/203083436-c236691e-0957-414b-991a-2e44faf6029c.png)

Criamos o executor da aplicacao com o host alterado para o endereço que funcionou no teste previo:

![image](https://user-images.githubusercontent.com/79231882/203083525-ac83377d-8699-4f3f-9ec8-09fe7a8ff1ab.png)



Vamos agora construir o modulo app (no meu caso, app_git).

Importamos o dash, criamos uma instância do dash, chamada de app, colocamos o parametros necessarios para que o layout do aplicativo possa ser responsivo.

![image](https://user-images.githubusercontent.com/79231882/203083643-c5541017-917c-4df2-8c09-6be8b95d9f2d.png)


# Construcao das paginas da aplicacao


Vamos construir a pagina dashboard:

- importacao das bibliotecas

![image](https://user-images.githubusercontent.com/79231882/203083794-fe874b2a-2def-4133-ae40-1e85efb9784f.png)

→ traceback: formata mensagem de erro via HTTP

Vamos criar uma funcao get_layout, que é chamada la no dataapp.

Inicialmente vamos tentar executar a funcao (laço “try”), se ocorrer um erro formatamos o erro com o modulo Jumbotron e mostramos ao usuario.

→ Carregamos os dados com o modulo data.operations;

→ Fazemos agrupamentos de colunas, estas colunas vem do modulo constant (apenas naquele modulo eh que podemos realizar alteracoes);
![image](https://user-images.githubusercontent.com/79231882/203083967-a2d3caa2-aa4c-4aa9-97cd-6396773d40c3.png)


Vamos criar agora um container a partir do modulo dbc (dash bootstrap components).

Utilizaremos isso para termos responsividade na aplicacao (layout se ajusta ao tamanho da janela do browser):
![image](https://user-images.githubusercontent.com/79231882/203084152-0947ced8-de81-4b19-b4ef-66c1df3cbda4.png)

![image](https://user-images.githubusercontent.com/79231882/203084220-7521a1cd-debb-4b62-bd55-f400d23d5588.png)


E seguida definimos as duas linhas do container em que:

→ na primeira linha ira o grafico de linha

→ na segunda linha irao os graficos de rosca e de pizza

→ na primeira linha teremos uma coluna, pois sera acomodado apenas um grafico

→ na segunda linha teremos duas colunas, para dois graficos


![image](https://user-images.githubusercontent.com/79231882/203084308-ce4dbf22-fd59-4b3b-82a0-c28b8767bf58.png)


Criamos o laço “except” para caso o enlace do Container apresente algum erro:

![image](https://user-images.githubusercontent.com/79231882/203084393-0d7ab07f-5910-44c5-9c49-1b8387e744f1.png)


**Vamos a pagina overview**

Ela seguira estrutura parecida ao que foi feita na pagina dashboard, com mudanca na formatacao do layout.

![image](https://user-images.githubusercontent.com/79231882/203084526-37215f8f-4388-47c9-86b0-10f2bd209d63.png)
![image](https://user-images.githubusercontent.com/79231882/203084583-db5fe691-84bf-4ae0-9879-1798aae16f41.png)


# Pagina settings

Mantemos a mesma estrutura de Cards.

Agora ao invés de criarmos um DashTable iremos criar uma DataTable que na pratica ira carregar o arquivo JSON que contera as eventuais modificacoes de nomes feita pelo usuario.

![image](https://user-images.githubusercontent.com/79231882/203084739-a536602e-3d41-405c-aa69-e0e22baf2683.png)

![image](https://user-images.githubusercontent.com/79231882/203084796-ac02460b-fb8e-4439-8178-7f957e3d82f7.png)


Como demos opcao de configurar para o usuario, precisamos criar um callback com Input e Output e apos isso uma funcao para quando o usuario clicar no botao.

![image](https://user-images.githubusercontent.com/79231882/203084895-2f52ea4d-ee75-43db-905c-18d54fa03384.png)



Vamos agora para o diretorio Modulos, comecando pela “constant_git.py”.

Aqui apenas definimos os parametros que serao “estaticos” na nossa app.

Definimos os caminhos para alguns arquivos externos:

![image](https://user-images.githubusercontent.com/79231882/203085104-a80406aa-0c20-4c55-b0cc-bd567811e8e0.png)


Definimos a barra lateral:

![image](https://user-images.githubusercontent.com/79231882/203085195-1965ba8c-f7f3-46e5-9f7f-ffd1ab70433d.png)


Formatações para os dados no dashboard:

![image](https://user-images.githubusercontent.com/79231882/203085262-02bdebcf-412a-4f35-aa53-3ba78d26177f.png)


Inicializamos os nomes de coluna no dataset:

![image](https://user-images.githubusercontent.com/79231882/203085342-ec7e93f8-6b53-4c69-a7cc-df3d981e98ed.png)


Nomes de coluna no arquivo csv:

![image](https://user-images.githubusercontent.com/79231882/203085420-79b69d55-55e8-4f94-89fd-1b98f92c4313.png)


Criamos um dicionario em Python para mapeamento dos campos para o caso em que o usuario fizer alteracao ele conseguir encontrar a qual campo se refere a alteracao:

![image](https://user-images.githubusercontent.com/79231882/203085506-167f921d-d518-4359-982f-c62b7f260b19.png)


Definimos o formato das datas:

![image](https://user-images.githubusercontent.com/79231882/203085563-31f0cf72-8209-47b5-9600-e3defb762eac.png)


Variaveis customizadas:

![image](https://user-images.githubusercontent.com/79231882/203085627-908df783-d77b-4657-a69f-b2b33fdede1b.png)


Criamos uma funcao chamada read_config. Esta funcao define variaveis como globais porque desta forma conseguimos utilizar estas variaveis a partir de outros scripts.

![image](https://user-images.githubusercontent.com/79231882/203085695-db1051a0-ecca-41ab-9456-40700beb9941.png)


Carregamos o arquivo de mapeamento (JSON). Fazemos o mapeamento dos campos. Quando o usuario salvar alguma mudanca ele modificara o novo arquivo JSON:

![image](https://user-images.githubusercontent.com/79231882/203085752-609e9a7f-6bd4-43b7-810c-853261b617b1.png)


Fazemos a configuracao dos objetos do arquivo JSON:

![image](https://user-images.githubusercontent.com/79231882/203085817-9ee64429-f298-447f-9c68-e53113ba0973.png)


Quando o usuario fizer uma alteracao no arquivo JSON ele ira salvar o novo arquivo JSON. A funcao que possibilita esta acao por parte do usuario esta no modulo “data_operations_git.py”:

Vamos a ela, iniciando o carregamento dos pacotes:

![image](https://user-images.githubusercontent.com/79231882/203085942-810e9765-e278-45b4-91a0-5c3c00537388.png)


Funcao que gera o dataset:

→ primeiro eh carregado o dataframe, a aplicaca vai demorar um pouco mais para inicializar porque ao iniciarmos o dashboard ela ira carregar os dados, em compensacao apos carregado os dados, eles persistem em memoria e os graficos serao gerado com maior velocidade. Caso o arquivo csv que contem os dados sofra atualizacao, é preciso reinicializar a app

→ eh feito o mapeamento das colunas, em que alteramos os nomes das colunas no proprio dataframe

→ em seguida eh feita a formatacao das colunas com as datas

→ apos formatar as colunas adicionamos elas ao dataframe

→ habilitamos um filtro para status aberto ou fechado, dependendo do status que temos no arquivo csv

→ ao fim retornamos o dataframe completamente carregado

![image](https://user-images.githubusercontent.com/79231882/203086023-7c7b989b-337c-4db9-881f-0c440d5f2703.png)


Na sequencia temos funcoes que retornam status aberto ou fechado do chamado:

![image](https://user-images.githubusercontent.com/79231882/203086096-81c79ff1-d98f-4492-95c6-d2cc019e0350.png)


Funcao que carrega as configuracoes e prepara o dataframe, retornando o dataframe totalmente preparado com “id Coluna”, “Nome Coluna” e “Mapeado Para”, conforme abaixo:

![image](https://user-images.githubusercontent.com/79231882/203086178-b23aa9d2-28ff-41a3-9849-37736a63969b.png)

![image](https://user-images.githubusercontent.com/79231882/203086241-eeaa8da5-aa2f-4273-8421-0e8b03da158f.png)


Funcao que grava o arquivo de mapeamento no modulo JSON:

![image](https://user-images.githubusercontent.com/79231882/203086334-d27ebd3a-3115-4274-828c-53d233dfafc3.png)



Vamos a pasta config para desenvolver a pasta de mapeamento dos campos do dataset.

Este arquivo eh o que sera carregado na pagina de configuracoes do dashboard:

![image](https://user-images.githubusercontent.com/79231882/203086427-d57f7d30-9f0a-4565-8ce5-320f94f11a35.png)

![image](https://user-images.githubusercontent.com/79231882/203086482-17181b3d-787b-4e02-968a-219d3faaba1e.png)


É aqui que oferecemos ao usuario a opcao de alterar os nomes das colunas para que ele possa visualizar a informacao de forma mais amigavel.

Vamos olhar o arquivo com os dados dentro do diretorio dataset:
![image](https://user-images.githubusercontent.com/79231882/203086612-366b17bb-2d95-499d-a9ff-6417c02c3a78.png)


Nos carregamos estes dados e, apos isso, agrupamos eles.

![image](https://user-images.githubusercontent.com/79231882/203086671-af09e3b1-f0c1-4b74-bf11-c490a1bce117.png)


Em caso de alteracao deste dataset, todo mapeamento precisará ser alterado para que as mudancas possam ser refletidas no dashboard.

Vamos checar em assets, quais arquivos estamos utilizando.


Os arquivos com css:

→ bootstrap_git.min.css
![image](https://user-images.githubusercontent.com/79231882/203086835-29ac1964-229d-4cfc-9c47-b5e4be0cae8a.png)


Este é um arquivo open source disponibilizado pela equipe do twitter que nos permite ter um dicionario em CSS. Não precisamos criar, apenas utilizamos como um dicionario padrao. 

Em cima dele, construimos nosso arquivo CSS com o arquivo custom.styles.css

![image](https://user-images.githubusercontent.com/79231882/203087228-e4c5fd6b-43ac-438a-b71b-940a3a619874.png)


Nele constam configuracoes especificas em CSS para a nossa aplicacao.

Vamos aos demais arquivos em modulos, com o app_element_git:

![image](https://user-images.githubusercontent.com/79231882/203087397-b86c857d-cf31-428c-8062-45971dc0fd3e.png)


Neste modulo construimos a funcao para gerar a dashtable: generate_dashtable.

Podemos ve-la gerada abaixo:
![image](https://user-images.githubusercontent.com/79231882/203087487-b3182ab7-e442-4b92-baac-f99166f7959a.png)


Criamos a dashtable chamando a datatable do pacote dashtable, que foi importado neste modulo.

![image](https://user-images.githubusercontent.com/79231882/203087577-d80cba65-5072-4151-be0a-96e7ec902199.png)


Basicamente os parametros que utilizamos na dashtable sao de formatacao.

Vamos ao proximo modulo, em que voltamos ao data_operations_git.py em que trabalhamos, processamos e gravamos os dados. 

Vamos acessar o navbar_git.py.

![image](https://user-images.githubusercontent.com/79231882/203087721-900e7975-1afe-4569-a559-9a00451d2eea.png)


Este modulo define a configuracao da barra de navegacao do dashboard, situada a esquerda da app:

![image](https://user-images.githubusercontent.com/79231882/203087778-1e07986c-c3e5-4c05-bced-e73a3e16a4b0.png)


→ Importamos as bibliotecas que serao utilizadas;

→ Criamos o Container

→ Chamamos a Linha

→ Chamamos a Coluna

→ Criamos o modulo A (html.A ou tag A em HTML): esta eh uma tag para criar um link em HTML, quando passamos o mouse sobre o texto com o nome da pagina podemos ver o link sendo mostrado bem no rodape da pagina web, como pode-se abaixo:

![image](https://user-images.githubusercontent.com/79231882/203087922-786d9836-c56a-486c-b5bb-fdd189521be3.png)

![image](https://user-images.githubusercontent.com/79231882/203087980-b8243913-8fd2-4042-a393-793869fce0f8.png)



# Conclusao

Utilizando o Dash, criamos as configuracoes em Python para cada um dos modulos com pouco uso de programacao HTML, porque na pratica quem faz esta construcao eh o proprio Dash.


**Podemos fazer algumas questoes com base no que foi visto:**

1- Este problema poderia ser resolvido de forma mais simples ainda com o Power BI?

No Power BI tambem precisariamos carregar os dados, limpar colunas, ajustar a coluna de data, etc. 

2- O Power BI permite que seja criado um dashboard com o Power BI desktop, somente em ambiente Windows. Em outros OS ele nao funciona. Com Python nao temos esta restricao. 

3- O Power BI desktop eh gratuito mas para publicacao online ele é pago, ficariamos restritos ha uso apenas local, limitando a integracao e publicacao da analise. 

Com o dash pegariamos o dashboard desenvolvido, subiriamos ele para um servico de cloud, inicializariamos a app (poderiamos ate criar um sistema de autenticacao) e ele estaria pronto para acesso de outras pessoas. Nao ha custo adicional de licenca.

