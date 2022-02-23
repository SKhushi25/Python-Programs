p1=int(input(" Enter Age of First Person  : "))
p2=int(input(" Enter Age of Second Person : "))
p3=int(input(" Enter Age of Third Person  : "))
    #Oldest among three persons:
if p1>p2 & p1>p3:
    print(" Oldest : ",p1)

elif p2>p1 & p2>p3:
    print(" Oldest : ",p2)
   
else:
    print(" Oldest :",p3)

    #youngest among three persons:
if p1<p2 & p1<p3:
    print(" Youngest : ",p1)
    
elif p2<p1 & p2<p3:
    print(" Youngest : ",p2)
    
else:
    print(" Youngest :",p3)