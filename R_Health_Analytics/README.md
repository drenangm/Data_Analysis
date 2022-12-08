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


![image](https://user-images.githubusercontent.com/79231882/206553999-1145d8e4-d34f-4a20-9a5c-c0096bd1021e.png)

![image](https://user-images.githubusercontent.com/79231882/206554038-3578651d-7609-453c-ac32-e79d6a11cb1d.png)


## Analise exploratória de variáveis qualitativas

Explorando os dados das variáveis categóricas


Variável que indica diabetes (DIAB)

O interpretador interpretou esta variável como do tipo inteiro mas ela eh na verdade uma variável categórica (qualitativa)

Converteremos para tipo factor:

![image](https://user-images.githubusercontent.com/79231882/206554287-cd7f39e9-3553-4aa5-b139-f4601830e916.png)


Variável PSTATUS (também classificada incorretamente como INT):

![image](https://user-images.githubusercontent.com/79231882/206554399-6cb385d4-2ecd-4a4e-b574-fad9325bc9be.png)


0: representa a classe negativa (não morreu)

1: representa a classe positiva (morreu)


A maioria dos pacientes não faleceu após o procedimento

Também vemos que devido a isto temos um desbalanceamento entre as classes, neste projeto isto não nos afeta porque temos um problema de regressão (se fosse classificação isto seria um problema)


Vamos analisar as variáveis que indicam o gênero do paciente (GENDER) e o gênero do doador (GENDER_DON):

![image](https://user-images.githubusercontent.com/79231882/206554637-ec9213e9-8ea7-4b79-a755-9415290b7b12.png)


0: sexo masculino

1: sexo feminino


A predominância tanto em doadores quanto necessitados de transplantes são do sexo masculino

Vamos analisar a variável REGION (região em que os dados foram coletados):

![image](https://user-images.githubusercontent.com/79231882/206554847-abf4ac7f-2bd7-4e01-a3e5-bf661718ab1c.png)


TX_Year (indica o ano de obtenção dos registros):

![image](https://user-images.githubusercontent.com/79231882/206555025-668b4e9a-515c-445a-9802-c9d9359c78fd.png)


No processo de analise deveríamos utilizar todos os anos?

Nao, deveríamos utilizar todos os anos, eis as razoes:

- 2001 so tem um registro

- 2002 também tem um numero de registros muito inferior aos demais anos

- se levarmos um quantidade muito desigual de registros entre os anos, poderíamos carregar um vies ao modelo

- optaremos por remover 2001 e 2002


Vamos verificar a variável MALIG( indica se o tumor eh maligno):

![image](https://user-images.githubusercontent.com/79231882/206555296-df0eff98-1e9f-479c-80d2-eea374583767.png)


N: não eh maligno 

Y: eh maligno

U: undefined


Variável de histórico de cancer no doador (HIST_CANCER_DON):

![image](https://user-images.githubusercontent.com/79231882/206555455-f3816f67-74fa-444b-85a6-094de84466ba.png)


N: não eh maligno 

Y: eh maligno

U: undefined


## Filtrando os dados 

Um dos dados que tem bastante importância neste estudo diz que se o paciente após um ano do transplante, vivendo sobre rigorosas condições de saúde, tem chances muito grandes de sobreviver muitos anos após esse transplante

O primeiro de vida após o transplante eh muito critico para o paciente

Com isso em perspectiva nos vamos aplicar um filtro em que iremos buscar somente os pacientes que estão com registro ha mais de 365 dias, ou seja, que conseguiram ultrapassar a fase critica

Iremos adotar essa medida porque ela eh a base de solução do nosso projeto

Esta informação servira de suporte ao planejamento da vida do paciente envolvido nesta situação:

![image](https://user-images.githubusercontent.com/79231882/206555653-35d339c0-db7d-479a-b35d-3d3d2543f6f6.png)

![image](https://user-images.githubusercontent.com/79231882/206555673-dcf4c7a6-14d7-41bb-85b6-b0f94fb656b4.png)


Comparando com a dimensão original:

![image](https://user-images.githubusercontent.com/79231882/206555722-f79ffd13-b403-4041-858c-dede4d72e951.png)


Vamos criar mais um filtro que servira como uma janela para facilitar a criação do nosso modelo

Dos pacientes que sobreviveram ao primeiro ano da cirurgia, filtramos os que permaneceram vivos por até três anos depois da cirurgia

![image](https://user-images.githubusercontent.com/79231882/206555779-367c4a21-f7f0-476f-b8e4-ad8fcfeee102.png)


A escolha do critério de ate 3 anos após o transplante eh puramente subjetiva, poderíamos ter escolhido qualquer outro tipo de intervalo

Poderíamos ate mesmo criar varias amostras com diferentes intervalos de tempo e depois compara-los


## Correlação entre as variáveis numéricas

Vamos fazer uma divisão entre variáveis numéricas e categóricas

Começamos com a separação das variáveis numéricas


![image](https://user-images.githubusercontent.com/79231882/206555916-8bf506ee-c6bb-4d4c-9f3c-74e577aa0a90.png)

![image](https://user-images.githubusercontent.com/79231882/206555952-1c9fa27d-1751-4047-a691-edbeb79dd77b.png)


Esta divisão foi feita porque para que possamos calcular a matriz de correlação, idealmente devemos fazer com variáveis numéricas 

Para variáveis categóricas utilizamos matriz de associação

Vamos fazer a matriz de correlação:

![image](https://user-images.githubusercontent.com/79231882/206556034-facb8a88-468a-4d3e-8e6c-9cec252e23ee.png)


- iremos somente com valores que são não nulos

- iremos utilizar arredondamento de ate 2 casas decimais

![image](https://user-images.githubusercontent.com/79231882/206556095-c671fd37-a462-4556-826e-ddfe16ae6753.png)

Nao ha nada que justifique, ao analisar esta matriz, que devemos ter algum trabalho adicional de verificação de relação entre variáveis


## Padronização das variáveis numéricas

Padronização das variáveis numéricas e combinação em um novo dataframe com as variáveis categóricas

obs: para termos certeza que o algoritmo que pretendemos utilizar requer que os dados estejam na mesma eh necessário checar a documentação e a padronização eh necessária de ser aplicada somente a dados numéricos, em variáveis qualitativas nos não aplicamos padronização

Aplicamos a padronização aos dados numéricos:

![image](https://user-images.githubusercontent.com/79231882/206556237-7071c783-0534-46ae-9206-7aad318974f9.png)


Unimos os dados numéricos padronizados com os dados categóricos, formando o dataframe final:

![image](https://user-images.githubusercontent.com/79231882/206556290-b23643bb-b40f-4117-a795-cc40b7e55a12.png)

![image](https://user-images.githubusercontent.com/79231882/206556314-0c30a96d-ba23-4e0d-8da9-654bfd39097f.png)


## Divisão dos dados em treino e teste

Por que aplicamos a padronização antes de fazer a divisão dos dados em treino e teste?

Veremos mais a frente…

Vamos dividir os dados em treino e teste (divisão 70/30), a função que faz isso considera:

→ todas as linhas do dataset com o dataframe total:

![image](https://user-images.githubusercontent.com/79231882/206556440-2cb0740d-90e7-446e-8029-3fd8bf31863e.png)


→ fatio a porção que representara os dados de treino, uma  amostra aleatória das linhas do dataframe final:

![image](https://user-images.githubusercontent.com/79231882/206556481-847a0190-82fb-4bc6-bf93-a02ca6de7260.png)


→ função completa da divisão:

![image](https://user-images.githubusercontent.com/79231882/206556535-052c7817-8b2d-431f-ad73-741ecfebe0b5.png)


→ identificamos as porções de treino (70% da amostra aleatória de linhas de dados_final:

![image](https://user-images.githubusercontent.com/79231882/206556601-98034839-3d60-4b8b-bebb-1fd313201647.png)


→ a porção complementar sera alocada para os dados de teste:

![image](https://user-images.githubusercontent.com/79231882/206556650-7badefc4-0ee6-4d33-83f5-34a2409a89fc.png)


Para finalizar vamos remover os anos de 2001 e 2002 porque contem um numero bem mais baixo de registros em relação aos demais anos, o que pode inserir algum tipo de vies aos dados (decisão arbitraria)

![image](https://user-images.githubusercontent.com/79231882/206556704-334e920b-2242-4908-a529-aec38368ed0e.png)


## Modelagem preditiva - Versão 1


Para esta versão faremos a modelagem preditiva utilizando Modelo de Regressão

Vamos trabalhar apenas com algumas variáveis mais significativas para o problema

Isso também reduz o tempo total de treinamento


Veja que vamos desenvolver um modelo de regressão utilizando tanto variáveis quantitativas como qualitativas:

![image](https://user-images.githubusercontent.com/79231882/206556816-fb3d8ed2-9d54-475a-a966-3e61209ce056.png)


![image](https://user-images.githubusercontent.com/79231882/206556862-f3040792-18c1-4df9-abc1-1623ece83116.png)


![image](https://user-images.githubusercontent.com/79231882/206556927-93223c0e-74db-4926-913c-fdbed93c5ef3.png)



Conseguimos um modelo um pouco acima da media, com R2 de 0.549 (quanto maior melhor)

O nível de histórico de uso de álcool do doador na classe undefined (ALCOHOL_HEAVY_DONU) não acrescenta nenhuma informação para o nosso modelo (esta categoria poderia ser removida para simplificar nosso modelo)

O fator de possuir um tumor maligno para ser bastante significativo para o nosso modelo



## Avaliação do modelo versão 1

Vamos avaliar o modelo, primeiramente utilizando dados de treino

![image](https://user-images.githubusercontent.com/79231882/206557042-a9894cf9-f405-44d6-83ee-4e99b20fb84a.png)


Vamos calcular a acurácia em treino comparando as previsões feitas pelo modelo com os dados reais do dataframe:

![image](https://user-images.githubusercontent.com/79231882/206557109-fea045af-a952-48b7-a4f6-7146fb49cab3.png)

obs: o termo “test set” devolvido pela função accuracy eh genérico, e não tem relação com dados de teste


Vamos utilizar dados de teste:

![image](https://user-images.githubusercontent.com/79231882/206557221-3143dd2e-b981-49a3-b151-92a70b260b49.png)


Observamos que o RMSE obtido tanto em treino como em teste possuem valores muito parecidos, o que eh um bom sinal, caso a diferença fosse muito grande poderia ser indicativo de overfitting ou algum outro tipo de problema


Vamos calcular todos os resíduos obtidos em teste e iremos plotar o resultado em um histograma, esperamos obter uma distribuição do tipo normal para os resíduos

![image](https://user-images.githubusercontent.com/79231882/206557333-68ca6f76-eeca-4e82-ab02-8d23f271e895.png)


![image](https://user-images.githubusercontent.com/79231882/206557378-83617a67-0936-440b-9951-c49db945dfe0.png)


A distribuição dos resíduos mostrou próxima a uma normal (não esta perfeito, mas muito próxima), indicando que o modelo esta equilibrado embora ainda tenha uma taxa de acertos um pouco baixa, precisaríamos trabalhar mais para melhorar o desempenho do modelo

Mas eh preciso lembrar que padronizamos os dados antes da divisão dos dados em treino e teste. Vamos mudar a padronização e testar novamente.


## O efeito da padronização antes e depois da divisão em treino e teste


Qual sera o efeito da padronização feita após a divisão em treino e teste?

Agora vamos padronizar os dados de treino e teste de forma separada.

Executamos o procedimento anterior, mas de forma separada em cada subset.

Vamos pegar o dataset dados2 (intacto, so aplicamos o período de analise de casos de ate 1095 dias ou 3 anos)

Vamos fazer novamente a divisão em dados de treino e teste no dataset dados2


![image](https://user-images.githubusercontent.com/79231882/206557631-934c9750-2e67-487c-89bf-138f80a39e8a.png)


Vamos separar as variáveis categóricas e numéricas em treino:

![image](https://user-images.githubusercontent.com/79231882/206557684-72e65f34-4049-41f6-a92d-781458ed1c75.png)

![image](https://user-images.githubusercontent.com/79231882/206557870-40572bd7-674f-4cb1-87e7-f84b9950724f.png)


![image](https://user-images.githubusercontent.com/79231882/206557913-8846a162-7454-4309-81fa-fca690c9137c.png)


Vamos separar as variáveis categóricas e numéricas em teste:

![image](https://user-images.githubusercontent.com/79231882/206557961-7a6ba7e1-101e-4783-af3c-0f5ef7a54f7c.png)


![image](https://user-images.githubusercontent.com/79231882/206558004-74fe0df5-1546-4e9d-a921-f740c1bf90d1.png)


Vamos fazer a padronização das variáveis numéricas em treino:

![image](https://user-images.githubusercontent.com/79231882/206558078-de561ff4-6c70-4748-8785-18412bd7509f.png)


Fazemos a padronização das variáveis numéricas em teste:

![image](https://user-images.githubusercontent.com/79231882/206558162-cd940da2-19ef-4474-832c-d6dd3a4dbf63.png)


Vamos aplicar novamente o filtro para remoção dos registros dos anos 2001 e 2002 em treino e teste:

![image](https://user-images.githubusercontent.com/79231882/206558225-44b5517e-27e1-4034-9268-64b2f9842cda.png)


Vamos criar novamente o modelo agora com o outro dataset de treino (ja padronizado e com os filtros):

![image](https://user-images.githubusercontent.com/79231882/206558287-d99074c6-fde0-4dcb-9374-b6a78badc20f.png)

![image](https://user-images.githubusercontent.com/79231882/206558314-1bb8f047-017b-43e6-954b-fd68c6164a9a.png)

![image](https://user-images.githubusercontent.com/79231882/206558387-686e54aa-4475-41a8-84be-b2c251deb08e.png)


Vemos que o R^2 obtido eh muito parecido ao anterior

Observamos o mesmo efeito no nível de significância das variáveis


Vamos avaliar o modelo com os dados de treino final:

![image](https://user-images.githubusercontent.com/79231882/206558506-e63770ec-f140-4d64-b57e-3aa499d5a9ce.png)

![image](https://user-images.githubusercontent.com/79231882/206558532-f5b61379-e147-4966-b576-eb728123dc27.png)


Avaliaremos com os dados de teste:

![image](https://user-images.githubusercontent.com/79231882/206558584-17a17f9e-ab3c-4c38-9109-8c6d75c3313f.png)


Distribuição do erro de validação:

![image](https://user-images.githubusercontent.com/79231882/206558631-b254a228-1d13-4657-a7dd-4acc0246ed5e.png)


![image](https://user-images.githubusercontent.com/79231882/206558656-64924bc5-f7c8-415e-948f-bd0eb129c946.png)


Vemos que o resultado obtido continua muito parecido


Vamos a algumas razoes sobre os resultados que obtemos:

- sempre precisamos experimentar diferentes métodos para tirarmos nossas próprias conclusões

- não podemos decorar regras, temos boas praticas que devemos procurar observa-las mas analise critica de quem esta desenvolvendo uma solução para o problema eh fundamental

- embora os resultados apresentados sejam parecidos, a padronização deve ser aplicada separadamente entre dados de treino e de teste, para fazermos apenas um estudo nos dados observando o comportamento em diferentes métodos não ha problema com o procedimento que adotamos, mas para colocar o modelo em produção devemos padronizar os dados separadamente


## Desfazendo a escala dos dados

Por que precisamos da padronização nos dados?

Apenas para treinarmos o modelo! O algoritmo de aprendizado de maquina espera receber os dados em um padrão para que ele possa compreende-los

Mas para entregarmos os resultados para uma apresentação, apresentar aos tomadores de decisões nos precisamos desfazer a padronização após o treino do modelo


Vamos desfazer a escala dos dados:

![image](https://user-images.githubusercontent.com/79231882/206558963-e28ff416-e0d5-4958-af1e-062f1c7c3501.png)


Removemos valores NA das variáveis que usaremos para aplicar o unscale

obs: quando criamos o modelo “lm” ele automaticamente remove os valores NA do treinamento

![image](https://user-images.githubusercontent.com/79231882/206559019-8d4d048f-f61d-4622-979b-33afa46c49f2.png)


Lembremos que dados2 contem so dados brutos, aos quais não aplicamos a padronização


Vamos aplicar o filtro para remoção dos anos 2001 e 2002 (na porção de teste apenas)

![image](https://user-images.githubusercontent.com/79231882/206559086-48805f91-7b58-44c8-aa40-857494b9898d.png)


Fazemos as previsões e comparamos com os dados originais para tirarmos os dados de performance:

![image](https://user-images.githubusercontent.com/79231882/206559143-578d9ee9-4df2-48bd-8e50-69431b6b3747.png)


![image](https://user-images.githubusercontent.com/79231882/206559170-34a74a61-1fed-4843-8505-ef8a5d590439.png)


O comportamento observado no histograma eh praticamente o mesmo com os dados padronizados, o que ja era esperado


A padronização eh um artificio matemático que nos utilizamos para fazermos o treinamento dos modelos, porem para comunicarmos os dados em um ambiente externo ao da analise ou experimentação, nos devemos retornar sempre os dados ao seu padrão original


## Modelagem preditiva - Versão 2


Modelagem Preditiva com Modelo de Rede Neural

Vamos iniciar preparando os dados (vamos utilizar os dataset dados_final, que contem variáveis numéricas padronizadas, variáveis categóricas e o filtro do período de interesse)

Também iremos trabalhar apenas com as variáveis utilizadas no modelo da versão 1 (variaveis_amostra)

![image](https://user-images.githubusercontent.com/79231882/206559362-b25444e4-5ea5-4b64-b530-1639e0bb5567.png)

![image](https://user-images.githubusercontent.com/79231882/206559399-e96ba817-313d-4338-9cb8-dbcf1168a9d3.png)


Retorna somente as variáveis que não são do tipo fator:

![image](https://user-images.githubusercontent.com/79231882/206559467-8bfd9216-cdda-4a8b-8060-feb2b411b86d.png)

![image](https://user-images.githubusercontent.com/79231882/206559506-10c3d4b8-1936-4365-8061-91bb179841dc.png)


Retorna o nome das variáveis numéricas:

![image](https://user-images.githubusercontent.com/79231882/206559567-f09712e0-0cd4-4de9-9dfe-96d4dc859302.png)

![image](https://user-images.githubusercontent.com/79231882/206559598-a8befdd8-060b-4afb-afdd-76718bf86449.png)


Iremos gerar uma versão final do dataframe com variáveis dummy:

![image](https://user-images.githubusercontent.com/79231882/206559688-13c36554-adf8-406f-85e3-a4717bfb1127.png)


Quando geramos o modelo com regressão linear nos não precisamos criar esta variáveis dummy porque a função “lm” ja faz isso por nos (basta observar o summary do modelo e ver que, por exemplo, ele criou uma serie de dummies para REGION; REGION1, REGION2, REGION3, …)

Veja abaixo as variáveis dummies criada pelo algoritmo do lm:

![image](https://user-images.githubusercontent.com/79231882/206559769-560015f6-09bc-4055-9838-cf2e21809fcb.png)


Na rede neural nos precisamos preparar o dataframe com estas variáveis dummy

A variável dummy eh a aplicação de one-hot-encoding, vejamos a variável REGION1, por exemplo:

![image](https://user-images.githubusercontent.com/79231882/206559853-52b1d436-4293-49c6-88e4-853196259061.png)


Na coluna 1 acima (relacionada a variável REGION1) temos que sera marcado o valor 0 se o paciente não pertence a REGION1 e sera marcado 1 quando ele pertencer a REGION1

Na REGION2 este mesmo paciente tera marcação igual 0 pois pela regra deste problema este paciente não pode pertencer a duas regiões diferentes

Isto foi feito utilizando a funcao “class.ind” do pacote NNET

Criamos as variáveis dummy para as variáveis do tipo categórica

Vamos acertar os nomes das variáveis dummy que foram criadas para que fiquem bem identificadas:

![image](https://user-images.githubusercontent.com/79231882/206559976-5d8df077-b612-4e6d-9b9e-abd5613ee037.png)

![image](https://user-images.githubusercontent.com/79231882/206560003-6cca4f2d-1956-42e0-a42a-9e1e03862827.png)


![image](https://user-images.githubusercontent.com/79231882/206560047-29def049-f592-4a6e-ac46-127b2c7232fa.png)


Dividimos os dados em treino e teste na proporção 70/30:

![image](https://user-images.githubusercontent.com/79231882/206560100-90ecf8a5-be55-4f8f-8754-b76c4f0eaec5.png)


Verificamos os resultados das variáveis para apenas a primeira amostra:

![image](https://user-images.githubusercontent.com/79231882/206560169-5e61366b-4fde-441d-be78-afc6a1f8bebc.png)


Vamos criar o modelo:

![image](https://user-images.githubusercontent.com/79231882/206560214-05d26373-f402-40b2-ac8f-3881780c1093.png)


→ hiperparametros dos modelo:

- criamos uma saída linear (linear.output), para indicarmos que sera uma rede neural regressora

- duas camadas ocultas (hidden)

- definição do numero de passos (stepmax), se este parâmetro não for ajustado ele responderá que não consegue chegar a convergência porque não ha tempo suficiente para isso, a rede neural eh um modelo que executa muitas operações matemáticas


## Avaliação do modelo Versão 2


Vamos criar um plot do modelo_v2:

![image](https://user-images.githubusercontent.com/79231882/206560365-57c4372d-5257-4a16-b9f3-60d8bd664c7a.png)


![image](https://user-images.githubusercontent.com/79231882/206560413-6e3e21d0-a56e-4107-a96a-c536e949e329.png)


Vamos a avaliação deste modelo


Avaliação dos dados de treino:

![image](https://user-images.githubusercontent.com/79231882/206560487-ed869cf0-a57c-43ab-a5f7-a69a16a10e5c.png)


Observação: para fazermos as previsões com o modelo de rede neural nos utilizamos a função compute, no modelo de regressão linear utilizamos a função predict

Avaliação dos dados de teste:

![image](https://user-images.githubusercontent.com/79231882/206560606-3e28dd0c-3f27-4a93-a136-c921ad50b10b.png)

Os resultados das métricas foram muito parecidos, o que nos leva a avaliar que este modelo possui um bom equilíbrio



## Conclusão

Voltamos a pergunta que gerou o problema ao qual trabalhamos:

**Podemos prever o tempo de sobrevivência dos pacientes 1 ano após receberem um transplante?**

**Sim, conseguimos prever o tempo de sobrevivência dos pacientes 1 ano após receberem um transplante.**


### Qual modelo escolheremos?

### **O modelo de regressão linear apresentou uma taxa de erro menor e, portanto, deve ser usado como versão final**

### Podemos avaliar também que para problemas com dados um pouco mais simples, que possuem um padrão claro a regressão linear se mostra bastante satisfatória

### Sem contar também que a regressão linear oferece maior interpretabilidade o que facilita compreendermos os resultados que obtemos, o que eh fundamental na area medica

