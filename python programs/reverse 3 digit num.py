num=int(input(" Enter any 3 digit number : "))

a=num%10
num=num/10
b=num%10
num=num/10
c=num

print(a*100+b*10+c*1)