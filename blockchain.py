# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain to the blockchain

    Arguments: 
        :transaction_amount: the amount that should be added
        :last_transaction: the Last blockchain transaction
    """
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

# Get the first transaction input and add the value to the blockchain
tx_input = get_transaction_value()
add_value(tx_input)

while True:
    print("please choose")
    print("1: Add a new transaction value")
    print("2: Output blockchain blocks")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else: 
        print_blockchain_elements()

  

print('done!')
