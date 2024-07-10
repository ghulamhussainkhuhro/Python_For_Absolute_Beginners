# Write a function to calculate the sum of list

# Method 1:
def calc_sum(list):
    sum = 0
    # Approach 1 to iterate
    for i in range(0,len(list)):
        sum += list[i]
    return sum
    
    # Approach 2 to iterate
    for i in list:
        sum += i
    return sum

i = 0
def calc_sum_2(numbers):
    # base case when the list is empty
    if(not numbers):
        return 0
    else:
        return numbers[0] + calc_sum_2(numbers[1:]) # will call the same fuction with a list excluding 1st element
    

print(calc_sum([1,2,3,4,5]))
print(calc_sum([2]))
print(calc_sum_2([1,2,3,4,5]))
print(calc_sum_2([2]))