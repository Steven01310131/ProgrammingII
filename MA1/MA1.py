"""
Solutions to module 1
Student: Nils Tsabanakis
Mail:stefanos.tsabanakis@gmail.com
Reviewed by: David Meadon
Reviewed date: 6/9/2022
"""

import random
import time


def power(x, n):         # Optional
    pass


def multiply(m, n):      # Compulsory
    if n==0 or m==0 :
        return 0
    elif n==1 :
        return m
    else :
        return m+multiply(m,n-1)
    pass


def divide(t, n):        # Optional
    pass


def harmonic(n):  
    if n<2 :
        return 1
    else :
        return 1/n + harmonic(n-1)
    pass


def digit_sum(x):        # Optional
    pass


def get_binary(x):       # Optional
    pass


def reverse(s):          # Optional
    pass


def largest(a):
    if len(a)==1:
        return a[0]
    else :
        m=largest(a[1:])
        return m if m> a[0] else a[0]          # Compulsory
    pass


def count(x, s):
    if not s: 
        return 0
    elif x == s[0]:
        return 1 + count(x, s[1:])
    else:
        return 0 + count(x, s[1:])
    pass

def count(x, s):
    if not s: 
        return 0
    elif x == s[0]:
        return 1 + count(x, s[1:])
    elif type(s[0])==list:
        return count(x,s[1:])+count(x,s[0])
    else:
        return 0 + count(x, s[1:])
    pass


def zippa(l1,l2):
    if len(l1)==0 :
        return l2
    elif len(l2)==0 :
        return l1
    else:
        return [l1[0]]+[l2[0]]+zippa(l1[1:],l2[1:])
    pass


def bricklek(f, t, h, n):
    if n==0:
        return []
    else:
        return bricklek(f,h,t,n-1)+[f"{f}->{t}"]+bricklek(h, t, f, n-1)


def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    print('Bye!')
    

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  
  
  print(2**50-1)
  output : 1125899906842623
  
  
  
  Exercise 17: Time for Fibonacci:
  
  def fib ( n ) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fib ( n - 1 ) + fib ( n - 2 )


def calc(n):
    import time 
    tstart= time . perf_counter ()
    fib(n)
    tstop = time . perf_counter ()
    print ( " Measured time : { ",tstop - tstart," } seconds " )
    return tstop-tstart
a=calc(28)
b=calc(29)
c=calc(30)
d=calc(31)
e=calc(32)
f=calc(33)
g=calc(34)
print(b/a)
print(c/b)
print(d/c)
print(e/d)
print(f/e)
print(g/f)
#output:1.5694535928229845
#       1.6334630926984037
#       1.6172713364867481
#       1.5725007703333838
#       1.5382148319575288
#       1.587891429650756

second question
import time
def fib ( n ) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fib ( n - 1 ) + fib ( n - 2 )


tstart1= time . perf_counter ()
fib(35)
tstop1 = time . perf_counter ()
print ( " Measured time : { ",tstop1 - tstart1," } seconds " )
a=tstop1 - tstart1

def timecalc(q):
    if q==1:
        return 1.618
    else  :
        return 1.618*timecalc(q-1)

def apprtime(y,b) :
    if 60<y<3600 :
        print("To calculate the ",b," it will take ", y/60,"minutes")
    elif 3600<=y<86400 :
        print("To calculate the ",b," it will take ", y/60/60,"hours")
    elif 86400<=y<31536000 :
        print("To calculate the ",b," it will take ", y/60/60/24,"days")
    elif y>= 31536000 :
        print("To calculate the ",b," it will take ", y/60/60/24,"years")
    else :
        print ("To calculate the ",b," it will take ", y,"seconds")

apprtime(timecalc(15)*a,"f(50)")
apprtime(timecalc(65)*a,"f(100)")
#output:To calculate the  f(50)  it will take  9.025968919191898 hours
#       To calculate the  f(100)  it will take  10573248898.68548 years
  
  
  Exercise 20: Comparison sorting methods:
insertion sort t=c1*n^2
merge sort t=c2*n*log(n)
t=c1*f1000 t=1=>c1=1/10^6
t=c2*f1000 t=1=> c2=1/10^3*log(10^3)

for 10^ 6 random numbers
inserion: t=c1*n^2=10^6*10^6/10^6 => t=10^6 sec => t= 11.5740741 days
merge : t=c2*n*log(n)=10^6*6*log(10)/10^3*3*log(10) => t= 2*10^3 sec => t=33.33333 minutes

for 10^9 random numbers

insertion : t=10^18/10^6 => t=10^12 => t=31709.7919837646 years
merge :     t=10^9*9*log(10)/10^3*3*log(10) => t=3*10^6 sec => t=34.72222222 days

  
  
  
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
 algoritm A t=CA*f=> n=cA*n => cA=1
 algoritm B t=CB*f => t=c*log(n)*n

algorithm B  takes 1 second to solve a problem
when n = 10 so
1=c*log(10)*10 +=> c=1/(log(10)*10)
for tA<tB => n<log(n)*n/(log(10)*10)=>  10<log(n)=>n>10^10

  
  
  
  
  





"""