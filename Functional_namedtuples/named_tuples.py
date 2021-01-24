from collections import namedtuple

print("===============Creation and attributes================")
MyTuple = namedtuple("MyTuple", "x y z") # The attributes can be either a list,tuple or a string separated with a whitespace or ','
print(MyTuple) # Get the representation and equality for free
# Getting the fields
print(MyTuple._fields)
t1 = MyTuple(1, 2, 1)
print(t1.count(1)) # Returns the number of occurences of a value
print(t1._asdict()) # Returns the tuple  as an ordereddict
print("===================Accessing fields================")
print(t1.x) # By passing the attribute name
print(t1[1]) # By indexing
print(t1[:2]) # With slicing
a, *_ = t1 # With extended unpacking
print(a)
print("=============Replacing the values======================")
t1 = t1._replace(x=10, y=20) # The cleanest way to replace some of the values
print(t1)
new_values = 30, 30, 30
t2 = t1._make(new_values)
print(t2)

print("========Extending the fields and values============")
# The cleanest way is by getting the fields from the base tuple and extend them
MyExtTuple = namedtuple("MyExtTuple", MyTuple._fields + ('a', 'b'))
print(MyExtTuple._fields)
t1_ext = MyExtTuple(*t1, 500, 1000) #Pass the values from the previous tuple and add the new ones
print(t1_ext)