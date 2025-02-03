class Employee:
    company_name = 'code'

    def __init__(self,name,age,design):
        self.name = name
        self.age = age
        self.design = design

    def login(self,time):
        print(f"{self.name} logged in at {time}")

    def logout(self,time):
        print(f"{self.name} loggedout in at {time}")

    def work(self,hours):
        print(f"{self.name} worked for {hours} hrs.")

    def getDetails(self):
        print("Employee name: ",self.name)
        print("Employee age: ",self.age)
        print("Employee Designation: ",self.design)

e1 = Employee("Sk",24,"Student")
e2 = Employee("Ak",22,"Intern")
e3 = Employee("Dk",19,"Teacher")

e1.login(3)
e1.logout(4)
e1.work(5)
e1.getDetails()
e2.getDetails()
e3.getDetails()