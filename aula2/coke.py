def main():
    amount_due = 50
    print("Amount Due:", amount_due)

    while amount_due > 0:
        try:
            money = int(input("Insert Coin: "))
            if is_valid(money):
                amount_due -= money
                if amount_due > 0:
                    print("Amount Due:", amount_due)
                else:
                    print("Change Owed:", abs(amount_due))  # Exibe o troco
            else:
                print("Amount Due:", amount_due)  # Não altera o valor devido
        except ValueError:
            print("Please enter a valid integer.")

def is_valid(coin):
    """Verifica se a moeda inserida é válida."""
    return coin in [5, 10, 25]

main()
