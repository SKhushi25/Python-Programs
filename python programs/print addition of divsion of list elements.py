l=[]
n=int(input("Enter number of list element : "))
div=int(input(" Enter number to divide: "))
for i in range(0,n):
    ele=int(input(" Enter the elements of list : "))
    l.append(ele)
    print(l)
b=[]
for i in l:
    x=i//div
    b.append(x)
    print("addition is : ",sum(b))