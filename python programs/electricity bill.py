u=int(input(" Enter no. of unit Consumed by you in a month : "))

if u<=50:
    pay=u*2.5+0.36
    print(" Your Billing Amount is Rs. ",pay)
elif 50<u<=150:
    pay=u*5.5+0.36
    print(" Your Billing Amount is Rs. ",pay)
elif 150<u<=300:
    pay=u*7.5+0.36
    print(" Your Billing Amount is Rs. ",pay)
elif 300<u<=500:
    pay=u*10+0.36
    print(" Your Billing Amount is Rs. ",pay)
elif u>500:
    pay=u*15+0.36
    print(" Your Billing Amount is Rs. ",pay)