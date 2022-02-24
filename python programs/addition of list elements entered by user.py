l=[]
n=int(input(" Enter Size of List : "))

for i in range(0,n):
    item=int(input())
    l.append(item)
print(" The Sum of list elements entered by you is :",sum(l))