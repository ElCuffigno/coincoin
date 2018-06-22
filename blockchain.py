# Initializing our blockchain list
genesis_block = {
    'previous_hash' : '', 
    'index': 0, 
    'transactions' : []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Tom'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    # This only executes if the above is false
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction( recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain to the blockchain

    Arguments: 
        :sender: sender of the coins
        :recipient: recipient of the coins
        :amount: The amount of coins sent with transaction, default = 1.0
    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    """
    Simplified minding function, adds dict of block to chain, 
    including open transactions
    """
    last_block = blockchain[-1]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)

    block = {
        'previous_hash' : hashed_block, 
        'index': len(blockchain), 
        'transactions' : open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)



def print_blockchain_elements():
    """ Output the blockchain list to the console"""
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     # block_index used to find the correct block in the chain to check
    #     if block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index +=1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('please choose')
    print('1: Add a new transaction value')
    print('2: Mine new block')
    print('3: Output blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        # tuple unpacking example
        recipient, amount = tx_data

        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()   
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid input. Please select from list')
    # if not verify_chain():
    #     print("invalid blockchain!")
    #     break
else:
    print('User left!')


print('done!')
