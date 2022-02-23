a=int(input(" Enter any digit number : "))

n=str(a)    #Converting Number into String.

fd=int(n[0])   #first character of string of is a[0] is converted into integer type so we get first digit.
ld=int(n[-1])  #last character of string of is a[-1] is converted into integer type so we get last digit.

add=fd+ld

print(add)