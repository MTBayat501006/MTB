a=int(input("Enter a number:"))
print("PrimeNumbers={",end=" ")
for b in  range(1,a+1):
    FactNum=0
    for i in range(1,b+1):
        if b%i==0 :
            FactNum +=1
    if FactNum==2 :
        print(b ,end="  ")
print("}")
