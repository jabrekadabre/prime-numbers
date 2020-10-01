#program works
a = int(input("enter the value of a"))
flag = False
def prime():
    for i in range(2,a):
        if a%i == 0:
            flag = False
        else:
            flag = True

if flag == True:
    print("the given number is a prime")
else:
    print("the given number is not a prime")
