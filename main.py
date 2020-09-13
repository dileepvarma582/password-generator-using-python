#password generator in python
from random import randint,shuffle
u1=chr(randint(65,90))
u2=chr(randint(65,90))
l1=chr(randint(97,122))
l2=chr(randint(97,122))
d1=str(randint(0,9))
d2=str(randint(0,9))
d3=str(randint(0,9))
p1=chr(randint(33,47))
p2=chr(randint(33,47))
s=u1+u2+l1+l2+d1+d2+d3+p1+p2 
s=list(s)
shuffle(s)
s="".join(s)
print("The password generated is: ",s)
