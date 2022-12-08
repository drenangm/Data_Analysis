# Criacao de um scatterplot interativo


Vamos criar um scatterplot (grafico de dispersao) com o D3.js.

Vamos com ele criar um grafico mostrando a relacao entre duas variaveis.

No eixo x teremos a variavel idade do entrevistado.

No eixo y colocaremos a variavel avaliacao (contendo a variacao de 1 (baixa) a 5 (alta)).



No estado padrao do grafico, os pontos ficarao sombreados (opacos) e, por meio de recursos de interatividade, os pontos ficarao mais destacados conforme formos passando o mouse sobre eles:


Cada estado do grafico corresponde a um dos fabricantes de veiculos:


**laranja:** Honda

**azul:** Ford

**verde:** Toyota

**vermelho:** BMW


Default:

![image](https://user-images.githubusercontent.com/79231882/206539939-8cbc8802-7dcd-49c9-8721-08a56dbbeb41.png)


Honda em destaque:

![image](https://user-images.githubusercontent.com/79231882/206540017-f5d8f7f8-5cb3-40b1-a38e-86b433b29dc4.png)


Ford:

![image](https://user-images.githubusercontent.com/79231882/206540077-c40e1dd7-7027-437d-8615-f490c60671c3.png)


BMW:

![image](https://user-images.githubusercontent.com/79231882/206540139-ccf61294-b1b7-4ea2-b615-64a16655fea2.png)


Toyota:

![image](https://user-images.githubusercontent.com/79231882/206540197-880403e1-d047-4381-a369-52d41ac94261.png)



Os recursos utilizados neste grafico conseguem transmitir uma quantidade muito grande informacao sem que o grafico fique muito poluido.

Quando clicamos em uma parte do grafico ele consegue captar a qual fabricante aquele dados se refere, informa tambem a faixa etaria a qual a pesquisa foi respondida sobre a marca e fornece a nota media de avaliacao da marca para aquela faixa etaria.


Vamos ao desenvolvimento do grafico em detalhes.

O conjunto de dados foi colocado em um arquivo de dados separado: **“pesquisa.js”**

![image](https://user-images.githubusercontent.com/79231882/206540319-27de11cf-f141-4560-87dd-e15f75bf8212.png)



Criamos o objeto data, que uma array contendo varios conjuntos de chave/valor.

Vamos ver como chamamos este objeto no nosso arquivo principal HTML **“scatterplot.html”:**

Comecamos carrageando o d3.min.js.

Depois chamamos o “pesquisa.js”.

![image](https://user-images.githubusercontent.com/79231882/206540386-ac9ff69c-abbd-4587-8568-641634d712ca.png)


Eh como se carregassemos uma biblioteca, so que nela consta nossa “variavel”, que eh um objeto.

Definimos a configuracao da area de desenho (largura, altura, margens):

![image](https://user-images.githubusercontent.com/79231882/206540452-4e93de42-6a77-443d-964a-4d800b86934b.png)


Definimos a escala de cores para a area do grafico:

![image](https://user-images.githubusercontent.com/79231882/206540527-c90bf103-09dd-4f2d-8ef7-767f35228e00.png)


Definimos a escala dos eixos x e y, que sera uma escala linear:

![image](https://user-images.githubusercontent.com/79231882/206540590-71680a70-4c5c-4482-a0d9-143800d1d80c.png)


Construcao dos eixos x e y (informacao que ira aparecer no grafico, contendo as faixas etarias selecionadas para serem exibidas no eixo x):

![image](https://user-images.githubusercontent.com/79231882/206540673-25403d3b-6ec6-40f9-aa90-b046c3458713.png)


Incluimos grades para ficarem visiveis no grafico:

![image](https://user-images.githubusercontent.com/79231882/206540734-062e0b00-b908-42e8-837b-4d676d37473b.png)


Criamos um objeto novo que representara a escala das respostas. Essa escala organiza como os circulos serao representados dentro do grafico, fazendo com que a escala de cada bolinha caiba dentro do grafico. Se isto nao for feito da forma correta estas bolinhas poderao aparecer em posicoes fora do grafico.

![image](https://user-images.githubusercontent.com/79231882/206540811-69e9d487-f93f-448e-8530-83527e1e7fbc.png)


Desenvolvemos uma funcao para desenhar os eixos:

![image](https://user-images.githubusercontent.com/79231882/206540894-14098b3d-7603-4483-b4f7-e31dfade0d1e.png)


Criamos a funcao para desenhar o plot chamando a classe “donuts”. Donuts eh a representacao grafica das bolinhas no plot:

![image](https://user-images.githubusercontent.com/79231882/206540977-cf0ef244-aa13-4361-9269-0d53ed62f0bc.png)
![image](https://user-images.githubusercontent.com/79231882/206541039-86ae794e-7e09-4cfc-aeb6-4b8bb975cd83.png)


Incluimos na funcao os recursos de interatividade. Qunado passamos o mouse sobre uma figura plotada reduzimos a opacidade (cor fica nitida). Quando tiramos o mouse sobre o objeto grafico a opacidade volta ao seu valor minimo, fazendo com que a figura volte a ficar opaca.

Depois percorremos os pontos de dados, chamamos os pares chave/valor. 

E por ultimo, quando passamos o mouse sobre um objeto grafico, incluimos uma instrucao para trazer uma mensagem contendo uma frase informando qual a faixa etaria e avaliacao media se refere aquele dado.

Quando tiramos o mouse sobre uma figura, retornamos um texto em branco.

No fim, chamamos nossa funcao:

![image](https://user-images.githubusercontent.com/79231882/206541204-888fbd13-fecd-40b0-95dc-2dfbd22c80be.png)

