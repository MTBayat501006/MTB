stuList=["Ali", "Pari", "Hasan" ,"Kati"]
def addToList():
    a=input("Enter a name to add or e for end :")
    while a!="e":
        stuList.append(a)
        if a=="e" :
            break
        a = input("Enter a name to add or e for end :")


#==========================================================
def delFromList():
    if len(stuList)==0 :
        print("There is no item for delete!")
    while len(stuList)!=0 :
        a=input("Enter a member to delete or e for end :")
        if a=="e" : break
        stuList.remove(a)
#===========================================================
def editMember() :
    if len(stuList)==0:
        print("There is no item to edit!")
    while len(stuList)!=0 :
        a=input("Enter a member to Edit or e for end :")
        if a=="e" : break
        if stuList.count(a)==0 :
            print("There is no such a member!")
        else:
            b = input("What do you want to replace :")
            stuList[stuList.index(a)]=b
#===========================================================
def isInList():
    x=input("Who do you search:")
    c=stuList.count(x)
    if c==0:
        print("There is no",x,"in the list!")
    else:
        print("There is", c ,x ,"in the list.")
#===========================================================
while True :
    print("================================")
    print("Enter 1 for Add new member.")
    print("Enter 2 for Remove some members.")
    print("Enter 3 for Edit new member.")
    print("Enter 4 for search a member.")
    print("Enter 5 for SHOW THE LIST.")
    print("Enter 6 if have no task.")
    print("================================")
    Choice=int(input("Enter your Choice :"))
    match Choice :
        case 1 :
            addToList()
        case 2 :
            delFromList()
        case 3 :
            editMember()
        case 4 :
            isInList()
        case 5 :
            print(stuList)
        case 6 :
            print("Have a good time (-:D")
            break



