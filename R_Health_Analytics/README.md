# Projeto - Podemos prever o tempo de sobrevivência dos pacientes 1 ano após receberem um transplante?

O maior desafio deste projeto sera compreender as variáveis que envolvem nosso problema.


## Definição do Problema e Fonte de Dados


O objetivo deste projeto é tentar prever o tempo de sobrevivência de um paciente um ano após o transplante de fígado. Usaremos dados reais disponibilizados publicamente.

Há normalmente uma grande fila de pacientes esperando em um determinado momento para receber um transplante de fígado, pois não há outra cura para o estágio final de doença hepática. Nosso estudo visa ajudar os pacientes a compreender melhor suas chances de sobrevivência após um ano do transplante. As informações do nosso estudo mostram que somos capazes de prever o tempo de sobrevivência com razoável precisão para diferentes intervalos de tempo. Nosso modelo pode auxiliar os pacientes no processo de tomada de decisão(como financeiro por exemplo), enquanto eles esperam na fila para fazer um transplante.

Usando dados do Registro Científico de Recipientes de Transplante (Scientific Registry of Transplant Recipients-SRTR), trabalharemos com variáveis quantitativas e qualitativas criando modelos preditivos usando o tempo de sobrevivência do paciente como nossa variável de resposta(ou seja, teremos um problema de regressão, cujo objetivo é prever um valor numérico).

Usaremos duas técnicas de regressão: regressão linear e rede neural. Ambos os modelos previram o tempo de sobrevida do paciente por 1 a 3 anos após o transplante, usando um conjunto de variáveis mais significativas. As variáveis foram escolhidas após uma pesquisa sobre quais são os fatores mais importantes no processo de transplante de fígado.

Nossos resultados nos dão a certeza de que podemos prever com razoável precisão o tempo de sobrevivência um ano após os pacientes receberem um transplante de fígado. Acreditamos que isso dará aos pacientes uma ideia melhor de suas mudanças de sobrevida por um período prolongado de tempo após o transplante. Usando as informações desses modelos, os pacientes podem tomar uma decisão mais informada quando se trata de transplante de órgão com base em sua condição médica.

Os dados foram extraídos do SRTR Database e modificados para que os alunos pudessem executar o script em suas máquinas. Script e dataset podem ser encontrados ao final do capítulo. Site oficial dos dados:

[https://www.srtr.org/about-the-data/the-srtr-database/](https://www.srtr.org/about-the-data/the-srtr-database/)


Os dados originais devem ser solicitados no link abaixo e a aprovação pode levar até 30 dias, sendo o objetivo estudo e pesquisa:

[https://www.srtr.org/requesting-srtr-data/data-requests/](https://www.srtr.org/requesting-srtr-data/data-requests/)


## Iniciando o projeto

Aqui tentaremos prever o tempo de sobrevida de pacientes que sofreram transplante de fígado um ano após o procedimento ter sido realizado

Quais são as implicações ao ser fazer um transplante de fígado?

O que leva o medico a decidir ou não por fazer um transplante de fígado?

Qual eh a taxa normal de sobrevivência ou mortalidade para pessoas que fizeram transplante de fígado?

Pacotes que serão utilizados:

![image](https://user-images.githubusercontent.com/79231882/206551982-d076cc44-3720-48da-b1f2-040c0461d697.png)

dplyr: manipulação de dados

ggcorrplot: cria plot de correlação, matriz de correlação

forecast: para uso da função accuracy

nnet: uso de uma função para tratamento dos dados 

neuralnet: para construir nosso modelo de rede neural

Vamos construir um modelo de regressão linear (função lm, do pacote stat) e também iremos construir um modelo de rede neural (do pacote neuralnet)

## Carregando e compreendendo os dados

![image](https://user-images.githubusercontent.com/79231882/206552109-6d6064cb-18b4-4a58-95bf-9591fc2c7450.png)


![image](https://user-images.githubusercontent.com/79231882/206552159-d099980e-7dc6-4721-a98f-58666722a6d2.png)


![image](https://user-images.githubusercontent.com/79231882/206552195-3ed41bed-1906-4169-8f30-207f60fc5167.png)


na.strings ⇒ vazio, (trata string como string e numero como numero)


Vamos visualizar os dados:

![image](https://user-images.githubusercontent.com/79231882/206552308-36a9d32b-127f-4f85-a339-99b2e0e400fb.png)


Ja podemos observar duas variáveis que serão muito importantes neste projeto:

PSTATUS (indica se o paciente sobreviveu ou não ao transplante)

PTIME (indica quantos dias o paciente sobreviveu depois do transplante)


Se uma variável não contiver “DON” significa que aquele dado eh do paciente


## Analise exploratória de variáveis quantitativas

Análise Exploratória, Limpeza, Transformação e Manipulação de Dados (Data Wrangling)

Tipos de dados:

![image](https://user-images.githubusercontent.com/79231882/206552563-e2fd835f-4486-4a91-b5c1-c8722cebbcd8.png)

![image](https://user-images.githubusercontent.com/79231882/206552626-57c093a9-f4e4-4f65-8523-3ef348d3fd17.png)


Vamos começar explorando algumas variáveis que temos maior certeza de que são quantitativas (iremos escolher o tipo de gráfico de acordo com o tipo de variável)

numéricas: histograma

categórica: tabela de contingencia (frequência de cada nível/classe)


Idade do paciente:

![image](https://user-images.githubusercontent.com/79231882/206552752-4d4f58a5-5ba8-419d-814b-ba0abe5893f4.png)

![image](https://user-images.githubusercontent.com/79231882/206552791-da00788d-97c9-45e4-8707-3cf5c5b00274.png)


Idade do doador:

![image](https://user-images.githubusercontent.com/79231882/206552845-2fb205ea-aa66-44c4-8d3e-49406710eec4.png)

![image](https://user-images.githubusercontent.com/79231882/206552888-2711ef64-6463-4bf4-8ab3-12b058812186.png)


O padrão dos doadores eh completamente diferente

Variável de resposta PTIME (dias de sobrevivência após o transplante)

![image](https://user-images.githubusercontent.com/79231882/206552962-693f9fb9-9ca0-4302-ab5b-b6c06ac672dc.png)


A grande maioria sobrevive ate mais ou menos 500 dias, conforme ocorre a progressão do tempo o tempo de sobrevivência vai diminuindo

Uma observação importante eh que a pessoa pode vir a falecer devido a outras causas, não necessariamente devido ao transplante


Variável DAYSWAIT_CHRON (quantidade de tempo que a pessoa espera para receber um transplante)

![image](https://user-images.githubusercontent.com/79231882/206553082-9f62f72d-6a1a-47c7-a614-89b2c530c92a.png)

![image](https://user-images.githubusercontent.com/79231882/206553120-57035d57-ea45-47d6-9a6f-4277026b26ee.png)


Em geral as pessoas aguardam 500 dias (mais ou menos 1,5 anos) para receber um transplante



Variável FINAL_MED_SCORE (pontuação que os medicos dão pra pessoa de acordo com a severidade da doença hepatica)

Esse score o medico a decidir em caso de dois pacientes com características semelhantes o que tiver o score maior tem um risco provável de morte maior sem o transplante















