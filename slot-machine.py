import random

symbols = ["🍒", "⭐", "💎", "🍊", "🍇"]


def getDeposit():
    try:
        amount = int(input("How much would you like to deposit? $"))
        if amount <= 0:
            print("Amount must be greater than 0.")
            getDeposit()
        return amount
    except ValueError:
        print("Please enter a number.")
        getDeposit()


def getBet(balance):
    if balance <= 0:
        print("You have no balance left by losing all.")
        exit(0)
    while True:
        amount = input("How much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if 0 < amount <= balance:
                break
            else:
                print(f"Amount must be between $1 - ${balance}.")
                continue
        else:
            print("Please enter a number.")
            continue
    return amount


def spin():
    return [random.choice(symbols) for i in range(3)]


def calculateWinnings(columns, bet):
    if columns[0] == columns[1] == columns[2]:
        return bet * 5
    elif len(set(columns)) == 2:
        return bet * 2
    else:
        return 0


def currentStatus(balance, winnings):
    if winnings > 0:
        print(f"\nYou won ${winnings}!")
    else:
        print("\nYou lost!")
    print(f"Your current balance is ${balance}.")
    if balance <= 0:
        print("You have no balance left.")
        startGame()


def slotMAchine(balance):
    while True:
        betAmount = getBet(balance)
        balance -= betAmount
        result = spin()
        print("\nSpinning...\n")
        print(f"| {result[0]} | {result[1]} | {result[2]} |")

        winnings = calculateWinnings(result, betAmount)
        balance += winnings
        currentStatus(balance, winnings)

        decide = input("\nTo play more, press enter or type q to quit : ")
        if decide.lower() == "q":
            print(f"\n💵 Cashing out with ${balance}!")
            print("Thanks for playing!")
            exit(0)
        else:
            print("\nLet's play again!")
            continue


def startGame():
    balance = getDeposit()
    slotMAchine(balance)


def main():
    print("Welcome to the Slot Machine Game!")
    print(symbols)
    print("2 of a kind pays 2x, 3 of a kind pays 5x")
    print("-------------------------------------")
    startGame()


if __name__ == "__main__":
    main()