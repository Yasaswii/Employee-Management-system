from employees import employees
from functions import add_employee,view_employees,search_employee,update_employee,delete_employee
def menu():
    while True:
     print("Employee Management System")
     print("1.Add Employee")
     print("2.View Employees")
     print("3.search Employee")
     print("4.Update Employee")
     print("5.Delete Employee")
     print("6.Exit")
     choice=input("enter your choice:")
     if choice=="1":
        add_employee(employees)
     elif choice=="2":
        view_employees(employees)
     elif choice=="3":
        search_employee(employees)
     elif choice=="4":
        update_employee(employees)
     elif choice=="5":
        delete_employee(employees)
     elif choice=="6":
        print("exit")
        break
     else:
        print("invalid choice")
menu()



        



