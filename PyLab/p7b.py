class employee:

    def __init__(self):
        self.name = " "
        self.id = " "
        self.dep = " "
        self.salary = 0

    def getdetail(self):
        self.name = input("enter the name:")
        self.id = input(" the employee id:")
        self.dep = input("Department     :")
        self.salary = input("enter   salary:")

    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.dep)
        print("Salary", self.salary)

    def newsalary(self):
        self.salary = int(input("enter the new salary"))
        print("updated salary:", self.salary)


emp = []
n = int(input("enter the no of employee"))
for _ in range(n):
    e1 = employee()
    e1.getdetail()
    e1.display()
    e1.newsalary()
    emp.append(e1)






