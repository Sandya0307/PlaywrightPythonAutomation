str="PQR"
print(str[0])
print(str[1])
print(str[2])

# Slicing Example:
str="SGSOFTWARETESTING"
print(str)     # SGSOFTWARETESTING
print(str[1])  # G
print(str[2:10])   # SOFTWARE
print(str[10:14])   # TEST
print(str[-11:-7])   # WARE
print(str[-15:-11])  # SOFT
print(str[10:])      #TESTING
print(str[:6])       # SGSOFT
print(str[-11:])     # WARETESTING
print(str[:-7])      # SGSOFTWARE
print(str[::-1])     # GNITSETERAWTFOSGS

# How to Format the Strings in Python:

 
# Default Fromating of String
str1="{} {} {}".format("Python","Programming","Language")
print(str1)
 
# Based on Position of Formatting the String
str2="{1} {0} {2}".format("Python","Programming","Language")
print(str2)
 
# Based on keyword of Formatting the String
str3="{r} {q} {p}".format(p="Python",q="Programming",r="Language")
print(str3)




# triple Quotes are preserving Newlines in a given String but single quote and Double do not preserving Newlines:

# triple quote
str1='''
We are learning Playwright
We are using playwright based on Python
Python provides OOPS concepts
'''
print(str1)
 
# Single quote
str2='We are playing' \
' a foot ball in our school ground' \
' It is a international Game'
print(str2)
 
# Double quote
str3="We are playing" \
" Cricket in College Gound" \
" It is a international Game" 
print(str3)
 
# triple quote in teh form 3 double quotes
str4="""
We are learning Playwright
We are using playwright based on Python
Python provides OOPS concepts
"""
print(str4)

# How to Delete the String in Python:

# Delete String
str1="Welcome"
print(str1)
 
del str1
print(str1)