import pandas as pd

#Download from: https://drive.google.com/drive/folders/1EcmoEgj0grqwRH5XCdRBoIy1T9tEm75C?usp=sharing
 
#metadata = open('../data/silva_SSU/Parc_db/SILVA_138.1_SSUParc.full_metadata', 'r')
#metadata = open('../data/silva_SSU/SILVA_138.1_SSURef.full_metadata', 'r')
metadata = open('../data/silva_SSU/SILVA_138.1_SSURef_Nr99.full_metadata', 'r')
lines = metadata.readlines()
#print(len(lines[0].split("\t")))
#print(len(lines[1].split("\t")))
data = []
for line in lines[1:]:
    row = line.split("\t")
    row[-1] = row[-1].strip()
    data.append(row)
table = pd.DataFrame(data)

column_names = lines[0].split("\t")
column_names[-1] = column_names[-1].strip()

table.columns = column_names
# table = table.set_index('acc')
print(table)

isolation_sources = sorted(table['isolation_source'].unique())
for i in isolation_sources:
    print(i)
print(len(isolation_sources))
print(len(table[table.isolation_source == '']))
print(len(table))

#table.to_csv("isolation_source_db_SSUParc.csv",index=False)
#table.to_csv("isolation_source_db_SSURef.csv",index=False)
table.to_csv("isolation_source_db_SSURefNr99.csv",index=False)