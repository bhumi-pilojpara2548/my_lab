Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print("hello atmiya university..")
hello atmiya university..
#sum
a=input("enter a value : ")
enter a value : 8
b=input("enter a value: ")
enter a value: 7
result=int(a)+int(b)
print(result)
15
#odd even
num=int(input("enter a value: "))
enter a value: 8
if(num%2==0):
    print("This number is even.")
else:
    print("This number is odd.")

    
This number is even.
#leap year
year=int(input("enter a year: "))
enter a year: 2028
if(year%4==0 and year%100!=0):
    print("Leap year.")
else:
    print("Not a leap year.")

    
Leap year.
#pi value
import math
print(math.pi)
3.141592653589793
#print constant value
a=10
print(a)
10
#square of number
num=int(input("enter a number: "))
enter a number: 12
square=num*num
print("square=",square)
square= 144
#area of circle
import math
r=float(input("enter radius: "))
enter radius: 55
area=math.pi * r * r
print("area of circle=",area)
area of circle= 9503.317777109125
#cheak data type
a=input("enter anything: ")
enter anything: 48
print(type(a))
<class 'str'>
>>> #use math function
>>> import math
>>> print("square root:",math.sqrt(25))
square root: 5.0
>>> #find power
>>> print("power:",math.power(2,3))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print("power:",math.power(2,3))
AttributeError: module 'math' has no attribute 'power'
>>> print("power:",math.pow(2,3))
power: 8.0
>>> #positive negative
>>> n=int(input("enter number: "))
enter number: 45
>>> if n > 0:
...     print("positive number.")
... elif n < 0:
...     print("negative number.")
... else:
...     print("Zero.")
... 
...     
positive number.
