import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler
  
import warnings
warnings.filterwarnings('ignore',category=Warning)
sns.set_style('ticks')
sns.set_context('talk')

class MethodsPreparation():
    ''' 
    Esta classe define todos os métodos que serão utilizados
    na etapa Data Preparation.
    
    '''

    def __init__(self):
      pass

    def preprocessing(self, df):

      ''' esta função bla bla bla '''
      scale = StandardScaler()
      df_scale = pd.DataFrame(scale.fit_transform(df), 
                               columns=df.columns,
                               index=df.index)

      return df_scale
    
    def import_df(self, nome_arquivo, extensao_arquivo='csv'):
      data = pd.read_csv(os.getcwd()+f'//..//..//data//raw//{nome_arquivo}.{extensao_arquivo}')
      return data


    def export_df(self, df, nome_arquivo, extensao_arquivo='csv'):
      df.to_csv(os.getcwd()+f'//..//..//data//processed//{nome_arquivo}.{extensao_arquivo}')
      return f'Arquivo salvo com sucesso.'
    

    def dynamic_range(self, df):
      plt.figure(figsize=(13,6))
      sns.boxplot(df)
      return plt.show()
    

    def boxplot_distribution(self, df):
      for i in range(0, 8) :
        fig, ax = plt.subplots(1, 2, figsize=(9, 2))
        plt.suptitle(df.columns[i], fontsize=15)
        sns.boxplot(x=df.columns[i], data=df, ax=ax[0]), sns.histplot(df[df.columns[i]], ax=ax[1], alpha=0.5, bins=30)
      return plt.show()
  

    def correlation(self, df):
      plt.figure(figsize=(9,6))
      sns.heatmap(df.iloc[:,1:].corr(),annot=True,cmap='seismic')
      return plt.show()
    

    def pair_plot(self, df):
      plt.figure(figsize=(9,6))
      sns.pairplot(df.iloc[:,1:], hue='cluster', palette='Set1')
      return plt.show()
    



  