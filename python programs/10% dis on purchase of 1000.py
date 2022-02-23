p=int(input(" Enter Total no. of Products you buy : "))

t=p*100   #Total Cost of all Products brought by user.
q=t*0.1   #10% Discount on the Products Cost.
t1=t-q    #Total cost after Applying discount.

if t>1000:
    print(t1)
else:
    print(t)