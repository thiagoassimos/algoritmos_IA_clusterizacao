import os
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
from paretochart import pareto
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn_extra.cluster import KMedoids
from yellowbrick.cluster import KElbowVisualizer
from sklearn.metrics import davies_bouldin_score
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import cophenet, linkage


sns.set_style('ticks')
sns.set_context('talk')

warnings.filterwarnings('ignore')


class Modeling_Agglomerative():
  
    def __init__(self):
       pass
    
    
    def import_df(self,nome_arquivo,extensao_arquivo='csv'):
      data = pd.read_csv(os.getcwd()+f'//..//..//data//processed//{nome_arquivo}.{extensao_arquivo}')
      return data


    def export_df(self,df,nome_arquivo,extensao_arquivo='csv'):
      df.to_csv(os.getcwd()+f'//..//..//data//modeling//{nome_arquivo}.{extensao_arquivo}')
      return f'Arquivo salvo com sucesso.'
    

    def clustering_hierarchical(self, df, n_cluster):
      model = Pipeline([('hierarchical', AgglomerativeClustering(n_clusters=n_cluster, linkage='ward')
                      )])
      cluster_hierar = model.fit_predict(df)
      return cluster_hierar
    

    def ideal_clusters(self, df, model):
      fig, ax = plt.subplots(1,1,figsize=(16,8))
      visualizer = KElbowVisualizer(model, k=(2,8), metric='distortion', distance_metric='manhattan', ax=ax, timings=False)
      visualizer.fit(df)
      return visualizer.show()

    
    def count_clusters(self, df, cluster_column):
      cluster_counts = df[cluster_column].value_counts()
      for cluster, count in cluster_counts.items():
        print(f'Quantidade de países do cluster {cluster} é {count}.')


    def metrics_model(self, df, n_cluster):
        model = AgglomerativeClustering(n_clusters=n_cluster)
        label = model.fit_predict(df)
        print('*'*45)
        print(f'Índice de Davies-Bouldin: {davies_bouldin_score(df,label)}')

    def report_clustering(self, df, cluster_type):
      for cluster in df[cluster_type].unique(): 
        cluster_data = df[cluster_type] == cluster
        countries = df.loc[cluster_data, 'country']
        print('*'*80)
        print(f'A quantidade de países no CLUSTER {cluster} é {cluster_data.sum()} e são eles: \n\n {countries.tolist()}')
        print('*'*80)
        
        print(f'Estatísticas descritivas do CLUSTER {cluster}\n')
        print('*'*80)
        print(df[df[cluster_type]==cluster].describe())
        print('*'*80)
        print(f'Boxplot do CLUSTER {cluster}\n')
        plt.figure(figsize=(15,9))
        sns.boxplot(df[df[cluster_type]==cluster]);
        plt.show()


    def pca_method(self, df, n_component):
      pca = PCA(n_components = n_component)
      df = pd.DataFrame(pca.fit_transform(df))
      return df 
    

    def pca_(self,df,n_component):
      pca = PCA(n_components = n_component)
      pca.fit_transform(df)
      return pareto(pca.explained_variance_ratio_)


    def best_point_numpy(self, df, cluster_name, n_cluster):
        
      for k in range(n_cluster):
            distance_numpy = df[df[cluster_name]==k].drop([cluster_name], axis=1)
            cluster_numpy = np.array(distance_numpy)
            distances = []
            for i, item1 in enumerate(cluster_numpy):
                avg_distance = 0
                for j, item2 in enumerate(cluster_numpy):
                        if i != j:
                            dist = np.sqrt(np.sum((item1 - item2)**2))                              
                            avg_distance += dist
                avg_distance /= len(cluster_numpy) - 1 
                distances.append(avg_distance)
            best_item_idx = np.argmin(distances) 
            best_point_np =  distance_numpy.iloc[best_item_idx].name.upper()
            print(f'O país com melhor ponto médio do cluster {k} é: {best_point_np}')


    def best_point_scipy(self, df, cluster_name, n_cluster):
        
      for cluster_id in range(n_cluster):
            df_cluster = df[df[cluster_name] == cluster_id].drop(
                        [cluster_name], axis=1)
            distances = pdist(df_cluster.values, metric='euclidean')
            distance_matrix = squareform(distances)
            total_distances = np.sum(distance_matrix, axis=1)
            best_point_index = np.argmin(total_distances)
            best_point = df_cluster.iloc[best_point_index].name.upper()       
            print(f'O país com melhor ponto médio do cluster {cluster_id} é: {best_point} - Distância: {total_distances[best_point_index]}')      


    def medoids_sklearn(self, df, cluster_type):
              
      for i in range(3):
          df_medoid = df[df[cluster_type]==i].drop([cluster_type], axis=1)
          df_array_medoid= np.array(df_medoid) 

          KMobj = KMedoids(n_clusters=1).fit(df_array_medoid)
          kmedoid = KMobj.cluster_centers_.flatten().tolist()
          kmedoid = list(map(float, kmedoid))

          isin_filter = df_medoid.isin(kmedoid)
          row_filter = isin_filter.sum(axis=1) == len(kmedoid)
          linha_localizada = df_medoid.loc[row_filter]

          print(f"O medóide do cluster {i} é: {linha_localizada.index[0].upper()}")
 
  
    def dendrogram_visualization(self, df, method, dist_thrs1, dist_thrs2, dist_thrs3):
         
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))

        linkage = sch.linkage(df, method)
        sch.dendrogram(linkage, labels=df.index, leaf_rotation=90, color_threshold=None)

        ax.set_xlabel('Países')
        ax.set_ylabel('Distâncias')
        ax.axhline(dist_thrs1, color='orange', ls=":")
        ax.axhline(dist_thrs2, color='black', ls=":")
        ax.axhline(dist_thrs3, color='blue', ls=":")   


    def cophenetic_index(self, df):    
      Z = linkage(df, method='average')
      cophenetic_corr, _ = cophenet(Z, pdist(df))
      print('*'*45)
      print(f'Correlação de cophenetic: {cophenetic_corr}')