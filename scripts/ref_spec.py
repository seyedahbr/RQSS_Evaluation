import pandas as pd

subsets = ['GeneWiki_2022','Music_2022','Ships_2022','Random_100000_1/','Random_100000_2/','Random_500000','Random_1000000/']
not_ref_specifics = []
for subset in subsets:
    df = pd.read_csv(subset+'/rqss_framework_output/ref_properties_consistency.csv')
    [not_ref_specifics.append(x) for x in df.loc[df['is_ref_specific']==False,'property'].to_list() if x not in not_ref_specifics]

statement_refprop = pd.read_csv('statement_fact_refed_props.data', names = ['sid','fid','refid'])
total = len(statement_refprop.loc[~statement_refprop['refid'].isna()].drop_duplicates(subset=['sid']))

non_ref_specific_freqs = {}
total_freq = 0
for prop in not_ref_specifics:
    non_ref_specific_freqs[prop] = len(statement_refprop.loc[statement_refprop['refid'] == prop].drop_duplicates(subset=['sid']))
    total_freq += non_ref_specific_freqs[prop]
sorted_d = dict(sorted(non_ref_specific_freqs.items(), reverse = True, key=lambda item: item[1]))
print('total number of distinct statements: ', total)
print('total number of distinct statements referenced with non-specific references: {0}, ({1} %)'.format(total_freq,(total_freq/total)*100))
print('details:')
for key, value in sorted_d.items():
    print('\t {0}: {1}, ({2} %)'.format(key, value, (value/total)*100))
