# #Q1
# ls=[]
# mystring=input("Please enter string: ")
# mychar=input("Please enter char need search in string: ")

# for i,mychar1 in enumerate(mystring):
#     if mychar1==mychar:
#         out=mystring.find(mychar)
#         ls.append(i)
# print(ls)
#################################

###############################
#Q2
#########multiplction number and it sam##########

num=int(input("Please enter number: "))

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         # print(i*j)
#         pass
print( [ [i*j for j in range(1,i+1)] for i in range(1,num+1) ] )


############################
#Q3
#####false answer
# listname=eval(input("Please Enter LIST OF NAME ex:['mostafa','asd']: "))
# listname=["mostafa","hussien"]

# print("{",[ [listname[i][0],':', listname[i]]   for i in range(len(listname))] ,"}")

############
#Q3
listname=eval(input("Please Enter LIST OF NAME ex:['mostafa','asd']: "))
Dictionary={}
for i in range(len(listname)):
    d={listname[i][0]:listname[i]}
    Dictionary.update(d)
print(Dictionary)

    