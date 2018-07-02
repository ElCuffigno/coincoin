simple_list = [1,2,3,4]
simple_list.extend([5,6,7])
print(simple_list)
del(simple_list[0])
# or del simple_list[0]
print(simple_list)

d = {'name': 'Max'}
#Get tuple of keys and values in dict
print(d.items())
# iterate over keys/values and print themS
for k, v in d.items():
    print(k,v)
del(d['name'])
print(d)

t = (1,2,3)
print(t.index(1))
#tuples are immutable and have no "del" function

s = {'Max', 'Anna', 'Max'}
# Redundant method not included
# use IDE autocomplete to see methods (s.)
print(s)
# del doesn't work for sets

new_list = [1, 2, 3, -5]
any(new_list)
# should return True

# returns false
all(new_list)

number_list = [1, 2, 3, -5]
#list comprehension to check for positive numbers
[el for el in number_list if el > 0]
# returns [1, 2, 3]

[el > 0 for el in number_list if el > 0]
# returns booleans for list [True, True, True]

# We can use any or all with list comprehension
[el > 0 for el in number_list]
# returns [True, True, True, False]

all([el > 0 for el in number_list])
# returns False