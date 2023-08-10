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
    fasta_file = "data/silva_SSU/silva_test.fasta"

    exact_matches = search_exact_matches(query_sequence, fasta_file)

    if exact_matches:
        print("Exact matches found:")
        for match in exact_matches:
            print(match.id)
    else:
        print("No exact matches found.")

    # Match to publications
    df = pd.read_table('data/silva_SSU/publications_for_sequence_entries.ssu.tsv')
    #df = df.set_index("primaryAccession")
    publications = []
    for match in exact_matches:
        # get primary accession
        prim_acc = match.id.split(".")[0]
        print(prim_acc)
        result = df[df["primaryAccession"] == prim_acc]
        publications.append(match)
        print(result["title"])
    
