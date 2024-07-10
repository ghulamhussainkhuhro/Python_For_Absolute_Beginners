# pass statement 
# Pass is a null statement that does nothing, It is used as a placeholder for future code

# Why pass statement...?
# If you will write 

# for i in range(1,11):
#     #empty 
# print("Code after for loop") IndentationError: expected an indented block after 'for' statement on line 7

# This will cause an IndentationError:

# To make an empty for loop we use pass statement

for i in range(1,11):
    pass 
print("Code after for loop") 
