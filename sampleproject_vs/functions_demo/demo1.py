# Case 1: Write a function to perform multiplication of two numbers without parameters.
def multiplication():
    x=12
    y=10
    result=(x * y)
    print("Multiplication Result :",result)
 
multiplication()
multiplication()
multiplication()
 
 
# Case 2: Write a function to perform multiplication of two numbers with parameters.
# Solution:
 
def multiplication(a,b):
    result= (a * b)
    print("Multiplication Result :",result)
 
multiplication(12,10)
multiplication(13,5)
multiplication(14,9)
 
# Case 3: Write function to find factorial of a given number
# Solution:
# Case 3: Write function to find factorial of a given number
 
def find_factorial(num):
    fact=1
    for i in range(1, num+1):
        fact=fact * i
    print("Factorial of number ",num," is ",fact)
 
 
find_factorial(4)
find_factorial(5)
find_factorial(6)
 
# Case 4: Write a program for the given tuple of elements add into list and Read Elements from list.
# Solution:
def assign_elements(tupleobject):
    list=[]
    for item in tupleobject:
        list.append(item)
    print(list)
 
# Execute Execution
tup_elements=(40,60,"Mango","Lotus",12.75,True)
assign_elements(tup_elements)
 
 
# Case 5: Write a program to display Prime numbers in between 10 to 100
def display_prime_numebrs(start, end):
 
    for number in range(start, end):
        flag=0
        for i in range(2, number):
            if(number % i ==0):
                flag=1
                break
 
        if(flag==0):
            print(number, end="  ")
 
display_prime_numebrs(10,100)

# 2. Functions which return value:
# ------------------------------------------------
# If a body of function contains return keyword it represents that function can return a value.
 
# Example: 
# Without Return value
def show_studnet_name(sname):
    print("The Student name is ",sname)
 
 
show_studnet_name("Santosh")
 
print("-------------------")
# with return value
 
def get_student_name(sname):
    return sname
 
 
v1=get_student_name("Srinivasa")
print(v1)
print("Name of the Student ",v1)
print("the Student who belong to our Cricket Team is ",v1)
 
# Example2: Write a function to validate the given number prime
 
# Example2: Write a function to validate the given number prime
def isPrimeNumber(number):
    flag=0
    for i in range(2, number):
        if(number % i ==0):
            flag=flag+1
            break
 
    if(flag==0):
        return True
    else:
        return False
 
# Case 1: Validate the given numebr
v1=isPrimeNumber(11)
print("Prime Number :",v1)
 
# Case 2: find count of prime numbers in between 10 to 50
count=0
for i in range(10,51):
    if(isPrimeNumber(i)==True):
        count=count+1
print("Count of Prime Numbers in betwen 10 to 50 :",count)
 
# Case 3: display Prime numbers in between 50 to 75
for i in range(50, 76):
    if(isPrimeNumber(i)==True):
        print(i, end=" ")
print()
# Case 4: Fidn sum of Prime numebrs i nbetween 25 to 50
sum=0
for i in range(25,51):
    if(isPrimeNumber(i)==True):
        sum=sum+i
print("Sum of Prime Numbers 25 to 50 :",sum)
 
 
# Case 2: Write a function to return a Integer list from a function.
# Case 2: Write a function to return a Integer list from a function.
def get_integer_list():
    new_list=[x for x in range(1,11)]
    return new_list
 
# Case 1 : display the return value
elements = get_integer_list()
print(elements)
# Case 2: find sum of All Elements in a list
sum=0
for i in range(1, len(elements)+1):
    sum=sum+i
print("Sum of All Elements :",sum)
# Case 3: Print first half of teh Elements
half_elements=[x for x in range(1, int(len(elements)/2)+1)]
print(half_elements)
# Case 4: Print Second Half of Eleemnts
second_half_eleemnts=[x for x in range(int(len(elements)/2)+1, len(elements)+1) ]
print(second_half_eleemnts)




