import random
import matplotlib.pyplot as plt
import math
steps = 1000
 
nc = 0
n = 0
x_inside = []
y_inside = []
x_outside = []
y_outside = []

for i in range(steps):
 
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)
 

    inside_circle= rand_x**2 + rand_y**2
 

    if  inside_circle <= 1:
        nc += 1
        x_inside.append(rand_x)
        y_inside.append(rand_y)
    else :
        x_outside.append(rand_x)
        y_outside.append(rand_y)
 
    n += 1
 
pi = 4 * nc / n
 
print("number of points inside the circle", nc)
print("Approximation of π=", pi)
print("Builtin constant π ",math.pi)
fig, ax = plt.subplots()
ax.scatter(x_inside, y_inside, color='b')
ax.scatter(x_outside, y_outside, color='r' )
plt.show()