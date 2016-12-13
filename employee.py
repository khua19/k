class Employee:
   empCount = 0
   mancount = 0
   clerkcount 0

    def __init__(self, name, salary, title):
        self.name = name
        self.salary = salary
        self.title = title
        Employee.empCount += 1

        if self.title=="manager":
            Employee.mancount += 1
        if self.title=="clerk":
            Employee.clerkcount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary,", Title:",self.title

emp1 = Employee("Zara", 2000, "manager")
emp2 = Employee("Manni", 5000, "clerk")
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
print "Total manager %d" % Employee.mancount
print "Total clerk %d" % Employee.clerkcount
