# 1) Create a list of names and use a for loop to output the length of each name (len() ).
# 2) Add an if  check inside the loop to only output names longer than 5 characters.
# 
# 3) Add another if  check to see whether a name includes a “n”  or “N”  character.
#       Recommends using "in" keyword to check for n, could also output name 
# 4) Use a while  loop to empty the list of names (via pop() )
#       condition should ensure the loop exists once the list is empty.

NAMES_LIST = ['Thomas', 'Joanna', 'Malcolm', 'Declan', 'Bob']

def name_processor():
    for name in NAMES_LIST:
        if len(name) > 5 and ('n' or 'N') in name:
            print(name + ' ' + str(len(name)))
        

name_processor()