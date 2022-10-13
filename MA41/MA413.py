
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
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
    return Vmontecarlo



if __name__ == "__main__":
    start=pc()
    V=highorderV(10000000,11)
    end=pc()
    print(f"Time required without multiprocessing is {round(end-start, 2)} seconds")
    print("Calculated V without multiprocessing:",V)

    start=pc()
    k=0
    with future.ProcessPoolExecutor() as ex :
        p=[1000000 for i in range(10)]
        L=[11 for i in range(10)]
        results=ex.map(highorderV,p,L)

        for r in results:
            k+=r
            
    end=pc()
    print(f"Time required with multiprocessing is {round(end-start, 2)} seconds")
    print("Calculated V without multiprocessing:",k/10)
# Time required without multiprocessing is 45.68 seconds
# Calculated V without multiprocessing: 1.8581504
# Time required with multiprocessing is 15.59 seconds
# Calculated V without multiprocessing: 1.8673663999999999