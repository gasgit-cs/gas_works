# terminal program to multiply 2 numbers
# author: glen gardiner

# version 1
# multiply 111 x 555 and assign it to a var answer
answer = 111 * 555
# print var answer to terminal
print("V1: " + str(answer)) 

# version 2
# assign values to x, y and multiply , assign value to ans and print
x = 111
y = 555
ans = x * y
print("V2: " + str(ans))

# version 3
# create function with arguments, calculation andprint statement
def multiply_xy(x, y):
    answer = x * y
    print("V3: " + str(answer))
# call function passing  sargs 111, 555
multiply_xy(111, 555)

#version 4
# create function to get user input, calculate and print statement
def multiply_xy_from_input():
    a = int(input("Enter value a: "))
    b = int(input("Emnter value b: "))
    answer = a*b
    print("V4: " + str(answer))
# call fuunction
multiply_xy_from_input()



   


