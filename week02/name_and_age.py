# program to get user input, name andage and print
# author glen gardiner


# get user name as inpput
user_name = input("Enter your name: ")
# create var and assign string with place holder
txt_name = "Name: {}"
# print string with placeholder using format and var user_name
print(txt_name.format(user_name))


# get user age as inpput
user_age = input("Enter your age: ")
# create var and assign string with place holder
txt_age = "Age: {}"
# print string with placeholder using format and var user_age
print(txt_age.format(user_age))

# create message string with placeholders
txt_message = "Hello {}, your age is {}"
# print string with placeholders using format and vars user_name, user_age
print(txt_message.format(user_name, user_age))

# create var with placeholders and tab to format
txt_message_tab = "Hello {},\t your age is {}"
# print string with placeholders using format and vars user_name, user_age
print(txt_message_tab.format(user_name, user_age))





