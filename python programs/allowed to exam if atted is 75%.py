c=int(input(" Enter no. of Classes held : "))
a=int(input(" Enter no. of Classes attended by you : "))

per=(a/c)*100

print("Percentage of your Attendance : ",per)

if per>=75:
    print(" You are allowed to give the Exam. ")
else:
    print(" You are not allowed to give the Exam. ")