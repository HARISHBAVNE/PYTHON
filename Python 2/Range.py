# Python code to demonstrate range() vs xrange()
# on  basis of return type
  
# initializing a with range()
a = list(range(1,10000))
  
# initializing a with xrange()
x = range(1,10000)
  
# testing the type of a
print ("The return type of range() is : ")
print (type(a))
  
# testing the type of x
print ("The return type of xrange() is : ")
print (type(x))

Z = []
import sys
print(sys.getsizeof(Z))
