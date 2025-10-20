# #report for project   methodology goal advantage how we will achieve this    week wise division  bioinformatics  ngs relevent pipeline structural prediction  machine learning model    api use 






# #Dictionary
# """
# 1. An unordered , un indexed collection of elements
# 2. key and values
# 3. Declared curly brackets {}
# 4. Mutatable
# """
# dict1={"apples":200 , "banana":150 , "peach":250}
# print(dict1)
# print(dict1["banana"])
# dict1["banana"]=100
# print(dict1)

# print(len(dict1))
# print (dict1.keys())
# print(dict1.values())
# print(max(dict1.values()))
# print(min(dict1.values()))

# # dict1.pop("banana")
# # print(dict1)

# # print(dict1["banana"])

# ##errors type error synrax error index error value error key error identation error

# # dict1["banana"]=100
# # print(dict1["banana"])


# dict2={"onion":50 , "tomato":80 , "potato":30}
# print(dict2)
# dict1.update(dict2)
# print(dict1)

# t2={"onion":[50,60 , 70 , 80] , "tomato":80 , "potato":[30,40 , 50 ,77 ]}
# print(t2)

# for x in dict1:
#     print(x)



# gene1={"p1": [1,0,0,1]}
# gene2={"p2"  : [0,1,0,0]}
# gene3={" p3": [0,0,1,0]}
# gene4={"p4  ": [0,0,1,1]}

# for x in gene1:
#     if(gene1[x][i]==1):
#         print(x, "mutated gene")

genes = {"EGFR": [1, 0, 0, 0], "FGFR": [0, 1, 0, 0], "AKT": [0, 0, 1, 1], "TP53": [0, 0, 1, 1]}
c = 0
inputgene = ""
while inputgene != "q":
    print("list of genes:", list(genes.keys()))
    inputgene = input("enter gene (or 'q' to quit): ")
    if inputgene == "q":
        break
    if inputgene in genes:
        for i in genes[inputgene]:
            if i == 1:
                print(inputgene)
        c += 1
        print(inputgene, "is mutated in patient", c)
    else:
        print("Gene not found. Please enter a valid gene name.")







# #Sets
# """
# 1. An unordered and unindexed collection of items
# 2. Declare curly brackets {}
# 3. Duplicates not allowed
# """

set1={"EGFR","FGFR","AKT","TP53"}
set2={"EGFR","CTNNB1","WNT","MAPK"}

set3=set1.intersection(set2)
print(set3)

set4=set1.union(set2)
print(set4)

set3.remove("EGFR")

set3.add("EGFR")


# GENE ADD PATHWAY SETS GENE 1 TO 6 GENES CANCER GENES USE SET TO MAKE THIS CODE RUN WE WILL GIVE PATHWAY AND IT WILL TELL US HOW MANY GENES ARE THERE IN PATHWAY AND HOW MANY CANCER GENES ARE THERE IN PATHWAY