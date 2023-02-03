# -*- coding: utf-8 -*-
"""Teachnook - Assignment 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1avlU9lfq-0GKCZ5BjzvrsnoT35SBD0qY




**Assignment 1**

**Create two different types of  examples for collective datatypes in python**

**Collective data types**

**1. List**

**2. tuple**

**3. dictionary**

**4. set**
"""

# list -> mutable, ordered, []

mylist1 = [1,2,3,"class",3.45,"house",False]
mylist2 = [5,6,7,8,"school",5.5,"building",True]

#concatenation 
 
print("the concatenated list is ",(mylist1+mylist2))

# indexing 

print(mylist1[-3])
print(mylist1[3])

# updating 

print(mylist2)
mylist2[-3] = 6.789
print('The value of mylist2 is',mylist2)

# appending & Inserting

mylist2.append("delta")
print('The value of mylist2 is',mylist2)
mylist2.insert(2,"alpha")
print('The value of mylist2 is',mylist2)

#del (pop,remove)

print(mylist2)
del mylist2[-4]
print(mylist2)

# tuple  -> immutable, ordered, ()

mytuple1 =(1,2,3,"class",3.45,"house",False)
mytuple2 = (5,6,7,8,"school",5.5,"building",True)

# tuple does not have extend,append,insert or delete 

# concatenation of 2 tuples work
print('The concatenated value of mytuple1+2 is',(mytuple1+mytuple2))
print()
mytuple3 = mytuple1+mytuple2
print(mytuple3)
print(type(mytuple3))

# Dictionary -> {key:value} , ordered
# values can only be changed using the keys

mydict1 = {"name":"suhas","age":20,"type":"work"}

# updating

mydict1["name"] = ["suhas","joshua","sohan","ujval"]
print(mydict1)

# Adding a new key/value pair with a tuple 
mydict1["health"] = ("good","bad")
print("The updated value after changing the key/value pair is ", mydict1)

# dictionary does not have append,extend,insert,remove

# deleting values from a dictionary

del mydict1["health"]
# mydict1.pop("health")
print(mydict1)

# set -> {}, Unordered, cant be indexed,
# important point -> does not contain any duplicate values.

myset = {'net','free',12,300.96,12,False,96,12,"net"}
print(myset)

# Add -> used in place of append
# set does not have -> extend,insert,append

myset.add("true")
print(myset)

# Union -> used in place of extend(adding 2 sets of data)
# union -> |
set1 = {1,2,3,4}
set2 = {4,5,6,7}
set3 = {7,8,9,0,100,200}

set4 = set1|set2|set3 
print(type(set4))
print(set4)

# inetsection -> & 
# only get the common data in all the sets

# set5 = set1&set2
set5 = set1.intersection(set2)
print(set5)
