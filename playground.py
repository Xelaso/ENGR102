from math import *
four = int(input('Enter a four digit integer: '))
p = int(input('Enter an integer value for P: '))
a = four // 1000
b = (four % 1000) // 100
c = ((four % 1000) % 100) // 10
d = four % 10

pdi = a ** p + b ** p + c ** p + d ** p
if(pdi == four):
    print(four, "with p:", p, 'is a PDI because', pdi)

