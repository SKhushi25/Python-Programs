m=int(input(" Enter your Marks between 1-100 : "))

if m>90:
    print("Grade : A+")
elif 90>=m>80:
    print("Grade : A")
elif 80>=m>60:
    print("Grade : B")
elif 60>=m>50:
    print("Grade : C")
elif 50>=m>45:
    print("Grade : D")
elif 40>=m>25:
    print("Grade : E")
else:
    print("Grade :F")