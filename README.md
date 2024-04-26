<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

## Interpretação dos resultados 

O dendrograma é uma representação gráfica em forma de árvore para analisar agrupamentos ou clusters e assim mostrar a estrutura hierárquica dos dados. Nesta análise cada país é considerado um cluster (folha) que vai sendo aglomerado aos pares levando em conta alguma medida de similaridade - em nosso caso a distância euclidiana - até formar clusters maiores também conhecidos como nós subordinados, que serão conectados entre si até um limite (_threshold distance_) que é o ponto de corte para que os países sejam agrupados no mesmo cluster; se tiver um valor acima deste limite, o algoritmo não une. A partir daí todos os nós subordinados são conectados entre si até serem conectados ao nó raiz.

 Fazendo a análise de cima para baixo, podemos observar que o nó raiz se divide em 2 nós subordinados maiores, tal que o da direita é subdividido em outros dois, formando assim os 3 agrupamentos imputados no algoritmo.

Os valores de thresholsd e a forma do dendrograma praticamente não sofreram alterações com e sem o uso da PCA no dataset.
 
Uma observação para não gerar confusão é que os países representados pelo cluster na cor verde no primeiro dendrograma (sem PCA) são os mesmos na cor roxa do segundo dendrograma (com PCA). Isso dá para ver tanto pelos nomes quanto pelo formato do agrupamento.


- Países mais ricos - threshold pouco maior que 15;
 
- Países intermediários - threshold ligeiramente maior que 9 no dendrograma sem PCA e ligeiramente menor que 9 no dendrograma com PCA;

- Países mais pobres - threshold praticamente igual a 13.

Essas diferenças nos dendrogramas dos países intermediários se deve à diferença na quantidade de países em cada cluster que o modelo de clusterização hierárquica apresentou para os casos sem PCA e com PCA.

## Comparação dos resultados

A principal semelhança nos resultados comparando ambos os modelos (com e sem uso da PCA) foram os valores bem próximos para o índice de Davies-Bouldin(DB), entretanto, a clusterização hierárquica ainda leva uma pequena vantagem. Uma outra semelhança foi no resultado do dendrograma (escolhendo 3 clusters para representar os países) o que condiz com o número de clusters que escolhemos inicialmente no K-Means. Os medóides usando PCA foram os mesmos para ambos os modelos, porém sem o uso da PCA alguns cluster tiveream o mesmo medóide e outros não. O mesmo resultado ocorre com o país que melhor representa seu cluster - a PCA mostra o mesmo resultado para K-Means e hierárquica, o que não ocorre sem o uso da PCA; somente 1 país coincide para ambos os modelos.

A escolha pelo índice de DB se deve ao fato dele ser menos sensível a presença de _outliers_ - os quais foram mantidos no modelo - já que não seria interessante remover diversos países para fazer a análise.

A principal diferença foi a quantidade de países em cada cluster de K-Means vs. Hierárquica. Essa diferença pode estar associada ao fato de K-Means:

1 - ser mais sensível a _outliers_ em relação à clusterização hierárquica;

2 - assumir clusters esféricos e ter sensibilidade a tamanhos e formas irregulares de clusters; isso já é mais flexível no  algoritmo de clusterização hierárquica;

3 - depender da escolha inicial dos centros dos clusters, o que não é necessário na clusterização hierárquica.

Além disso, também usei o índice cophenetic e ele apresentou um ótimo resultado, o que define a escolha pela clusterização  hierárquica como melhor modelo.

Um outro ponto a ser observado é que a visualização do método do cotovelo definiu valores diferentes para o número de ideal de clusters na Hierárquica:

1) K-Means: 

    sem PCA: 6

    com PCA: 6

2) Hierárquica:

    sem PCA: 6

    com PCA: 4 

Ressalto que esses valores foram testados em ambos os modelos e apresentou melhora significativa no índice de DB, todavia não foi implementado porque, como dito anteriormente, o interesse inicial é trabalhar com 3 clusters.

