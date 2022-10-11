from person import Person
import time
from matplotlib import pyplot as plt
import numba 

def main():
	
	pythonTimes = []
	cplusplustimes = []
	nlist = [30,35,36,37] # enter 30,40,45 for the long run
	for n in nlist:
		# #Runnning with pure python
		# time_start1 = time.perf_counter()
		# result = fib_py(n)
		# time_stop1 = time.perf_counter()
		# #pythonTimes.append(time_stop1-time_start1)
		# print("For n=",n,"time passed is ",time_stop1-time_start1)
		#Running with C++
		time_start2 = time.perf_counter()
		f = Person(n)
		f.fib()
		time_stop2 = time.perf_counter()
		print("n is", n)
		cplusplustimes.append(time_stop2-time_start2)
		print("C++ Fibonacci Execution /n", "The result is = Time elapsed = ", time_stop2-time_start2, "seconds")
	# print("The length of the lists is", len(pythonTimes))
	# #print(pythonTimes)
	# plt.plot(nlist, pythonTimes, color = 'red', label = "Python")
	# plt.plot(nlist, cplusplustimes, color = 'blue', label = "C++")
	# plt.xlabel("Fibonacci number n")
	# plt.ylabel("Time (s)")
	# plt.legend()
	# plt.xlim(0 , 45)
	# plt. ylim(0, 120)
	# plt.show()
	# plt.savefig('timeplot6.png')

	# #C++ Fibonacci Execution  /n The result is =  -1323752223 Time elapsed =  57.004970107926056 seconds
	# #the number is longer than int
	# #Fibonacci Calculation 47
	# time_start = time.perf_counter()
	# f = Integer(47)
	# result = f.fib()
	# time_stop = time.perf_counter()
	# print("C++ Fibonacci Execution  /n", "The result is = ", result, "Time elapsed = ", time_stop-time_start, "seconds")
def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2)) 


if __name__ == '__main__':
	main()