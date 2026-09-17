# class Student:
#     def __init__(self):
#         print("Welcome to No Args Constructor")
 
#     def __init__(self, firstname):
#         print("first Name :",firstname)
 
#     def __init__(self, firstname,coursename,age):
#         print("First Name :",firstname)
#         print("Course Name :",coursename)
#         print("Age :",age)
 
# obj1=Student()
# obj2=Student("Santosh")
# obj3=Student("Santosh","Research and Science",22)

# class Employee:
#     def __init__(self, empno=None, ename=None, jobname=None, sal=None):
#         self.empno=empno
#         self.ename=ename
#         self.jobname=jobname
#         self.sal=sal
#         print("Employee Number :",self.empno)
#         print("Employee Name :",self.ename)
#         print("Employee Job Name :",self.jobname)
#         print("Employee Salary :",self.sal)
#         print("---------------")
 
# obj1=Employee()
# obj2=Employee(101)
# obj3=Employee(102,"Santosh")
# obj4=Employee(103,"Vinith","Analyst")
# obj5=Employee(104,"Srinivasa","Clerk",25000)

# class Employee:
#     def __init__(self, empno=None, ename=None, jobname=None, sal=None):
#         self.empno=empno
#         self.ename=ename
#         self.jobname=jobname
#         self.sal=sal
#         if(empno==None and ename==None and jobname==None and sal==None):
#             print("It is a No Args Constructor!!")
#             print("-----------------")
#         elif(ename==None and jobname==None and sal==None):
#             print("Employee Number :",self.empno)
#             print("-----------------")
#         elif(jobname==None and sal==None):
#             print("Employee Number :",self.empno)
#             print("Employee Name :",self.ename)
#             print("-----------------")
#         elif(sal==None):
#             print("Employee Number :",self.empno)
#             print("Employee Name :",self.ename)
#             print("Employee Job Name :",self.jobname)
#             print("-----------------")
#         else:
#             print("Employee Number :",self.empno)
#             print("Employee Name :",self.ename)
#             print("Employee Job Name :",self.jobname)
#             print("Employee Salary :",self.sal)
#             print("-----------------")
 
# obj1=Employee()
# obj2=Employee(1001)
# obj3=Employee(1001, "Santosh")
# obj4=Employee(1002,"Sahana","Clerk")
# obj5=Employee(1003,"Srinivasa","Analyst",45000)

# class Employee:
#     def __init__(self, *args):
#         if(len(args)==0):
#             print("It is No Args Constructor!!!")
#             print("----------")
#         elif(len(args)==1):
#             print("Employee Id :",args[0])
#             print("----------")
#         elif(len(args)==2):
#             print("Employee Id :",args[0])
#             print("Employee Name :",args[1])
#             print("----------")
#         elif(len(args)==3):
#             print("Employee Id :",args[0])
#             print("Employee Name :",args[1])
#             print("Employee Job Name :",args[2])
#             print("----------")
#         else:
#             print("Employee Id :",args[0])
#             print("Employee Name :",args[1])
#             print("Employee Job Name :",args[2])
#             print("Employee Salary:",args[3])
#             print("----------")
 
# obj1=Employee()
# obj2=Employee(1901)
# obj3=Employee(1902,"Santosh")
# obj4=Employee(1903,"Srinivasa","Analyst")
# obj5=Employee(1904,"Vinith","Clerk",43000)
 
# class Employee:
#     def __init__(self, **kwargs):
#         if(kwargs.get("empno")==None and kwargs.get("ename")==None and kwargs.get("job")==None and kwargs.get("sal")==None):
#             print("It is a No Args Constructor!!!")
#             print("----------------")
#         elif(kwargs.get("ename")==None and kwargs.get("job")==None and kwargs.get("sal")==None):
#             print("Employee Number :",kwargs.get("empno"))
#             print("----------------")
#         elif(kwargs.get("job")==None and kwargs.get("sal")==None):
#             print("Employee Number :",kwargs.get("empno"))
#             print("Employee Name :",kwargs.get("ename"))
#             print("----------------")
#         elif(kwargs.get("sal")==None):
#             print("Employee Number :",kwargs.get("empno"))
#             print("Employee Name :",kwargs.get("ename"))
#             print("Employee Job :",kwargs.get("job"))
#             print("----------------")
#         else:
#             print("Employee Number :",kwargs.get("empno"))
#             print("Employee Name :",kwargs.get("ename"))
#             print("Employee Job :",kwargs.get("job"))
#             print("Employee Salary :",kwargs.get("sal"))
#             print("----------------")
 
# obj1=Employee()
# obj2=Employee(empno=1901)
# obj3=Employee(empno=1902,ename="Santosh")
# obj4=Employee(empno=1903,ename="Srinivasa",job="Analyst")
# obj5=Employee(empno=1904,ename="Vinith",job="Clerk",sal=43000)

# Methods in Python Class:

# ---------------------------------------

# We can specify the following Methods in Python Class
 
# 1. Instance Methods

# 2. Class Methods

# 3. Static Methods
 
# 1. Instance Methods: 

# This Type of Methods never accept any decorator, It accept first parameter as self.

# Example:
 
class DistictLibrary:

    def show_book_name(self, bookname):

        print("Book Name :",bookname)
 
    def show_author_name(self, authorname):

        print("Author Name :",authorname)
 
obj=DistictLibrary()

obj.show_book_name("Java Complete Reference")

obj.show_author_name("Richard")
 
 
# 2. Class Methods:

# This type of methods should have decorator @classmethod and it accepts first parameter as cls.

# Example:

class Task:

    taskname="Test Plan Creation"
 
    @classmethod

    def display_task_name(cls):

        print("Task Name :",Task.taskname)
 
    @classmethod

    def display_task_description(cls, description):

        print("Task Description :",description)
 
 
Task.display_task_name()

Task.display_task_description("Test Plan drives all Testing Activities")
 
# 3. Static Methods:

# This type of methods should have decorator @staticmethod and It does not have any specific first parameter.
 
class Maths:

    @staticmethod

    def addition(x,y):

        result=(x + y)

        print("Addition Result :",result)
 
    @staticmethod

    def multiplication(x,y):

        result=(x * y)

        print("Multiplication Result :",result)

 
obj=Maths()

obj.addition(20,50)

obj.multiplication(12,10)

print("-----------")

Maths.addition(40,50)

Maths.multiplication(13,9)
 
 
 