A principal semelhança nos resultados comparando ambos os modelos (com e sem uso da PCA) foram os valores bem próximos para o índice de Davies-Bouldin(DB), entretanto, a clusterização hierárquica ainda leva uma pequena vantagem. Uma outra semelhança foi no resultado do dendrograma (escolhendo 3 clusters para representar os países) o que condiz com o número de clusters que escolhemos inicialmente no K-Means. Os medóides usando PCA foram os mesmos para ambos os modelos, porém sem o uso da PCA alguns cluster tiveream o mesmo medóide e outros não. O mesmo resultado ocorre com o país que melhor representa seu cluster - a PCA mostra o mesmo resultado para K-Means e hierárquica, o que não ocorre sem o uso da PCA; somente 1 país coincide para ambos os modelos.

A escolha pelo índice de DB se deve ao fato dele ser menos sensível a presença de _outliers_ - os quais foram mantidos no modelo - já que não seria interessante remover diversos países para fazer a análise.

A principal diferença foi a quantidade de países em cada cluster de K-Means vs. Hierárquica. Essa diferença pode estar associada ao fato de K-Means:

1 - ser mais sensível a _outliers_ em relação à clusterização hierárquica;

2 - assumir clusters esféricos e ter sensibilidade a tamanhos e formas irregulares de clusters; isso já é mais flexível no  algoritmo de clusterização hierárquica;

3 - depender da escolha inicial dos centros dos clusters, o que não é necessário na clusterização hierárquica.

Além disso, também usei o índice cophenetic e ele apresentou um ótimo resultado, o que define a escolha pela clusterização  hierárquica como melhor modelo.

Um outro ponto a ser observado é que a visualização do método do cotovelo definiu valores diferentes para o número de ideal de clusters na Hierárquica:

1) K-Means: 

    sem PCA: 6

    com PCA: 6

2) Hierárquica:

    sem PCA: 6

    com PCA: 4 

Ressalto que esses valores foram testados em ambos os modelos e apresentou melhora significativa no índice de DB, todavia não foi implementado porque, como dito anteriormente, o interesse inicial é trabalhar com 3 clusters.

## Escolha de algoritmos

### 1. Escreva em tópicos as etapas do algoritmo de K-médias até sua convergência.

**Matematicamente:**

Primeiramente vamos definir um objeto $\textbf{c}_{i} \in \mathbb{R}^{K\times 1}$ que representará cada cluster. A ideia é buscar atribuir os dados aos clusters, bem como um conjunto de objetos $\{\textbf{c}_i\}_{i=1}^{k}$, tais que a soma das distâncias de cada amostra $\textbf{x}_n$ ao $\textbf{c}_i$ mais próximo seja minimizada.
Considerando que temos um espaço métrico em questão, vamos definir uma função chamada objetivo, que é dada por: 

$$O = \displaystyle{\sum_{n=1}^{N}}\displaystyle{\sum_{i=1}^{k}}z_{n,i}\Vert\textbf{x}_{n}-\textbf{c}_i\Vert^2\nonumber$$, onde

