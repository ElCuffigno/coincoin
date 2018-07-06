# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.

def normal_func(funco, *args):
    a, b = args
    return funco(a, b)

# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.

print(normal_func(lambda a, b: a + b, *[1,2]))

# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.     

def normal_func(funco, *args):
    if not args:
        return "Needs Arguments!"
    elif len(args) == 1:
        return args
    else:
        for arg in args:
            


# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.