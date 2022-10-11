"""
Solutions to module 2 - A calculator
Student: Stefanos Tsabanakis
Mail:stefanos.tsabanakis@gmail.com
Reviewed by:Benjamin Verbeek
Reviewed date: 23/9/2022
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)
class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

def statement(wtok, variables):
    result = assignment(wtok, variables)
    if wtok.has_next(): 
        raise SyntaxError('Unexpected token')
    return result

def arglist(wtok, variables):
    wtok.next()
    result =[] + [assignment(wtok, variables)]
    while wtok.get_current() == ',':
        wtok.next()
        result =result + [assignment(wtok, variables)]
    return result

def assignment(wtok, variables):
    result = expression(wtok, variables)
    while wtok.get_current()=="=":
        wtok.next()
        if wtok.is_number():
            raise SyntaxError("Expected variable after '='")
        else :
            variables[wtok.get_current()]=result
            wtok.next()
    else:
        return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current()=='-':
        if  wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        if wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/' or  wtok.get_current() == '//':
        if wtok.get_current() == '*': 
            wtok.next()
            result = result * factor(wtok, variables)
        elif wtok.get_current() == '/':
            wtok.next()
            try:
                result = result / factor(wtok, variables)
            except:
                raise EvaluationError("Division by zero")
        elif wtok.get_current() == '//':
            wtok.next()
            result = result // factor(wtok, variables)
    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
    elif wtok.get_current() == '-': 
        wtok.next()
        result = -1*factor(wtok, variables)
    elif wtok.get_current() in variables:
        result=variables[wtok.get_current()]
        wtok.next() 
    elif wtok.get_current() in function2:
        wtok.next()
        result=function2[wtok.get_previous()](arglist(wtok, variables))
        wtok.next()
    elif wtok.get_current() in function1:
        
        wtok.next()
        if wtok.get_current()=='(':
            try:
                result=function1[wtok.get_previous()](factor(wtok, variables))
            except:
                raise EvaluationError('must be integer =0')  
        else :
            raise SyntaxError('Expected a (')     
    elif wtok.is_number():  
        result = float(wtok.get_current())
        wtok.next()
    else:
        if wtok.is_name():
            raise  EvaluationError(f'Undefined variable : {wtok.get_current()} ')
        else:
            raise SyntaxError(
                "Expected number or '('")  
    return result

def fib(n,cache={}):
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
        cache[n] = result
        return result
def fac2(n):
    if (n // 1) == n and n>=0:
        return math.factorial((int(n)))
    else:
        raise EvaluationError('Amust be integer >=0')

    
def mean(n):
    return sum(n)/len(n)

function1={"sin": math.sin,"cos":math.cos,"log":math.log,"exp":math.exp,"fac":fac2,"fib":fib}
function2={"max":max,"min":min,"sum":sum,"mean":mean}

         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    function1={"sin": math.sin,"cos":math.cos,"log":math.log,"exp":math.exp,"fac":fac2,"fib":fib}
    function2={"max":max,"min":min,"sum":sum,"mean":mean}

    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current()=="vars":
            for i in variables :
                print(i,'\t', variables[i])
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except EvaluationError as se :
                print("*** Evaluation error: ", se)

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

 


if __name__ == "__main__":
    main()
