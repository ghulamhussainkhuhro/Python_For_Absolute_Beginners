
# NOTE: Strings are immutable in python (cannot be changed)
#       Lists are mutable in python (It can be changed)

# str = "Hello"
# print(str[0])
# str[0] = "Y" # TypeError: 'str' object does not support item assignment

# But in case of liats we can change the data entries Within range of list we cannot not aceess or update 
student_info = ["Ghulam Hussain", 19, "23SW050", +923000000000, 69350]
print("Before changes :", student_info)
student_info[0] = "Abbas ALi"
student_info[2] = "23SW056"
print("After changes :", student_info)
print(len(student_info))
# len of list is 5 so last index is 4
# print(student_info[5]) # IndexError: list index out of range








