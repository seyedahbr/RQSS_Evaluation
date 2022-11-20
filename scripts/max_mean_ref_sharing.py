import pandas as pd
dfgene = pd.read_csv('GeneWiki_2022/rqss_framework_output/ref_sharing.csv', index_col=None, header=0)
dfmusic = pd.read_csv('Music_2022/rqss_framework_output/ref_sharing.csv', index_col=None, header=0)
dfships = pd.read_csv('Ships_2022/rqss_framework_output/ref_sharing.csv', index_col=None, header=0)
dfrandom_1 = pd.read_csv('Random_100000_1/rqss_framework_output/ref_sharing.csv', index_col=None, header=0)
dfrandom_2 = pd.read_csv('Random_100000_2/rqss_framework_output/ref_sharing.csv', index_col=None, header=0)
dfrandom_5 = pd.read_csv('Random_500000/rqss_framework_output/ref_sharing.csv', index_col=None, header=0)
dfrandom_10 = pd.read_csv('Random_1000000/rqss_framework_output/ref_sharing.csv', index_col=None, header=0)

MaxMeans = {'Gene Wiki':[round(dfgene['num_of_incomes'].mean()),dfgene['num_of_incomes'].max()], 'Music':[round(dfmusic['num_of_incomes'].mean()),dfmusic['num_of_incomes'].max()],'Ships':[round(dfships['num_of_incomes'].mean()),dfships['num_of_incomes'].max()], 'Random 100000 #1':[round(dfrandom_1['num_of_incomes'].mean()),dfrandom_1['num_of_incomes'].max()],'Random 100000 #2':[round(dfrandom_2['num_of_incomes'].mean()),dfrandom_2['num_of_incomes'].max()], 'Random 500000':[round(dfrandom_5['num_of_incomes'].mean()),dfrandom_5['num_of_incomes'].max()], 'Random 1000000':[round(dfrandom_10['num_of_incomes'].mean()),dfrandom_10['num_of_incomes'].max()]}

print(MaxMeans)
