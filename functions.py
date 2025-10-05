from employees import employees
def add_employee(employees):
    if len(employees)>=8:
        print("cannot add more employees")
        return
    new_id=int(input("enter employee id:"))
    for emp in employees:
        if emp["id"]==new_id:
            print("employee with this id alreay exists")
            return
        name=input("enter employee name:")
        department=input("emter employee department:")
        role=input("enter employee role:")
        salary=int(input("enter employee salary:"))
        employees.append({"id":new_id,"name":name,"department":department,"role":role,"salary":salary})
        print("employee added successfully")
        return

def view_employees(employees):
    if not employees:
        print("no employees to display")
        return
    for emp in employees:
        print(f"ID:{emp["id"]},Name:{emp["name"]},Department{emp["department"]},Role:{emp["role"]},Salary:{emp["salary"]}")

def search_employee(employees):
    if not employees:
        print("no employees to found")
        return
    search_id=int(input("enter employee id to sesrch:"))
    for emp in employees:
        if emp["id"]==search_id:
            for emp in employees:
                print(f"ID:{emp["id"]},Name:{emp["name"]},Department{emp["department"]},Role:{emp["role"]},Salary:{emp["salary"]}")
                return
    print("employee not found")

def update_employee(employees):
    if not employees:
        print("no employees to update")
        return
    update_id=int(input("enter employee id to update"))
    for emp in employees:
        if emp["id"]==update_id:
            print("Employee found",emp)
            field = input("What do you want to update? (department/role/salary): ")
            if field=="department":
                new_department=input("enter new department")
                emp["department"]=new_department
            elif field=="role":
                new_role=input("enter new role")
                emp["role"]=new_role
            elif field=="salary":
                new_salary=int(input("enter new salary"))
                emp["salary"]=new_salary
            else:
                print("Invalid field")
                return
            print("employee updated successfully")
            return
        print("employee not found")

def delete_employee(employees):
    if not employees:
        print("no employees found to delete")
        return
    delete_id=int(input("enter employee id to delete"))
    for emp in employees:
        if emp["id"]==delete_id:
            employees.remove(emp)
            print("employee deleted successfully")
            return
    print("employee not found")





            




