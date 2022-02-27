list=[]
n=int(input(" Enter Size of List : "))

for i in range(0,n):
    ele=int(input())
    list.append(ele)
    rev=list[::-1]
    print(list)