class employee():
    total=0
    def __init__(self,name,id,dept,salary):
        self.name=name
        self.id=id
        self.dept=dept
        self.salary=salary

    def update(self,percent):
        self.salary+=self.salary*percent/100

    def details(self):
        print("name:"+self.name)
        print("id:" ,self.id)
        print("dept:" + self.dept)
        print("salary:",  self.salary)

emp=[]
n=int(input("enter no. of employees"))
for i in range(n):
    print(f"employee-{i+1}")
    name=input("enter name")
    id=int(input("enter id"))
    dept=input("enter dept:")
    salary=int(input("enter salary:"))
    emp.append(employee(name,id,dept,salary))

for i in range(n):
    emp[i].details()

hike=int(input("enter hike in %"))
for i in range(n):
    emp[i].update(hike)


for i in range(n):
    emp[i].details()