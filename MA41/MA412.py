import numpy
import functools
import math
import random 



def highorderV(n,d):
    n1=0
    for j in range(n):
        x_random=[random.uniform(-1, 1) for i in range(d)]
        sum_of_x_random=functools.reduce(lambda x,y:x+y,map(lambda x:x**2,x_random))
        if sum_of_x_random<=1:
            n1+=1
    Vmontecarlo=(2**d)*n1/n
    Vexact=((math.pi)**(d/2))/math.gamma(d/2+1)       
    print("the theoretical V for for d=",d,"is",Vexact)
    print("the monte carlo approximation for n=",n,"and d=",d,"is",Vmontecarlo)
    return Vmontecarlo   
highorderV(100000,2)
print()
highorderV(1000000,11)
# the theoretical V for for d= 2 is 3.141592653589793
# the monte carlo approximation for n= 100000 and d= 2 is 3.15128

# the theoretical V for for d= 11 is 1.8841038793898994
# the monte carlo approximation for n= 1000000 and d= 11 is 1.9968