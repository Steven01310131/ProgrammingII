""" bst.py

Student:Stefanos Tsampanakis
Mail:stefanos.tsabanakis@gmail.com
Reviewed by: Mikel 
Date reviewed:5/10
"""


from linked_list import LinkedList
import random
import math


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

    def height(self):                             # Compulsory

        return self._height(self.root)

    def _height(self,r):
        
        if r is None:
         
            return 0
        else:

            return 1 + max(self._height(r.left),self._height(r.right))

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left =self._remove( r.left, k)
        elif k > r.key:
            r.right =  self._remove( r.right, k)
        else:  # This is the key to be removedel
            if r.left is None and r.right is None:
                r=None
            elif r.left is None:     # Easy case
                r.key=r.right.key
                r.right=r.right.right
            elif r.right is None:  # Also easy case
                r.key=r.left.key
                r.left=r.left.left
            
            else:  # This is the tricky case.
                temp=r.right
                while  temp.left :
                    temp=temp.left
                r.key=temp.key
                self._remove( r.right, r.key)

        return r  

    def __str__(self):  
        return '<' + str(list(self.__iter__()))[1:-1] + '>'
            

    def to_list(self):                            # Compulsory
        return list(self.__iter__())
        #complexity n 

    def to_LinkedList(self):                      # Compulsory
        newlst=LinkedList()
        if self.root is None:
            return newlst
        else:
            for i in self.__iter__():
                newlst.insert(i)
            return newlst

    def ipl(self):   
        return self._ipl(self.root,1)    

    def _ipl(self,r,level)   :                      
        if r is None :
            return 0
        else:
            return level + self._ipl(r.right, level+1) + self._ipl(r.left, level+1)
            

def random_tree(n): # Useful
    bst = BST()
    while n > 0:
        bst.insert(random.random())
        n = n-1
    return bst


def main():
    t = BST()
    k=BST()
    for x in [7,3,2,4,8,6,9]:
        t.insert(x)
    # k.print()
    # t.print()
    # print()
 
    # print('size  : ', t.size())
    # for k in [0, 1, 2, 5, 9]:
    #     print(f"contains({k}): {t.contains(k)}")
    # n=5000
    # bst1=random_tree(n)
    # print("For n=",n)
    # print("IPL/n is :",bst1.ipl()/n)
    # print("the height is :", bst1.height())
    # n=10000
    # bst2=random_tree(n)
    # print("For n=",n)
    # print("IPL/n is :",bst2.ipl()/n)
    # print("the height is :", bst2.height())
    # n=50000
    # bst3=random_tree(n)
    # print("For n=",n)
    # print("IPL/n is :",bst3.ipl()/n)
    # print("the height is :", bst3.height())
    # n=100000
    # bst4=random_tree(n)
    # print("For n=",n)
    # print("IPL/n is :",bst4.ipl()/n)
    # print("the height is :", bst4.height())

    n=1000
    k=1.39*(math.log2(n))
    print('For ',n,'approximated ipl/n:',k)
    # bst=random_tree(n)
    # print(bst.ipl())

    
if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================
Generators create iterable objects, they are memory 
efficient as they require less space to storage. 
They generate the requested values on the spot instead of calculating and storing.
But its required to strart looping from the start which could not be efficient for large lists

1. computing size? Yes
2. computing height? No because we need to know the structure
3. contains? Yes
4. insert? No because we need to know the structure
5. remove? No because we need to know the structure




Results for ipl of random trees
===============================
For n= 50
IPL/n is : 6.28
the height is : 10
For n= 100
IPL/n is : 8.25
the height is : 15
For n= 200
IPL/n is : 8.46
the height is : 16
For n= 1000
IPL/n is : 12.171
the height is : 22
For n= 10001
IPL/n is : 16.25947405259474
the height is : 32
For n= 5000
IPL/n is : 14.6516
the height is : 26
For n= 10000
IPL/n is : 15.887
the height is : 28
For n= 50000
IPL/n is : 20.70042
the height is : 37
For n= 100000
IPL/n is : 21.39659
the height is : 39

(1.39n n log 2 (n) + O(n) )/n =1.39log(n)
For  50 approximated ipl/n: 7.844960103786867
For  100 approximated ipl/n: 9.234960103786866
For  200 approximated ipl/n: 10.624960103786867
For  1000 approximated ipl/n: 13.8524401556803

We observe the rate of which height increases exponentially decreases.

The internal path length (IPL) changes as 1.39n n log 2 (n) + O(n) 
for large n we have  1.39n log 2 (n)

Calculated IPL =2176098  n=100000     Approximated: 2308740
Calculated IPL=26838015  n=1000000    Approximated: 27505564
Calculated IPL=141455012 n=5000000    Approximated: 154661801

We can see that the approximations are always in the same order of magnitude the slight differences we observeis produced from emmiting the O(n) . 

"""
