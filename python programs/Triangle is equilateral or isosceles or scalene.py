s1=int(input(" Enter First Side of the Triangle  : "))
s2=int(input(" Enter Second Side of the Triangle : "))
s3=int(input(" Enter Third Side of the Triangle  : "))

if s1==s2==s3:
    print(" Traingle is Equilateral.")
elif s1==s2!=s3:
    print(" Traingle is Isosceles.")
else:
    print(" Traingle is Scalene.")