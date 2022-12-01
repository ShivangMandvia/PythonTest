class Person(object):

	# Constructor
	# def __init__(self, name):
	# 	self.name = name

	# To get name
	def getName(self):
		Name = input("Enter a name -")
		return Name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
emp = Person()
print(emp.getName(), emp.isEmployee())   # type: ignore

emp = Employee()
print(emp.getName(), emp.isEmployee())  # type: ignore
