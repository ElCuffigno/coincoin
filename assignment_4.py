# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.

def normal_func(funco):
    return(funco(5))

''' EXAMPLE

def transform_data(fn):
    print(fn(10))

'''

# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.

print(normal_func(lambda a: a + 5))


''' EXAMPLE
transform_data(lambda data: data / 5)

'''
# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.     

def normal_func(funco, *args):
    if not args:
        return "Needs Arguments!"
    else:
        for arg in args:
            print(funco(arg))
            

''' EXAMPLE

def transform_data2(fn, *args):
    for arg in args:
        print(fn(arg))

transform_data2(lambda data: data / 5, 10 15, 22, 30)

'''

# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
def normal_func(funco, *args):
    if not args:
        return "Needs Arguments!"
    else:
        for arg in args:
            answer = funco(arg)
            print(f'{answer:^20f}')

normal_func(lambda a: a + 5, 1,2,3,4)



''' EXAMPLE

def transform_data3(fn, *args):
    for arg in args:
        print('Result: {:^20.2f}'.formatfn(arg))

transform_data3(lambda data: data / 5, 10 15, 22, 30)

'''
            