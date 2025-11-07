# Takes a natural number prints less than it.
a=int(input("Enter a number:"))
for i in range(1,a):
    print(i ,end="   ")
    if i%20==0:
        print()
