from person import Person
import time
from matplotlib import pyplot as plt
from numba import njit

def main():
	
	purepythontime= []
	clibrarytime= []
	numbatime=[]
	nlist = [30,35,36,37,40,41] 
	for n in nlist:
		print("for n=",n)
		#Runnning with pure python
		time_start1 = time.perf_counter()
		result = fib_py(n)
		time_stop1 = time.perf_counter()
		purepythontime.append(time_stop1-time_start1)
		print("For n=",n,"in pure python time required is ",time_stop1-time_start1)

		#Running with numba 
		time_start2 = time.perf_counter()
		result = fib_numba(n)
		time_stop2 = time.perf_counter()
		numbatime.append(time_stop2-time_start2)
		print("For n=",n,"in python using numba time required is ",time_stop2-time_start2)

		#Running with C++
		time_start3= time.perf_counter()
		f = Person(n)
		f.fib()
		time_stop3= time.perf_counter()
		clibrarytime.append(time_stop3-time_start3)
		print("For n=",n,"in python using c++ time required is ",time_stop3-time_start3)
		print()
		
	plt.plot(nlist, purepythontime, color = 'red', label = "Python")
	plt.plot(nlist, numbatime, color = 'blue', label = "Numba")
	plt.plot(nlist, clibrarytime, color = 'green', label = "C++")
	plt.xlabel("Fibonacci number n")
	plt.ylabel("Time (s)")
	plt.legend()
	plt.xlim(30, 45)
	plt.show()
	plt.savefig('timeplot.png')

	# time_start = time.perf_counter()
	# f = Person(47)
	# result = f.fib()
	# time_stop = time.perf_counter()
	# print("C++ Fibonacci Execution  /n", "The result is = ", result, "Time elapsed = ", time_stop-time_start, "seconds")
	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	"Output in terminal for n=47 with C++ execution                                                     "
	"C++ Fibonacci Execution  /n The result is =  -1323752223 Time elapsed =  20.691632530999414 seconds"
	"                                                                                                   "
	"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2)) 

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2)) 


if __name__ == '__main__':
	main()