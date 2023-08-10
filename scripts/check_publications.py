import pandas as pd
df = pd.read_table('../data/silva_SSU/publications_for_sequence_entries.ssu.tsv')
df = df.set_index("primaryAccession")
#print(df["info"].head())
print(df.iloc[2])
