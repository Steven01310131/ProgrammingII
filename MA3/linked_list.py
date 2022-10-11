""" linked_list.py

Student:stefanos tsampanakis
Mail:stefanos.tsabanakis@gmail.com
Reviewed by:Mikel
Date reviewed:5/10
"""


from re import I


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):
        sum=0
        if self.first==None:
            return sum
        else:
            f=self.first
            while f:
                sum+=1
                f=f.succ

        return sum

    def mean(self):
        sum1=0
        sum2=0
        f=self.first
        while f:
            sum1+=1
            sum2=sum2+f.data
            f=f.succ
        return sum2/sum1
        pass

    def remove_last(self):
        if self.first==None:
            return None 
        elif self.first.succ==None:
            x=self.first.data
            self.first=None
            return x
        elif self.first.succ.succ==None:
            x=self.first.succ.data
            self.first.succ=None
            return x
        else :   
            f=self.first
            while f:
                f=f.succ
                if f.succ.succ==None:
                    x=f.succ.data
                    f.succ=f.succ.succ
                    return x

    def remove(self, x):          
        if self.first.data==x:
            self.first=self.first.succ
            return True
        else :
            f=self.first
            while f.succ:
                if f.succ.data==x:
                    f.succ=f.succ.succ
                    return True
                f=f.succ
            return False
    def count(self, x):           
        if self.first.data==x and self.first.succ==None:
             return 1
        elif self.first.data!=x and self.first.succ==None:
            return 0
        else:
            return  self._count( x, self.first)
    def _count(self,x,f):
        if f.succ==None and f.data==x:
            return 1
        elif f.succ==None:
            return 0
        elif f.data==x :
            return 1 + self._count(x,f.succ)
        else:
            return self._count(x,f.succ)      


    def to_list(self):           
        return self._to_list(self.first )

    def _to_list(self,f):
        if f is None:
            return []
        else :
            return [f.data] + self._to_list(f.succ)



    def remove_all(self, x):
        if self.first.data==x and self.first.succ==None:
             self.first=None 
             return self.first
        elif self.first.data==x:
            self.first=self.first.succ
            return self.remove_all(x)
        elif self.first.data!=x and self.first.succ==None:
            return self.first
        else:
            return  self._remove_all( x, self.first)
    def _remove_all(self,x,f):
        if f.succ==None:
            return 
        elif f.succ.data==x :
            f.succ=f.succ.succ
            return self._remove_all(x,f)
        else :
            f=f.succ
            return self._remove_all(x,f)

    def __str__(self):         
        result='('
        f=self.first
        if f!=None:
            result += str(f.data)
            f=f.succ
            while f:
                result += ','+' ' + str(f.data)
                f=f.succ
        result += ')'
        return result          

    def copy(self):               # Compulsary
        result = LinkedList()
        for x in self:
            
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
    the complexity is O(n**2) becauce we are inserting in a linked list and looping
    '''

    def copy(self):   
        result = LinkedList()            # Compulsary
        if self.first is None:
            return result
        else:
            f = self.first
            result.first = LinkedList.Node(f.data, None)
            r = result.first
            while f.succ:
                r.succ = LinkedList.Node(f.succ.data, None)
                r = r.succ
                f = f.succ
            return result
    ''' Complexity for this implementation:
    Its just O(n) we are looping and just adding in the end of the linkedlist
    '''

    def __getitem__(self, ind):   
        if ind==0:
            return self.first.data
        else:
            f=self.first
            count=0
            while count<ind:
                f=f.succ
                count+=1
            return f.data

class Person:                
    def __init__(self, name, pnr):
            self.name = name
            self.pnr = pnr

    def __str__(self):
            return f"{self.name}:{self.pnr}"

    def __lt__(self,other):
            return self.name<other.name
    def __le__(self,other):
            return self.name<=other.name

def main():
    lst = LinkedList()
    for x in [ 3]:
        lst.insert(x)
    print(lst.length())
  

    # def remove_last(self): 
    #     if self.first==None:
    #         return None 
    #     if self.first.succ==None:
    #         self.first=None
    #         return None
    #     f=self.first
    #     while f.succ.succ:
    #         f=f.succ
    #     f.succ=None
    #     return self.first

    # def remove(self, x):
    #     if self.first.data==x:
    #         self.first=self.first.succ
    #     else :
    #         f=self.first
    #         while f.succ:
    #             if f.succ.data==x:
    #                 f.succ=f.succ.succ
    #                 return True
    #             f=f.succ
    #         return False



    x=lst.copy()
    x.print()


    

   
    
if __name__ == '__main__':
    main()
