# program to return random number in range
# author glen gardiner

# import he random module
import random
# using random to return a random int between 1 - 10 inclusive
number = random.randint(1, 10)
# print number 
print("random number is {} ".format(number))
# get user input string, cast to int
n = int(input("Enter integer: "))
# use random, randrange to take single int crateing range between & int inclusive
rdm = random.randrange(n)
# print rdm
print(rdm)
