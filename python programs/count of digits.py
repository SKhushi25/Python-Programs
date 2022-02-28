num=int(input(" Enter any numbers : "))

count=0
while(num>0):
    num//=10    #12345/10 = 1234
    count+=1
print(" Numbers of Digits Entered by you is : ",count)