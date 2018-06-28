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
