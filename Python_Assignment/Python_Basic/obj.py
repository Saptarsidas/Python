class Employee:
    count=0
    def __init__(self,nm):
        self.name=nm
        Employee.count+=1
    def displayemp(self):
            print("Employee name is {} and id is {}".format(self.name,self.count))

obj=Employee('Saptarsi')
obj.displayemp()
obj1=Employee('Susmita')
obj1.displayemp()
obj2=Employee('Sagnik')
obj2.displayemp()
obj2=Employee('Trishita')
obj2.displayemp()