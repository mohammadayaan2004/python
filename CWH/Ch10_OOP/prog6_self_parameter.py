class Employee:
    company="Google"
    def getsalary(self):
        print(f"Salary is {self.salary}")

ayaan=Employee()
ayaan.salary="110K"
ayaan.getsalary()        #Employee.getsalary(ayaan)