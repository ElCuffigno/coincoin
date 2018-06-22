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


def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
    return float(input("Your transaction amount please: "))

# Get the first transaction input and add the value to the blockchain
tx_input = get_user_input()
add_value(tx_input)

while True:
    tx_input = get_user_input()
    add_value(tx_input, get_last_blockchain_value())

# Output the blockchain list to the console
for block in blockchain:
    print('Outputting block')
    print(block)

print('done!')
