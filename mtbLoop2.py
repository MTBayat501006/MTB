# Takes a natural number and shows its factors.
a=int(input("Enter a number:"))
print("FactorsSet is { ",end=" ")
for i in range(1,a+1):
    if a%i==0:
        print(i,"  ",end=" ")
print("}")