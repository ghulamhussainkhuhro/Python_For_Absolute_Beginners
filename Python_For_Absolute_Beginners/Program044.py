# you are given a list of subjects for students.
# Assume 1 class room is required  for 1 subject.
# How many classrooms are needed by all students 

# Data : "python", "java", "c++", "javascript", "c", "python", "java", "python", "c++", "java", "c", "javascript"

# In this case we have to focus only on unique subjects not matter how many times they are repeated so
# making a set in this case is preferrable b/c it will ignore repitations

collection = {
    "python", "java", "c++", "javascript", "c", 
    "python", "java", "python", "c++", "java", 
    "c", "javascript"
    }

print(collection)
print("Number of classrooms required :",len(collection))
