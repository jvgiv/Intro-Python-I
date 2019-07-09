"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
str_one = "x is "
str_two = '%d' % (x) 
str_three = ", y is "
str_four = '%f' % (y)
str_five = ", z is "
str_six = '%s' % (z)
str_seven = str_one + str_two + str_three + str_four + str_five + str_six
print(str_seven) 


# Use the 'format' string method to print the same thing
print("x is %d, y is %f, z is %s" % (x, y, z))

# Finally, print the same thing using an f-string
print("x is {}, y is {}, z is {}".format(x, y, z))