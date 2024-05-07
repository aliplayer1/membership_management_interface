import tkinter as tk
import re
from tkinter import messagebox
from service import add_member, record_payment, get_financial_report, create_account, validate_credentials, get_member_info, log_expense, get_member_list, get_member_list_by_attendance, get_member_list_by_payment, get_payment_history
class ClubManagementApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Recreational Club Management App")

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)

        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.login_btn = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.create_account_btn = tk.Button(self.login_frame, text="Create Account", command=self.create_account)
        self.create_account_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5) 


    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        member = validate_credentials(username, password)
        if username == "admin" and password == "password":
            self.show_admin_menu()
        elif member:
            messagebox.showinfo("Login Successful", f"Welcome back, {member.name}!")
            self.show_member_menu(member)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    

    def show_admin_menu(self):
        self.login_frame.destroy()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        self.label = tk.Label(self.main_frame, text="Welcome to the Recreational Club Management System", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.add_member_btn = tk.Button(self.main_frame, text="Add Member", command=self.add_member)
        self.add_member_btn.grid(row=1, column=0, columnspan=2, padx=0, pady=0)

        self.record_payment_btn = tk.Button(self.main_frame, text="Record Payment", command=self.record_payment)
        self.record_payment_btn.grid(row=2, column=0, columnspan=2, padx=0, pady=0)

        self.log_expense_btn = tk.Button(self.main_frame, text="Log Expense", command=self.log_expense)
        self.log_expense_btn.grid(row=3, column=0, columnspan=2, padx=0, pady=0)

        self.view_report_btn = tk.Button(self.main_frame, text="View Financial Report", command=self.view_financial_report)
        self.view_report_btn.grid(row=4, column=0, columnspan=2, padx=0, pady=0)

        self.view_members_btn = tk.Button(self.main_frame, text="View Member List", command=self.view_member_list)
        self.view_members_btn.grid(row=5, column=0, columnspan=2, padx=0, pady=0)

    def add_member(self):
        self.add_member_window = tk.Toplevel(self.root)
        self.add_member_window.title("Add Member")

        self.name_label = tk.Label(self.add_member_window, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.add_member_window)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.add_member_window, text="Email:")
        self.email_label.grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.add_member_window)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_btn = tk.Button(self.add_member_window, text="Submit", command=self.submit_member)
        self.submit_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def submit_member(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return
        try:

            member_id = add_member(name, email)
            messagebox.showinfo("Member Added", f"Member added with ID: {member_id}")
            self.add_member_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not add member: {str(e)}")
    

    def record_payment(self):
        self.record_payment_window = tk.Toplevel(self.root)
        self.record_payment_window.title("Record Payment")

        self.member_id_label = tk.Label(self.record_payment_window, text="Member ID:")
        self.member_id_label.grid(row=0, column=0, padx=5, pady=5)
        self.member_id_entry = tk.Entry(self.record_payment_window)
        self.member_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = tk.Label(self.record_payment_window, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(self.record_payment_window)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_btn = tk.Button(self.record_payment_window, text="Submit", command=self.submit_payment)
        self.submit_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def submit_payment(self):
        member_id = int(self.member_id_entry.get())
        amount = float(self.amount_entry.get())
        record_payment(member_id, amount)
        messagebox.showinfo("Payment Recorded", "Payment recorded successfully.")
        self.record_payment_window.destroy()

    def view_financial_report(self):
        self.report_window = tk.Toplevel(self.root)
        self.report_window.title("Financial Report")

        self.month_label = tk.Label(self.report_window, text="Month (1-12):")
        self.month_label.grid(row=0, column=0, padx=5, pady=5)
        self.month_entry = tk.Entry(self.report_window)
        self.month_entry.grid(row=0, column=1, padx=5, pady=5)

        self.year_label = tk.Label(self.report_window, text="Year:")
        self.year_label.grid(row=1, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(self.report_window)
        self.year_entry.grid(row=1, column=1, padx=5, pady=5)

        self.view_btn = tk.Button(self.report_window, text="View Report", command=self.display_report)
        self.view_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.report_text = tk.Text(self.report_window, width=50, height=10)
        self.report_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def display_report(self):
        month = int(self.month_entry.get())
        year = int(self.year_entry.get())
        report = get_financial_report(month, year)
        report_text = f"Total Income: {report['total_income']}\n"
        report_text += f"Total Expenses: {report['total_expenses']}\n"
        report_text += f"Net Profit: {report['net_profit']}\n"
        self.report_text.delete("1.0", tk.END)
        self.report_text.insert(tk.END, report_text)

    def log_expense(self):
        self.log_expense_window = tk.Toplevel(self.root)
        self.log_expense_window.title("Log Expense")

        self.description_label = tk.Label(self.log_expense_window, text="Expense Description:")
        self.description_label.grid(row=0, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.log_expense_window)
        self.description_entry.grid(row=0, column=1, padx=5, pady=5)

        self.expense_amount_label = tk.Label(self.log_expense_window, text="Expense Amount:")
        self.expense_amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.expense_amount_entry = tk.Entry(self.log_expense_window)
        self.expense_amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_btn = tk.Button(self.log_expense_window, text="Submit", command=self.submit_expense)
        self.submit_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def submit_expense(self):
        description = str(self.description_entry.get())
        amount = float(self.expense_amount_entry.get())
        log_expense(description, amount)
        messagebox.showinfo("Expense Recorded", "Expense recorded successfully")
        self.log_expense_window.destroy()
    
    def view_member_list(self):
        member_list = get_member_list()

        self.member_list_window = tk.Toplevel(self.root)
        self.member_list_window.title("Member List")

        member_list_display = tk.Text(self.member_list_window, height=20, width=50)
        member_list_display.pack(padx=10, pady=10)

        for member in member_list:
            member_list_display.insert(tk.END, f"ID: {member.id}, Name: {member.name}, Email: {member.email} \n")
        
        member_list_display.config(state=tk.DISABLED)

        self.sort_attendance_btn = tk.Button(self.member_list_window, text="Sort by Attendance", command=self.sort_attendance)
        self.sort_attendance_btn.pack(padx=10, pady=5)

        self.sort_payment_btn = tk.Button(self.member_list_window, text="Sort by Payments", command=self.sort_payment)
        self.sort_payment_btn.pack(padx=10, pady=5)
    
    def sort_attendance(self):
        member_list = get_member_list_by_attendance()

        self.sort_attendance_window = tk.Toplevel(self.root)
        self.sort_attendance_window.title("Members Sorted by Attendance")

        member_list_display = tk.Text(self.sort_attendance_window, height=20, width=70)
        member_list_display.pack(padx=10, pady=10)

        for member in member_list:
            member_list_display.insert(tk.END, f"ID: {member.id}, Name: {member.name}, Email: {member.email}, Attendance: {member.attendance} \n")
        
        member_list_display.config(state=tk.DISABLED) 
    
    def sort_payment(self):
        member_list = get_member_list_by_payment()

        self.sort_payment_window = tk.Toplevel(self.root)
        self.sort_payment_window.title("Members Sorted by Payment")

        member_list_display = tk.Text(self.sort_payment_window, height=20, width=70)
        member_list_display.pack(padx=10, pady=10)

        for member in member_list:
            member_list_display.insert(tk.END, f"ID: {member.id}, Name: {member.name}, Email: {member.email}, Unpaid Classes: {member.unpaid_classes} \n")
        
        member_list_display.config(state=tk.DISABLED)

    def create_account(self):
        self.create_account_window = tk.Toplevel(self.root)
        self.create_account_window.title("Create Account")

        self.name_label = tk.Label(self.create_account_window, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.create_account_window)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.create_account_window, text="Email:")
        self.email_label.grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.create_account_window)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.username_label = tk.Label(self.create_account_window, text="Username:")
        self.username_label.grid(row=2, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(self.create_account_window)
        self.username_entry.grid(row=2, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.create_account_window, text="Password:")
        self.password_label.grid(row=3, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(self.create_account_window, show="*")
        self.password_entry.grid(row=3, column=1, padx=5, pady=5)

        self.submit_btn = tk.Button(self.create_account_window, text="Submit", command=self.submit_account)
        self.submit_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def submit_account(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return
        try: 
            new_member_id, new_member = create_account(name, email, username, password)
            messagebox.showinfo("Account Created", f"Account created successfully with ID: {new_member_id}")
            self.show_member_menu(new_member)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_member_menu(self, member):
        self.login_frame.destroy()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        self.label = tk.Label(self.main_frame, text="Welcome to the Recreational Club Management App", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        name, email = get_member_info(member.id)
        self.label.config(text=f"Welcome, {name}! \n Email: {email}")

        self.pay_class_btn =  tk.Button(self.main_frame, text="Pay for Class", command=lambda: self.pay_class(member))
        self.pay_class_btn.grid(row=1, column=0, padx=5, pady=5)

        self.show_payments_btn = tk.Button(self.main_frame, text="Payment History", command=lambda: self.payment_history(member))
        self.show_payments_btn.grid(row=1, column=1, padx=5, pady=5)

    def pay_class(self, member):
        self.pay_class_window = tk.Toplevel(self.root)
        self.pay_class_window.title("Pay for Class")

        self.name_label = tk.Label(self.pay_class_window, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.pay_class_window)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.amount_label = tk.Label(self.pay_class_window, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(self.pay_class_window)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_btn = tk.Button(self.pay_class_window, text="Submit", command=lambda: self.submit_member_payment(member))
        self.submit_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def submit_member_payment(self, member):
        member_id = member.id
        amount = float(self.amount_entry.get())
        record_payment(member_id, amount)
        messagebox.showinfo("Payment Accepted", "Payment accepted successfully.")
        self.pay_class_window.destroy()

    def payment_history(self, member):
        payment_history = get_payment_history(member.id)
        history_window = tk.Toplevel(self.root)
        history_window.title("Payment History")
        row = 0
        for payment in payment_history:
            tk.Label(history_window, text=f"Payment ID: {payment['payment_id']}, Amount: ${payment['amount']}, Date: {payment['date']}").grid(row=row, column=0, padx=10, pady=3)
            row += 1





if __name__ == "__main__":
    root = tk.Tk()
    app = ClubManagementApp(root)
    root.mainloop()