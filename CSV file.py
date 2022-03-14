import csv
f = open(" student.csv ","w")
a = csv.writer(f)
a.writerow([" Name "," Rollno "," Email id "," Address "," Mob.No ","p1","p2","p3","p4","p5","Total","Percentage","Result"])
name = str(input(" Enter your Name : "))
rollno = int(input(" Enter your Rollno : "))
email = (input(" Enter your email id : "))
address = (input(" Enter your Address : "))
mob_no = int(input(" Enter your mobile no : "))
print("---------------------------------------")
p1 = int(input(" Enter your Paper 1 marks : "))
p2 = int(input(" Enter your Paper 2 marks : "))
p3 = int(input(" Enter your Paper 3 marks : "))
p4 = int(input(" Enter your Paper 4 marks : "))
p5 = int(input(" Enter your Paper 5 marks : "))

tot=p1+p2+p3+p4+p5
per=tot/5

# if per>=35:
#     Result="Pass"
# else:
#     Result="Fail"
print(" Student Record has Saved Successfully. ")
f.close()