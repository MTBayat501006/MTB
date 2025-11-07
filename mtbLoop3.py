# Takes a natural number and determines if it is prime or not.
a=int(input("Enter a number:"))
FactNum=0
for i in range(1,a+1):
    if a%i==0 :
        FactNum +=1
if FactNum==2:
    print(a ,"is a Prime number")
else:
    print(a,"is Not prime number.")