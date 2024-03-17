# employee millions meant create a class representing an employee with attributes like employee ID name and salary implement methods to calculate the yearly bonus and display employee details
class Employee:
    def __init__(self,emp_id,emp_name,deperment,salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.deperment=deperment
        self.salary=salary
        
   
    def calculate_bonus(self):
        n=(int(input("Enter bonus percentage :")))
        year_salary=self.salary*12
        print("Yearly Salary",year_salary)
        calculate_bonus=(year_salary*n/100)+year_salary
        print("Yearly Bonus is ",calculate_bonus)
    def display(self):
       print("Id:",self.emp_id)
       print("Name:",self.emp_name)
       print("Deparment :",self.deperment)
       print("Salary:",self.salary)
 
emp=Employee(101,"Saptarsi Das","Bca",5000)
emp.display()
emp.calculate_bonus()



    

        