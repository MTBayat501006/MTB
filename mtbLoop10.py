#Takes an integer number and converts it to binary base
a=int(input("Enter a number :"))
b=""
while a>0 :
    b += str(a%2)
    a=a//2
print("(",end=" ")
for i in range(len(b)):
    print(b[len(b)-1-i],end=" ")
print(")2")
