# programe to create 5 var types and print to terminal using the type function
# author glen gardiner

# create variable type int, assign 5
i = 5
# create variable type float, assign 5.0
fl = 5.0
# create boolean, set True
is_five = True
# create var string, assign 'five little ducks'
s = "five little ducks"
# create list
my_list = ["one","two", "three", "four", "five"]


# print variable types using the type function and format
print('variable {} is type:{} and value:{}'.format( 'i', type(i), i))
print('variable {} is type:{} and value:{}'.format( 'fl', type(fl), fl))
print('variable {} is type:{} and value:{}'.format( 'is_five', type(is_five), is_five))
print('variable {} is type:{} and value:{}'.format( 'memo', type(s), s))
print('variable {} is type:{} and value:{}'.format( 'my_list', type(my_list), my_list))

