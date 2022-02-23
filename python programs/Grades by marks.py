m=int(input(" Enter your Marks between 1-100 : "))

if m>90:
    print("Grade : A+")
elif m>80 & m<90:
    print("Grade : A")
elif (m>60 & m<80):
    print("Grade : B")
elif m>50 & m<60:
    print("Grade : C")
elif m>45 & m<50:
    print("Grade : D")
elif m>25 & m<45:
    print("Grade : E")
else:
    print("Grade :F")