from Bio import SeqIO
import json

def search_exact_matches(query_sequence, fasta_file):
    matches = []

    # Iterate through fasta records
    for i, record in enumerate(SeqIO.parse(fasta_file, "fasta")):
        print(i)
        sequence = str(record.seq)
        if query_sequence in sequence:
            matches.append(record)

    return matches

if __name__ == "__main__":
    for record in SeqIO.parse("../sample.fasta", "fasta"):
        query_sequence = str(record.seq)
        fasta_file = "../data/silva_SSU/Parc_db/SILVA_138.1_SSUParc_tax_silva_trunc.fasta"

        exact_matches = search_exact_matches(query_sequence, fasta_file)

        if exact_matches:
            print("Exact matches found:")
            for match in exact_matches:
                print(match.id)
        else:
            print("No exact matches found.")


# def create_substring_set(s):
#     return set(s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1))

# def check_substring_in_list(query, string_list):
#     print("checking")
#     query_substrings = create_substring_set(query)
#     list_substring_sets = [create_substring_set(s) for s in string_list]
    
#     for substring_set in list_substring_sets:
#         if query_substrings & substring_set:
#             return True
#     return False

# if __name__ == "__main__":
#     string_list = []
#     # Iterate through fasta records
#     # seq_to_id_map = {}
#     # fasta_file = "../data/silva_SSU/Parc_db/SILVA_138.1_SSUParc_tax_silva_trunc.fasta"
#     # for i, record in enumerate(SeqIO.parse(fasta_file, "fasta")):
#     #     print(i)
#     #     sequence = str(record.seq)
#     #     seq_to_id_map[sequence] = record.id
#     #     string_list.append(sequence)

#     # with open('seq_to_id.json', 'w') as convert_file:
#     #     convert_file.write(json.dumps(seq_to_id_map))


#     fasta_file = "../data/silva_SSU/Parc_db/SILVA_138.1_SSUParc_tax_silva_trunc.fasta"
#     for i, record in enumerate(SeqIO.parse(fasta_file, "fasta")):
#         sequence = str(record.seq)
#         string_list.append(sequence)

#     for record in SeqIO.parse("../sample.fasta", "fasta"):
#         query = str(record.seq)

#     print("Query: " + query)
#     if check_substring_in_list(query, string_list):
#         print(f"'{query}' is a substring of at least one string in the list.")
#     else:
#         print(f"'{query}' is not a substring of any string in the list.")

#     with open('seq_to_id.json') as json_file:
#         seq_to_id_map = json.load(json_file)
