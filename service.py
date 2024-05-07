# service.py
from datetime import date
from models import Session, Member, Payment, Expense
from sqlalchemy import extract

# Financial Management Operations
def record_payment(member_id, amount):
    session = Session()
    payment = Payment(member_id=member_id, amount=amount, date=date.today())
    session.add(payment)
    session.commit()

def log_expense(description, amount):
    session = Session()
    expense = Expense(description=description, amount=amount, date=date.today())
    session.add(expense)
    session.commit()

def get_financial_report(month, year):
    session = Session()
    payments = session.query(Payment).filter(
        extract('month', Payment.date) == month,
        extract('year', Payment.date) == year
    ).all()
    expenses = session.query(Expense).filter(
        extract('month', Expense.date) == month,
        extract('year', Expense.date) == year
    ).all()

    return {
        "total_income": sum(payment.amount for payment in payments),
        "total_expenses": sum(expense.amount for expense in expenses),
        "net_profit": sum(payment.amount for payment in payments) - sum(expense.amount for expense in expenses)
    }
# Member Management Operations
def add_member(name, email):
    session = Session()
    member = Member(name=name, email=email)
    session.add(member)
    session.commit()
    return member.id

def get_member_payment_status(member_id):
    session = Session()
    member = session.query(Member).get(member_id)
    payments = session.query(Payment).filter_by(member_id=member_id).all()
    total_paid = sum(payment.amount for payment in payments)
    return {
        "member_id": member.id,
        "name": member.name,
        "total_paid": total_paid
    }

def update_member_attendance(member_id, attended):
    session = Session()
    member = session.query(Member).get(member_id)
    if attended:
        member.unpaid_classes -= 1  # Assuming one class is cleared per attendance
    else:
        member.unpaid_classes += 1
    session.commit()

def get_payment_history(member_id):
    session = Session()
    payments = session.query(Payment).filter_by(member_id=member_id).all()
    session.close()
    return [{
        "payment_id": payment.id,
        "amount": payment.amount,
        "date": payment.date
    } for payment in payments]

def get_member_list():
    session = Session()
    members = session.query(Member).all()
    session.close()
    return members

def get_member_list_by_attendance():
    session = Session()
    members = session.query(Member).order_by((Member.attendance)).all()
    session.close()
    return members

def get_member_list_by_payment():
    session = Session()
    members = session.query(Member).order_by(Member.unpaid_classes).all()
    session.close()
    return members
# User Interaction Operations
def send_reminder(member_id, message):
    # Placeholder for sending a reminder, e.g., email or SMS
    member = get_member_payment_status(member_id)
    print(f"Sending reminder to {member['name']} ({member['email']}): {message}")

def schedule_practice(member_id, practice_date):
    # This function would integrate with a calendar or scheduling system
    print(f"Scheduling practice for {member_id} on {practice_date}")


def create_account(name, email, username, password):
    session = Session()
    member = Member(name=name, email=email, username=username, password=password)
    session.add(member)
    session.commit()
    session.refresh(member)
    return member.id, member

def validate_credentials(username, password):
    session = Session()
    member = session.query(Member).filter_by(username=username, password=password).first()
    return member

def get_member_info(member_id):
    session = Session()
    member = session.query(Member).get(member_id)
    return member.name, member.email

# You can extend these functions to fully cover the requirements in the PDF.
