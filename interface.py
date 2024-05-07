# interface.py
import service

def main_menu():
    print("Welcome to the Recreational Club Management System")
    print("1. Add a new member")
    print("2. Record a payment")
    print("3. View financial report")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_member():
    name = input("Enter member's name: ")
    email = input("Enter member's email: ")
    member_id = service.add_member(name, email)
    print(f"Member added with ID: {member_id}")

def record_payment():
    member_id = int(input("Enter member ID: "))
    amount = float(input("Enter payment amount: "))
    service.record_payment(member_id, amount)
    print("Payment recorded successfully.")

def view_financial_report():
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year (e.g., 2023): "))
    report = service.get_financial_report(month, year)
    print("Financial Report:")
    print(f"Total Income: {report['total_income']}")
    print(f"Total Expenses: {report['total_expenses']}")
    print(f"Net Profit: {report['net_profit']}")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            add_member()
        elif choice == '2':
            record_payment()
        elif choice == '3':
            view_financial_report()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
