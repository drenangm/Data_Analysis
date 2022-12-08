# Contrucao de um dashboard para apresentacao de Market Cap, Rendimento de dividendos e EBITDA



Vamos construir uma visualização para análise de dados financeiros. Daremos ênfase à construção do dashboard e organização dos elementos visuais como cores, títulos, organização dos gráficos, etc…

O link abaixo foi usado como fonte de dados para extração dos dados que colocamos em uma planilha Excel que será carregada no Power BI.

## Fonte de Dados:

https://finance.yahoo.com


Vamos construir um dashboard financeiro interativo.

Para este Lab teremos uma base de dados que sera exportada.


Os dados foram extraidos do Yahoo Finance, do indice SP500.

Para testar o dashboard pronto, vamos abir-lo e editar o caminho da base de dados:

![image](https://user-images.githubusercontent.com/79231882/206521455-f25c57cb-621e-42cb-95c7-04a5be8daf9d.png)


Aparecera esta mensagem, que ja era esperada. Iremos editar o caminho da fonte de dados.

Clicamos na configuracao da fonte de dados:

![image](https://user-images.githubusercontent.com/79231882/206521536-f827e0b8-0a1e-4ade-a174-6bd8afeab3de.png)



Este eh o caminho para o qual ela aponta atualmente (de onde ela foi gerada):

![image](https://user-images.githubusercontent.com/79231882/206521635-72faee20-52a7-4087-b6be-ec0e95ad2b55.png)


Alteramos a fonte de dados:

![image](https://user-images.githubusercontent.com/79231882/206521691-15028b35-3273-446f-b57b-30ef9925910f.png)


Pronto, ja temos o dashboard completamente adequado:

![image](https://user-images.githubusercontent.com/79231882/206521735-5d8594b9-cbb2-4367-b79d-e8746d595071.png)


Para fazer este laboratorio eh importante pesquisar sobre dividendos, EBITDA e market cap.


Aqui temos o tema que foi utilizado neste dashboard:

![image](https://user-images.githubusercontent.com/79231882/206521875-85e8fe52-cd4e-437b-808c-e8c6a0ccae9a.png)


Visao geral do dashboard:

![image](https://user-images.githubusercontent.com/79231882/206522307-294cc06c-2040-4b3a-9ac0-eead6434cddf.png)


Podemos perceber que:


- todos possuem o mesmo padrao;

- todos possuem o titulo centralizado

- todos possuem informacao no eixo Y e no eixo X

- todos esta padronizados no mesmo tamanho (os dois da direita sao ligeiramente menores)

- alguns graficos por conterem muitas informacoes, necessitaram de barras de rolagem (uns na vertical e outros na horizontal)

- podemos observar que todos os graficos possui interatividade (quando passamos o mouse sobre a area eh possivel ver informacoes adicionais), isso eh padrao no Power BI

- alem disso quando criamos graficos o Power BI cria interatividade entre os graficos (abaixo selecionamos Microsoft no grafico Market Cap):

![image](https://user-images.githubusercontent.com/79231882/206522921-05ce4f5a-7d83-4bbe-be96-26289c05191b.png)

- foram utilizados 4 graficos de barras (3 com barras na vertical e 1 na horizontal), um grafico de dispersao (earnings/share por empresa) e um grafico de cascata (market cap)

 

Importante perceber que a cor de fundo do dashboard precisa contrastar com os graficos para que a leitura nao fique dificil e cansativa.

Para o primeiro grafico estamos utilizando duas variaveis: 

![image](https://user-images.githubusercontent.com/79231882/206523075-f5e7c391-b676-4de9-9ba2-600f23f1e797.png)


52 week high significa o valor da cotacao mais alto no periodo de 52 semanas (aproximadamente um ano)

Uma forma de chegarmos a um formato bom de exibicao eh montar o grafico o mais simples possivel e apos finalizado selecionamos os recursos de exibicao do Power BI, que dara um formato melhor montado ao grafico e vamos ajustando conforme desejarmos.


**Grafico 1:**

![image](https://user-images.githubusercontent.com/79231882/206523267-6a96fa99-1288-4399-97ad-c5e016cab029.png)

Esse grafico possui uma barra de rolagem na horizontal


**Grafico 2:**

Temos aqui Earnings/Share por Empresa. Aqui trabalhamos com as seguintes variaveis:

![image](https://user-images.githubusercontent.com/79231882/206523356-3050a123-c6c5-4877-a7d8-d116ce8bdf6e.png)

![image](https://user-images.githubusercontent.com/79231882/206523549-9d31a2ff-1489-4a28-91a3-c4f42ad4aeae.png)

![image](https://user-images.githubusercontent.com/79231882/206523726-4087fb94-2e12-4f7c-b53e-d89dadc3850d.png)


**Grafico 3:**


Usamos as seguintes variaveis e elas nos eixos:

![image](https://user-images.githubusercontent.com/79231882/206523817-7973d14c-2cd5-4bd9-a3c7-628db76753d5.png)

![image](https://user-images.githubusercontent.com/79231882/206523875-a1b12bcf-82ec-43f1-802c-052349bcf68d.png)

![image](https://user-images.githubusercontent.com/79231882/206524047-b4f1671f-4070-45f2-8d71-52cc72cb4966.png)


**Grafico 4:**

Aqui temos o market cap por empresa, em que utilizamos os seguintes campos:

![image](https://user-images.githubusercontent.com/79231882/206524147-21493a83-fe20-4365-91d0-e9d24f9d464c.png)

![image](https://user-images.githubusercontent.com/79231882/206524193-9444a9c2-adc4-482c-91de-ecd859351298.png)

![image](https://user-images.githubusercontent.com/79231882/206524227-68b3e7fe-e73b-4bb4-83ac-3e2a30a83ce4.png)


Symbol nada mais eh do que a representacao da empresa em forma de uma sigla oficial utilizada na bolsa de valores.


**Grafico 5:**

Proximo grafico eh o Rendimento de dividendos por empresa. Utilizamos as variaveis abaixo:

![image](https://user-images.githubusercontent.com/79231882/206524325-c9907952-d239-4325-a7ed-003801ca42a2.png)

![image](https://user-images.githubusercontent.com/79231882/206524426-81b04689-d4f4-4b29-a0a4-7ebd19c7d080.png)

![image](https://user-images.githubusercontent.com/79231882/206524516-8f6c7ec7-4499-4cd2-8655-fe6658cf8ab5.png)


**Grafico 6:**

O ultimo grafico eh o EBITDA de cada empresa do SP500. Utilizamos as variaveis abaixo:

![image](https://user-images.githubusercontent.com/79231882/206524591-f93ee36a-f450-41da-9d31-495e6bd47b3a.png)

![image](https://user-images.githubusercontent.com/79231882/206524634-2e82a6f9-4f4c-4570-b940-be835c13dbef.png)

![image](https://user-images.githubusercontent.com/79231882/206524676-3ad83616-a48e-4f5c-974a-134f38a949d4.png)


O indice EBITDA poderia ser calculado tambem, basta que tivessemos o net income das empresas e os juros, taxas, depreciacao e amortizacao.  Fariamos com isso um calculo basico com estes dados financeiros e chegariamos nos indices EBITDA de cada empresa.


Justificativas para usos desses graficos:


- graficos de barras na vertical: mais facil para observarmos hierarquia das informacoes

- grafico de barras na horizontal: porque queremos mostrar a informacao do maior para o menor

- grafico de dispersao: para mostrar o ponto das empresas

- grafico de cascata: para mostrar a evolucao do maior para o menor, mostrando o market cap total que compoe cada faixa (setor)