...z_{n,i} =
\left\{\begin{array}{rll}
1, & \; \hbox{se}\;\;\textbf{x}_{n}\in \textbf{c}_i \nonumber\\ 
0, & \; \hbox{se}\;\; \textbf{x}_{n}\notin \textbf{c}_{i}  \end{array}\right....

1 - Dadas as posições atuais dos clusters $\{\textbf{c}_i\}_{i=1}^{k}$, minimizamos $O$ em relação a
$z_{n,i}$, isto é, fazemos a atribuição de cada padrão $\textbf{x}_n$ a um dos clusters existentes,
$\begin{equation}
\displaystyle\min_{z_{n,i}} O = \displaystyle{\sum_{n=1}^{N}}\displaystyle{\sum_{i=1}^{k}}z_{n,i}\Vert\textbf{x}_{n}-\textbf{c}_{i}\Vert^2\nonumber, 
\end{equation}$
logo, 

$\begin{equation} 
z_{n,i} =
\left\{\begin{array}{rll}
1, & \; \hbox{se}\;\;\arg\displaystyle\min_{j}\Vert\textbf{x}_n-\textbf{c}_i\Vert^2 \nonumber\\ 
0, & \;\hbox{caso contrário} \end{array}\right.
\end{equation}$


2 - Dada a atribuição dos dados aos clusters, minimizamos com respeito a  $\textbf{c}_i$, ou seja, atualizamos as posições dos clusters e consequentemente

$\begin{equation}
\dfrac{\partial O}{\partial \textbf{c}_j} = \displaystyle{\sum_{n=1}^{N}} z_{n,j}(\textbf{x}_n-\textbf{c}_j)=0\nonumber,
\end{equation}$

logo,
$\begin{equation}
\textbf{c}_j = \dfrac{\displaystyle{\sum_{n=1}^{N}}z_{n,j}\textbf{x}_n}{\displaystyle{\sum_{n=1}^{N}z_{n,j}}}\nonumber.
\end{equation}$

Resumidamente, podemos dizer que o K-Means repete estes dois passos até que a convergência (posições dos objetos deve ser inferior a um limiar pequeno) seja atingida, isto é, até que o centróide não se desloque mais.

Veja que o denominador da equação acima equivale ao número de amostras $x_n$ atribuídas ao cluster, logo, $c_j$ nada mais é do que o vetor resultante da média aritmética de todas as amostras pertencentes ao cluster $j$.

**Interpretação da linguagem matemática**

A ideia central do K-Means é particionar um conjunto de dados em k clusters, nos quais cada ponto de dados pertence ao cluster cujo centróide é mais próximo. A partir daí ele repete sucessivamente esta tarefa com intuito de otimizar a divisão dos dados em clusters, de tal forma que a variância dentro de cada cluster seja minimizada.

As etapas do algoritmo são divididas da seguinte forma:

1) escolhe o número de clusters (k).

2) inicializa aleatoriamente os centróides, um para cada cluster; lembramdo que os centróides são os pontos que representam o centro de cada cluster.

3) atribui cada ponto de dados ao cluster cujo centróide é o mais próximo - isso é feito calculando a distância entre cada ponto e todos os centróides e atribuindo o ponto ao cluster cujo centróide é o mais próximo.

4) atualiza os centróides, ou seja, recalcula os centróides de cada cluster - isso é feito tirando a média de todos os pontos atribuídos a cada cluster.

Aplica sucessivamente os métodos 3 e 4 até que não haja mais alterações nas atribuições dos pontos aos clusters, isto equivale a dizer que as posições dos clusters é atualizada até que o centróide não se desloque mais ou até que se alcance o número máximo de iterações definido inicialmente.

### 2. O algoritmo de K-médias converge até encontrar os centróides que melhor descrevem os clusters encontrados (até o deslocamento entre as interações dos centróides ser mínimo). Lembrando que o centróide é o baricentro do cluster em questão e não representa, em via de regra, um dado existente na base. Refaça o algoritmo apresentado na questão 1 a fim de garantir que o cluster seja representado pelo dado mais próximo ao seu baricentro em todas as iterações do algoritmo. Obs: nesse novo algoritmo, o dado escolhido será chamado medóide.

O Medoid do Cluster 0 é: TANZANIA

O Medoid do Cluster 1 é: TUNISIA

O Medoid do Cluster 2 é: FINLAND

## Usando PCA

O Medoid do Cluster 0 é: TANZANIA

O Medoid do Cluster 1 é: SURINAME

O Medoid do Cluster 2 é: FINLAND

### 3. O algoritmo de K-médias é sensível a outliers nos dados. Explique.

Sim, pois a ideia é minimizar a norma(geralmente euclidiana) entre os pontos e os centróides dos clusters. Como os outliers são pontos discrepantes no espaço de características, eles oferecem alterações significativas na média e, consequentemente, no centróide.

A sensibilidade a outliers pode levar a resultados indesejados, pois o centróide pode ser "puxado" em direção aos outliers, distorcendo a formação dos clusters. Isso ocorre porque o K-Means assume que os dados são distribuídos de maneira esférica e homogênea, o que significa que ele tentará criar clusters que são esfericamente compactos e de tamanhos aproximadamente iguais.

# 4. Por que o algoritmo de DBScan é mais robusto à presença de outliers?

O DBSCAN se baseia na densidade de pontos em torno de cada padrão para definir os clusters. Na primeira etapa do algoritmo ele toma cada amostra e a considera: ou como um ponto central, ou como um ponto de fronteira ou como um ruído; já na segunda etapa os pontos centrais e de fronteira são agrupados em clusters, o que significa que os pontos de ruído ficam fora de qualquer cluster, e por isso sua robustez aos _outliers_.
