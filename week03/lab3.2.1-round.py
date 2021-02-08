# examples of rounding, floats & floats with decimal places
# author glen gardiner

# no change with int
int_to_round = int(input("Enter int to round: "))
rounded_int = round(int_to_round)
print( 'Int {} rounded is {}'.format(int_to_round, rounded_int))


# round up or down here
# example 3.59 -> 4
float_to_round = float(input("Enter float to round: "))
rounded_float = round(float_to_round)
print( 'Flaot {} rounded is {}'.format(float_to_round, rounded_float))

# to 1 decimal place 
# example 3.59 - 3.6
float_to_round = float(input("Enter float to round: "))
rounded_float = round(float_to_round, 1)
print('Flaot {} rounded is {}'.format(float_to_round, rounded_float))



