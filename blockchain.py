# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    #This only executes if the above is false
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]

def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain to the blockchain

    Arguments: 
        :transaction_amount: the amount that should be added
        :last_transaction: the Last blockchain transaction
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    user_input = float(input("Your transaction amount please: "))
    return user_input


def print_blockchain_elements():
    """ Output the blockchain list to the console"""
    for block in blockchain:
        print('Outputting block')
        print(block)

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input



while True:
    print("please choose")
    print("1: Add a new transaction value")
    print("2: Output blockchain blocks")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else: 
        print("Invalid input. Please select from list")
    print('Choice registered!')
  

print('done!')
