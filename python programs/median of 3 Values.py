n1=float(input(" Enter First number  : "))
n2=float(input(" Enter Second number : "))
n3=float(input(" Enter Third number  : "))

if n1>n2:
    if n1<n3:
        print("median is : ",n1)
    elif n2>n3:
        print("median is : ",n2)
    else:
        print("median is : ",n3)
else:
    if n1>n3:
        print("median is : ",n1)
    elif n2<n3:
        print("median is : ",n2)
    else:
        print("median is : ",n3)

