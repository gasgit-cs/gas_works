# program to takes string inputs x, y  from user,  cast to int
# divide and print result as int
# use modulo to print remainder
# author glen gardiner


# get first string input, cat to int and assign to var x
x = int(input("Enter first nmuber: "))
# get second string input, cat to int and assign to var y
y = int(input("Enter second nmuber: "))
# divide x by y assigning the int value to answer
answer = x // y
# calulate the remiander using modulo 
remainder = x % y
# print both division result and remainder
print("{} divided {} is {} with remainder {} ".format(x , y, answer, remainder))
