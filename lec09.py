# re module python ka ek built-in library hai jo regular expressions (regex) ko handle karta
# hai. Regular expressions ek special syntax hoti hai jo text patterns ko define karne ke liye
# use hoti hai. Is module ka use strings mein specific patterns ko search, match,
# split, aur replace karne ke liye hota hai.

# re module ke kuch important functions aur unka use:
# - import re: regex use karne ke liye.
# - re.search(pattern, string): string mein pehla match dhoondta hai (agar mile to Match object).
# - re.match(pattern, string): sirf string ke start pe match check karta hai.
# - re.fullmatch(pattern, string): poori string pattern se match honi chahiye.
# - re.findall(pattern, string): saare non-overlapping matches list mein return karta hai.
# - re.finditer(pattern, string): Match objects ka iterator deta hai (memory friendly).
# - re.split(pattern, string): pattern ke basis pe string split karta hai.
# - re.sub(pattern, repl, string): matches ko replace karta hai (repl string ya callable).
# - re.compile(pattern, flags): pattern ko compile karke speed improve karta hai (jab baar-baar use karna ho).
# - Common tokens: . ^ $ [] () | ? * + {m,n} \d \w \s — raw strings r"..." use karo.
# - Flags: re.I (ignore case), re.M (multiline), re.S (dot matches newline), re.X (verbose).
# - Tips: user input ko re.escape() se escape karo; greedy quantifiers overmatch kar sakte hain, use lazy ? jab required.
# - Bioinformatics tips: DNA codons r"[ACGT]{3}", FASTA header r"^>(\S+)" — use character classes for ambiguous bases.
# 


# import re 
# DNA = "ACGTAGCTAGCTAGCTGGCTGATCGATCGATCGTAGCTAGCTAGGCTAGCTA"
# x=re.search("GGC" , DNA)
# print(x)

# x=re.findall("GGC" , DNA)
# # print(x.index("GGC"))

# # x=re.finditer("GGC" , DNA)
# # for i in x:
# #     print(i) 
    
    
# # x=re.findall("GGC" , DNA)
# # print(x.count("G"))

# # print(x.start)
# # print(x.end)

# x=re.split("GGC" , DNA)
# print(x)

# count of g + count of c / total l of string *100



# import re 
# DNA = "ACGTAGCTAGCTAGCTGGCTGATCGATCGATCGTAGCTAGCTAGGCTAGCTA"
# # gc_content= (DNA.count("G") + DNA.count("C")) / len(DNA) * 100
# # print("GC content:", gc_content)


# # x=re.findall("G", DNA)
# # y=re.findall("C", DNA)
# # gc_content2= (len(x) + len(y)) / len(DNA) * 100
# # print(gc_content2)


# x= re.findall("...", DNA)  #... means 3 characters codon
# print(x)

# x= re.split("...", DNA)  #... means 3 characters codon
# print(x)
# ###split wont work as three dot search


# x=re.sub("GGC", "TTA", DNA)
# print(x)   #substitur\te fun change to the new patteren


# txt="welcome , {0} ,  you are in {1} vclass  i am in {2} here to guide you"
# print(txt.format("sir adnan","BIF","lecturer"))


# dna to rna for transcription and translation
# import re
# DNA = "ACGTAGCTAGCTAGCTGGCTGATCGATCGATCGTAGCTAGCTAGGCTAGCTA"
# codon_table = {
#     # Phenylalanine
#     'UUU': 'F', 'UUC': 'F',
#     # Leucine
#     'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
#     # Isoleucine
#     'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
#     # Methionine (Start codon)
#     'AUG': 'M',
#     # Valine
#     'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
#     # Serine
#     'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
#     # Proline
#     'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
#     # Threonine
#     'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
#     # Alanine
#     'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
#     # Tyrosine
#     'UAU': 'Y', 'UAC': 'Y',
#     # Histidine
#     'CAU': 'H', 'CAC': 'H',
#     # Glutamine
#     'CAA': 'Q', 'CAG': 'Q',
#     # Asparagine
#     'AAU': 'N', 'AAC': 'N',
#     # Lysine
#     'AAA': 'K', 'AAG': 'K',
#     # Aspartic Acid
#     'GAU': 'D', 'GAC': 'D',
#     # Glutamic Acid
#     'GAA': 'E', 'GAG': 'E',
#     # Cysteine
#     'UGU': 'C', 'UGC': 'C',
#     # Tryptophan
#     'UGG': 'W',
#     # Arginine
#     'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
#     # Glycine
#     'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
#     # Stop codons
#     'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
# }

# def t1_dna_to_rna(codon_table , dna_seq):
#     return dna_seq.replace('T', 'U')
# rna_seq = t1_dna_to_rna(codon_table , DNA)
# print("RNA Sequence:", rna_seq)


# def t2_rna_to_protein(codon_table , rna_seq):
#     protein_seq = ""
#     codons = re.findall("...", rna_seq)
#     for i in codons:
#         amino_acid = codon_table.get(i, "")
#         if amino_acid == "Stop":
#             break
#         protein_seq += amino_acid
#     return protein_seq

# print("Protein Sequence:", protein_seq)







try:
    print(100/10)
except ZeroDivisionError:
    print("you can not divide by zero")
finally:
    print("run complete")