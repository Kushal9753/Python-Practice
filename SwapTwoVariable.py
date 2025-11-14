''' using third variable '''

# x = int(input("enter the value of x:- "))
# y = int(input("enter the value of y:- "))

# z = x 
# x = y
# y = z

# print("the value of x is :- ",x,"\nthe value of y is :- ",y)



''' without third variable '''

# x = int(input("enter the value of x:- "))
# y = int(input("enter the value of y:- "))

# x = x + y
# y = x - y
# x = x - y

# print("the value of x is :- ",x,"\nthe value of y is :- ",y)


''' solution 3 '''

x = 12 
y = 74

x, y = y, x

print("the value of x is :- ",x,"\nthe value of y is :- ",y)

