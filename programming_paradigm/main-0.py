import sys
from bank_account import BankAccount
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py bank:<command>:<amount>   # For bank operations (deposit, withdraw, display)")
        print("  python main.py divide:<numerator>:<denominator>   # For safe division")
        sys.exit(1)

    # Split the operation type and parameters
    args = sys.argv[1].split(':')

    operation_type = args[0]

    if operation_type == "bank":
        account = BankAccount(100)  # starting balance
        if len(args) < 2:
            print("Bank usage: bank:<command>:<amount>")
            print("Commands: deposit, withdraw, display")
            sys.exit(1)

        command = args[1]
        amount = float(args[2]) if len(args) > 2 else None

        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command or missing amount.")

    elif operation_type == "divide":
        if len(args) != 3:
            print("Usage: divide:<numerator>:<denominator>")
            sys.exit(1)

        numerator = args[1]
        denominator = args[2]
        result = safe_divide(numerator, denominator)
        print(result)

    else:
        print("Invalid operation type. Use 'bank' or 'divide'.")

if __name__ == "__main__":
    main()
