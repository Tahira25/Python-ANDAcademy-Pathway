class Employee():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = " ".join([firstname, lastname])
        self.email = f"{self.fullname.lower().replace(' ','.')}@and.digital"
        

    def salary(self, annual_salary):
        self.annual_salary = annual_salary
        self.monthly_salary = annual_salary/12

test_one = Employee("Syeda-Tahira", "Tanzim")
print(test_one.email)
print(test_one.fullname)

test_one.salary(30000)
print(test_one.annual_salary)
print(test_one.monthly_salary)
