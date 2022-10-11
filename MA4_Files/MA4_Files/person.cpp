#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fib();
	private:
		int age;
		int _fib(int);
	};
 
Person::Person(int n){
	age = n;
	}
int Person:: fib (){
	int n=age;
	return _fib(n);
}
int Person :: _fib(int n){
	if (n <= 1)
        return n;
    return _fib(n - 1) + _fib(n - 2);
}
int Person::get(){
	return age;
	}
 

void Person::set(int n){
	age = n;
	}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	int Person_fib(Person*person){return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}