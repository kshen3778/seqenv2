# import subprocess
# result = subprocess.run(['blastn', '-db', 'data/silva_SSU/Parc_db/SILVA_138.1_SSUParc_tax_silva_trunc.fasta', '-query', 'sample.fasta', '-task', 'blastn', '-outfmt', '7 saccver'], capture_output = True, text = True)
# result_list = result.stdout.split("\n")
# # filter out non accession.version items
# accessionv_nums = []
# for x in result_list:
#     print(x)
#     if (x != '') and (x[0] != "#"):
#         accessionv_nums.append(x)

from Bio import SeqIO
import json
import pandas as pd

def search_exact_matches(query_sequence, fasta_file):
    matches = []

    # Iterate through fasta records
    for i, record in enumerate(SeqIO.parse(fasta_file, "fasta")):
        sequence = str(record.seq)
        if query_sequence in sequence:
            matches.append(record)

    return matches


for record in SeqIO.parse("sample.fasta", "fasta"):
    query_sequence = str(record.seq)
    #fasta_file = "../data/silva_SSU/Parc_db/SILVA_138.1_SSUParc_tax_silva_trunc.fasta"
    fasta_file = "data/silva_SSU/silva_test.fasta" # a small silva file just for testing purposes

    # find exact matches
    exact_matches = search_exact_matches(query_sequence, fasta_file)

    if exact_matches:
        print("Exact matches found:")
        for match in exact_matches:
            print(match.id)
    else:
        print("No exact matches found.")
    data_map = {k.id.split(".")[0]: {} for k in exact_matches}
    #data_map = {} # map of matched accessions to publication id and isolation source
    # Match to publications and isolation sources
    publication_df = pd.read_table('data/silva_SSU/publications_for_sequence_entries.ssu.tsv')
    isolation_source_df = pd.read_csv('data/silva_SSU/isolation_source_db_SSUParc.csv')
    #df = df.set_index("primaryAccession")
    publications = []
    for match in exact_matches:
        # get primary accession
        prim_acc = match.id.split(".")[0]
        #print(prim_acc)
        
        # get publication
        pub_result = publication_df[publication_df["primaryAccession"] == prim_acc]
        pub_result = pub_result.dropna()
        print(pub_result["title"])
        data_map[prim_acc]["publication"] = pub_result["title"].tolist()

        # get isolation source
        isolation_result = isolation_source_df[isolation_source_df["acc"] == prim_acc]
        isolation_result = isolation_result.dropna()
        print(isolation_result["isolation_source"])
        data_map[prim_acc]["isolation_source"] = isolation_result["isolation_source"].tolist()
    print(data_map)  #{'AB000391': {'publication': [], 'isolation_source': []}}


    
