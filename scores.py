#program to display a grading system
sub1=int(input("enter score obtained in sub1:"))
sub2=int(input("enter score obtained in sub2:"))
sub3=int(input("enter score obtained in sub3:"))
scores=((sub1+sub2+sub3)/3)
if scores >= 70 and scores <= 100:
    print("A")
elif scores >= 60 and scores <= 69:
    print("B")
elif scores >= 50 and scores <= 59:
    print("c")
elif scores >= 40 and scores <= 49:
    print("D")
elif scores >= 0 and scores <= 39:
    print("E")
else:
    print("fail")





