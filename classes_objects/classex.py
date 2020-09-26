class Employee:
	employee_count=0;
	def __init__(self,name,salary):
		self.name=name;
		self.salary=salary;
		Employee.employee_count+=1;
		
	def displaycount(self):
		print("Total Employee count: "+str(Employee.employee_count));
		
	def displayEmpData(self):
		print("Employee name: "+self.name+" Employee Salary: "+str(self.salary));
		
emp1 = Employee("shailesh",1000.0);
emp2 = Employee("vishal",2000.0);

emp2.displaycount();
emp1.displayEmpData();
emp2.displayEmpData();

if hasattr(emp1,"salary"):
    print("Employee has Salary attribute");
    setattr(emp1,"salary",2500.0);
    emp1.displayEmpData();
else:
    print("Employee does not have Salary attribute");