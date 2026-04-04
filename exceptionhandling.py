"""try:
   number1=int(input("enter a number: "))
   number2=int(input("enter another number: "))
   result=number1/number2
except ZeroDivisionError:
    print("you can not divide by zero")
except ValueError:
    print("please enter a valid number")
else:
    print("division successful result is: ",result)
finally:
    print("thids block is always runs.")"""

try:
    my_list = [1, 2, 3]
    print(my_list[1])
except IndexError:
    print("index is out of range!")
else:
    print("element found successfully..!")
finally:
    print("program finished.")