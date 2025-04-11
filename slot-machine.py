import random

# ['🍒', '⭐', '🔔', '💎', '7', '🍊', '🍇']

def getDeposit():
    while True:
        amount =input('How much would you like to deposit? $')
        if amount.digit():
            amount=int(amount)
            if amount >0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')
    return amount

def getBet(balance):
    while True:
        amount =input('How much woulf you like to bet? $')
        if amount.digit():
            amount=int(amount)
            if 0 < amount <= balance:
                break
            else:
                print(f'Amount must be between $0 - ${balance}.')
        else:
            print('Please enter a number.')
        return amount
    
                





def main():
    print('Welcome to the Slot Machine Game!')
    print('2 of a kind pays 2x, 3 of a kind pays 5x')
    print('-------------------------------------')
    balance = getDeposit()