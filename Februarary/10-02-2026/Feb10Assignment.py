
#Continuous sum but enter 0 to break
sum=0
while True:
    a=int(input("Enter number to add , enter 0 to stop:"))
    if a==0:
        break
    else:
        sum+=a
print("Final sum is",sum)


#Find odd or even

a=int(input("Enter number: "))

if (a%2):
    print(a,"is odd")
else:
    print(a,"is even")


# print 10,9,8,7,6,5,4,3,2,1

for i in range(10,0,-1):
    print(i)