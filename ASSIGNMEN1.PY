# Gene mutations for 4 patients
# 1 = mutated, 0 = not mutated
mutations = {
    "EGFR": [1, 0, 0, 0],
    "FGFR": [0, 1, 0, 0],
    "AKT": [0, 0, 1, 1],
    "TP53": [0, 0, 1, 1],
    "CTNNB1": [0, 1, 0, 1],
    "CDB": [0, 0, 0, 0]
}

# Pathways with their genes (sets are used because they store unique values)
pathways = {
    "Cancer": {"EGFR", "AKT"},
    "Metabolic": {"TP53", "CTNNB1"},
    "Immune": {"FGFR", "AKT", "CDB"}
}

# number of patients = length of any gene’s mutation list
num_patients = len(mutations["EGFR"])

print("Available pathways:", list(pathways.keys()))
print("Type 'q' to quit.")

while True:
    # Ask user for one or more pathways
    input_pathway = input("\nEnter pathway name(s): ")

    # If user types q → program ends
    if input_pathway.lower() == "q":
        print("Program ended.")
        break

    # ---- MULTIPLE PATHWAYS LOGIC ----
    # split input by comma → creates a list of pathways
    # Example: "Cancer, Immune" → ["Cancer", " Immune"]
    chosen_pathways = input_pathway.split(",")

    # Loop over each pathway entered by user
    for pathway in chosen_pathways:
        pathway = pathway.strip()   # remove extra spaces (e.g. " Immune" → "Immune")

        if pathway in pathways:
            print("\nPathway:", pathway)
            genes_in_pathway = pathways[pathway]   # get genes for that pathway
            print("Genes in pathway:", genes_in_pathway)

            # Show patient mutations
            for i in range(num_patients):
                mutated = []   # genes mutated in this patient
                unmutated = [] # genes not mutated in this patient
                for g in genes_in_pathway:
                    if mutations[g][i] == 1:
                        mutated.append(g)
                    else:
                        unmutated.append(g)
                print("Patient", i+1)
                print("  Mutated:", mutated if mutated else "None")
                print("  Unmutated:", unmutated if unmutated else "None")

        else:
            print("\nPathway not found:", pathway)
            
            
            #dictionary names ki 1 aur dictonary banaa laien compare values input compare with its key 
#2nd way ask user 1st pathway name 2nd pathway name compare both pathways genes