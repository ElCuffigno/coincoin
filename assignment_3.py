# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
# 3) Use a list comprehension to check whether all persons are older than 20.
# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
# 5) Unpack the persons of the original list into different variables and output these variables.

persons = [
    {
        'name': 'Bob',
        'age': 35,
        'hobbies': ['golf', 'reading', 'skiing']
    },
    {
        'name': 'Nacho',
        'age': 23,
        'hobbies': ['futbol', 'barbering']
    },
    {
        'name': 'Thorborg',
        'age': 3,
        'hobbies': ['drawing', 'colors', 'planes', 'yelling']
    }
]

print(persons)

names = [el['name'] for el in persons]

print(names)

age_check = [el['age'] > 20 for el in persons]

print(all(age_check))



def deeper_copy(list):
    new_list = []
    for el in list:
        # returns new dict with keys and values of old list, but not referencing old list
        new_dict = dict((k,v) for k,v in el.items())
        new_list.append(new_dict)
    return new_list


copy_persons = deeper_copy(persons)
print(copy_persons)
copy_persons[0]['name'] = 'Harold'
print(copy_persons)
print(persons)

a, b, c = persons

print(a, b, c)
print(c)
