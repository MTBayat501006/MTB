# takes some numbers and prints their summation and maximum.
a=int(input("Enter a number :"))
Sum=Max=a
while True :
    b=input("Enter a number to Continue or n to end :")
    if b=="n":
        break
    else:
        b=int(b)
        Sum +=Sum
        Max=max(Max,b)
print("Sum is : ",Sum)
print("Max is : ",Max )