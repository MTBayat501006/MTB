# Takes two integer numbers and prints odd or even numbers between them depending on yot choice.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter 1 for Odd or 0 for Even :"))
print("Your Choice is {",end=" ")
for i in range(min(a,b)+1 , max(a,b)):
    if i%2 ==c  :
        print(i , end="  ")
    if (i-min(a,b))%30==0:
        print(" ")
        print("                ",end=" ")
print("}")

