def unlimited_arguments(*args):
    print(args)
    for argument in args:
        print(argument)

unlimited_arguments(1,2,3,4)

# Python will create a tuple of arguments to run into a function with a * before an argument)

# Below, we can do the same but by making a list of arguments get passed through one by one

def unlimited_arguments(*args):
    print(args)
    for argument in args:
        print(argument)

unlimited_arguments(*[1,2,3,4])

print('Some text: {} {}'.format(1,2))
a = [1, 2, 3]

print('Some text: {} {} {}'.format(*a))

# Passing through a dictionary with keywords
def unlimited_arguments(*args, **kwargs):
    print(kwargs)
    for argument in kwargs:
        print(argument)

unlimited_arguments(1,2,3,4, name='Tom', age = 33)


# Passing through a dictionary with keywords and arguments
def unlimited_arguments(*args, **kwargs):
    print(kwargs)
    for k, argument in kwargs.items():
        print(k, argument)

unlimited_arguments(1,2,3,4, name='Tom', age = 33)