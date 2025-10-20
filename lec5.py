# # #loops

# # i=0
# # while i<6:
# #     i+=1  
# #     if i==2:
# #         continue
# #     if i==3:
# #         break
# #     print(i-1)
    
    
# #     # i=1: not 2 or 3, so print(1)
# #     # i=2: continue, so skip print
# #     # i=3: break, exit loop before print


# # i=0
# # while i<6:
# #     i+=1  
# #     if i==3:
# #         continue
# #     print(i-1)
# # else:
# #     print("loop ended")
    
# #     # i=1: not 2 or 3, so print(1)
# #     # i=2: not 3, so print(2)
# #     # i=3: continue, so skip print
# #     # i=4: not 3, so print(4)
# #     # i=5: not 3, so print(5)
# #     # i=6: not 3, so print(6)
# #     # loop ends normally, so else block runs





# fruits=["apple","banana","orange"]
# for i in fruits:
#     if i=="banana":
#         continue
#     print(i)



# fruits=["apple","banana","orange"]
# for i in fruits:
#     if i=="banana":
#         break
#     print(i)
#     #loop end ho ga  program nhi
# print(fruits)


# x=int(input("enter a number:"))
# y=int(input("enter a number:"))

# sum=0
# for i in range(x,y+1):
#     if x ==0 :
#          break 
#     if y ==1:
#         continue
#     sum+=i
# print("sum is:", sum)



# while True:
#     x=int(input("enter a number:"))
#     y=int(input("enter a number:"))
#     if x==0:
#         break
#     elif y==1:
#         continue
#     sum=0
#     for i in range(x,y+1):
#         sum+=i
#     print("sum is:", sum)


# for x in range (3,32 ,3):
#     print(x)
    
""" cancer pathway : egfr akt
metabolic pathway : tp52 ,ctknnb1 
immune pathway : fgfr , akt , cdb
"""


# genes = {"EGFR": [1, 0, 0, 0], "FGFR": [0, 1, 0, 0], "AKT": [0, 0, 1, 1], "TP53": [0, 0, 1, 1]}

# pathways = {
#     "Cancer": {"EGFR", "AKT"},
#     "Metabolic": {"TP53", "CTNNB1"},
#     "Immune": {"FGFR", "AKT", "CDB"}
# }

# c = 0
# inputgene = ""

# while True:
#     pw = input("Enter pathway name: ")
    
#     if pw == "q":
#         print("Program ended")
#         break
    
#     if pw in pathways:
#         gset = pathways[pw]
#         print("Pathway:", pw)
#         print("Total genes:", len(gset))
        
#         cset = gset & cancer_genes
#         print("Cancer genes:", len(cset), cset if cset else "None")
        
#         c += 1
#         print(inputgene, "is mutated in patient", c)
#     else:
#         print("Gene not found. Please enter a valid gene name.")




genes = {"EGFR": [1, 0, 0, 0], "FGFR": [0, 1, 0, 0], "AKT": [0, 0, 1, 1], "TP53": [0, 0, 1, 1]}

cancer_pathways = {"EGFR", "AKT"}
metabolic_pathways = {"TP53", "CTNNB1"}
immune_pathways = {"FGFR", "AKT", "CDB"}

c = 0
inputpathway = ""

while inputpathway != "q":
    print("list of genes:", list(genes.keys()))
    inputpathway = input("enter pathway (or 'q'  to quit): ")
    
for y in inputpathway:
    if(y in genes.keys()):
        c=0
        
if(input(cancer_pathways)):
    print("cancer pathway")
elif(input(metabolic_pathways)):
    print("metabolic pathway")
elif(input(immune_pathways)):
    print("immune pathway")
    
for i in genes:
    if inputpathway == "q":
        break
    c+=1
    for x in genes([i]):
        if x == 1:
            c+=1
    print("Pathway:", inputpathway)
    
    
    if inputpathway == "q":
        break
    if inputpathway in genes:
        for i in genes[inputpathway]:
            if i == 1:
                print(inputpathway)
        c += 1
        print(inputgene, "is mutated in patient", c)
    else:
        print("Gene not found. Please enter a valid gene name.")
        
else:
    print("Pathway not found. Please enter a valid pathway name.")