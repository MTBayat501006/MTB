# Takes two natural number and shows their comon factors.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Common factors ={",end=" ")
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0 :
        print(i ,end="  ")
print("}")


