# Capitalize - Converts teh Frist Character to uppercase
str1="java program"
print(str1.capitalize())  # Java program
 
print("--------------------------")
# title -> Converts first character of each word into uppercase
str2="python programming language"
print(str2.title())  #  Python Programming Language
 
print("--------------------------")
# lower - it converts given string into lowercase
str3="WELCOME"
print(str3.lower())  # welcome
 
print("--------------------------")
# upper - > it converts given string into uppercase
str4="welcome"
print(str4.upper())  # WELCOME
 
print("--------------------------")


# Starts with - It verifies beginning of teh string
str1="It is a new palace"
print(str1.startswith("It"))   # True
print(str1.endswith("palace"))  # True
print("-----------------------------------------")
# find -> Find the position of the string or character from Left to Right
str2="It is a book, It is on teh table, it is a new book"
print(str2.find("is"))  # 3
print(str2.find("is",4))  # 17
 
print("-----------------------------------------")
# rfind -> Find the position of the string or character from Right to Left
str3="It is a book, It is on the table, it is a new book"
print(str3.rfind("is"))
print("-----------------------------------------")
# index  -> Find the position of the string or character from Left to Right
str4="It is a book, It is on teh table, it is a new book"
print(str4.index("is"))  # 3
print(str4.index("is",4))  # 17
print("-----------------------------------------")
# rindex -> Find the position of the string or character from Right to Left
str5="It is a book, It is on the table, it is a new book"
print(str5.rindex("is"))
 
# split -> This function splits teh string based on delimiter
str1="Mango,apple,Banana,Orange"
print(str1.split(","))
print("-------------------------")
# splitlines -> This function splits the string based on delimiter
str2='''It is a book
It is on the table
It has many topics on history
'''
print(str2.splitlines())
print("-------------------------")
#lstrip -> It removes blank space on left side
str3="   WELCOME   "
print("Before lstrip , The number of Characters :",len(str3))
print("After lstrip , The number of Characters :",len(str3.lstrip()))
print("-------------------------")
#rstrip -> It removes blank space on right side
str3="   WELCOME   "
print("Before rstrip , The number of Characters :",len(str3))
print("After rstrip , The number of Characters :",len(str3.rstrip()))
print("-------------------------")
#strip -> It removes blank space both sides
str4="   WELCOME   "
print("Before strip , The number of Characters :",len(str4))
print("After strip , The number of Characters :",len(str4.strip()))
 