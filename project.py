import random

m = 3
ma = 100
mi = 1

row = 3
col = 3

d = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

d1 = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check(c, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = c[0][line]
        for column in c:
            if symbol != column[line]:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def spin(row, col, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(col):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(row):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def mach(columns):
    for r in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[r], end=" | ")
            else:
                print(column[r], end="")
        print()

def dep():
    while True:
        amount = input("Enter money: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Entered amount must be greater than 0.")
        else:
            print("Please enter a number.")

def get():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{m}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= m:
                return lines
            else:
                print("Entered lines are invalid.")
        else:
            print("Please enter a number.")

def bet():
    while True:
        amount = input(f"Enter bet from {mi}/- to {ma}/- on each line: ")
        if amount.isdigit():
            amount = int(amount)
            if mi <= amount <= ma:
                return amount
            else:
                print(f"Amount must be between {mi} - {ma}.")
        else:
            print("Please enter a number.")

def func(bal):
    lines = get()
    while True:
        be = bet()
        total = be * lines
        if total > bal:
            print(f"Bet is greater than balance (${bal})")
        else:
            break

    print(f"You are betting {be} on {lines} lines. Total amount is Rs.{total}")

    slot = spin(row, col, d)
    mach(slot)

    winn, winl = check(slot, lines, be, d1)
    print(f"You won Rs.{winn}.")
    print(f"You won on lines:", *winl)

    return winn - total

def main():
    bal = dep()
    while True:
        print(f"Current balance is Rs.{bal}")
        s = input("Press enter to play (q to quit): ")
        if s.lower() == "q":
            break
        bal += func(bal)

    print(f"You left with Rs.{bal}")

main()
