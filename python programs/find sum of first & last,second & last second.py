list=[]
num=int(input(" Enter Size of List : "))

for i in range(0,num):
    ele=int(input())
    list.append(ele)
if num%2!=0:
    print(" Wrong Input Only Even numbers are allowed. ")
elif num%2==0:
    i=0
    while i<num:
        add=list[i]+list[num-1]
        i+=1
        num-=1
        print("Sum is : ",add)
    # fd=int(list[0])   #first character of string of is num[0] is converted into integer type so we get first digit.
    # ld=int(list[-1])  #last character of string of is num[-1] is converted into integer type so we get last digit.
    # sd=int(list[1])   #Second character of string of is num[1] is converted into integer type so we get second digit.
    # sld=int(list[-2]) #Secondlast character of string of is num[-2] is converted into integer type so we get secondlast digit.
    # td=int(list[2])   #Third character of string of is num[2] is converted into integer type so we get Third digit.
    # tld=int(list[-3]) #Thirdlast character of string of is num[-3] is converted into integer type so we get thirdlast digit.
    # add=fd+ld
    # add1=sd+sld
    # add2=td+tld
    # print("Addition of First & Last Digit is : ",add)
    # print("Addition of Second & SecondLast Digit is : ",add1)
    # print("Addition of Third & ThirdLast Digit is : ",add2)
