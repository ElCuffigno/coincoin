# Assignment 1 involving variables and functions

name = input('What is your name? ')
age = input('What is your age? ')

def print_name_age():
    """ Prints the input variables """
    print('My name is ' + name + ' and I am ' + age + ' years old.' )


def print_any(person_name, person_age):
    """ Accepts 2 variables to print 1 string 
    
    Arguments:
        :person_name: a string
        :person_age: an integer """
    print('My name is ' + person_name + ' and I am ' + person_age + ' years old.' )


def decades_lived(my_age):
    """ Returns decades lived in age """
    return(int(my_age) // 10)


print_name_age()

print_any(name, age)

print(decades_lived(age))
