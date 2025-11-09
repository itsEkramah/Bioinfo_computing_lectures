# class landanimals:

#     def feature(self):
#         print("they can walk on land.")

# class wateranimals:
#     def feature(self):
#         print("they can swim in water.")
        
# # p1=landanimals()
# # p2=wateranimals()
# # p1.feature()
# # p2.feature()

# # class amphibians(landanimals,wateranimals):#inherit cherachetr of landanimal and wateranimals 
# #     def test(self):
# #         print("they can live both on land and in water.")
# #         """
# #         def feature(self):
# #             retrun .super().feature()#it will call the feature method of the first parent class landanimals
# # """
# # p3=amphibians()
# # p3.feature()#it will call the feature method of the first parent class landanimals
# # p3.test()



# #modules : are files containing python code
# # they can define functions, classes and variables
# # # they can also include runnable code
# # multiple classes

# # import module1 
# # module1.greeting("ekramah")
# # module1.person["name"]
# # print(module1.person)
# # print(module1.person["country"])

# #inbuilt modules: are modules that are included with python installation examples:math,random,os,sys

# # import platform #this module is used to access the underlying platform's data like system,version,architecture 
# # x=platform.system()
# # print(x) 

# # if x=="Windows":
# #     print("you are using windows operating system , ypu can proceed")
    
# # else :
# #     print("this code is not for you ")


# # x=platform.python_version()   #explore more leave after platform. it willl give all of options 
# # print(x)    

# # x=platform.processor()
# # print(x)

# import os  #os module is used to interact with the operating system most of destructive program use this like viruses
# x= os.path()
# print(x)

# x=os.mkdir("newfolder") #to create new directory
# print(x)


# #paper patteren
# #output prediction dry run 
# #error prediction code given pridict kro identify error krna ho gea
# #code and output    middle wala incomplete code complete kro
# #long question scenerio based question
# #write a code to do this and that

# import datetime as dt   ##baar baar datetime nah likhna pray iss lea dt use kren gaay
# x=dt.datetime.now()

# print(x.date)
# print(x.year)
# print(x.day)


##take input date of birth from user and print dayy of that date   (code has error )
# input(int("enter date of birth "))
# x = dt.datetime() 
# print(x.strftime("%A"))  



# import math 
# x=math.sqrt(64)
# print(x)



# import re ## re module is used for regular expressions (matlab ye module string main specific pattern ko search krta hai )
##features of re module
# bioinformatics main re module use hota hai 
#1.search    


##in easy words re module kya hai aur iska use kya hai
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