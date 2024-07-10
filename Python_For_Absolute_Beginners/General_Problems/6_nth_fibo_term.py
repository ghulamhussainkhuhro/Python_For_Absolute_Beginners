def nth_fibo(position):
    # 1st term
    if(position == 1):
        return 0
    # 2nd term
    elif(position == 2):
        return 1
    else:
        return (nth_fibo(position-1) + nth_fibo(position-2))
    
print("5th term of fibonacci series is :",nth_fibo(5))

# Let's perform a dry run for the `nth_fibo` function when calculating the 5th term of the Fibonacci series.

### Call Tree for `nth_fibo(5)`

# 1. `nth_fibo(5)`
#    - Since the position is neither 1 nor 2, it calls `nth_fibo(4)` and `nth_fibo(3)`.

# 2. `nth_fibo(4)`
#    - Calls `nth_fibo(3)` and `nth_fibo(2)`.

# 3. `nth_fibo(3)`
#    - Calls `nth_fibo(2)` and `nth_fibo(1)`.

# 4. `nth_fibo(2)`
#    - Position is 2, so it returns 1.

# 5. `nth_fibo(1)`
#    - Position is 1, so it returns 0.

# Now, combining the results for `nth_fibo(3)`:
# - `nth_fibo(3)` = `nth_fibo(2)` + `nth_fibo(1)` = 1 + 0 = 1.

# And for `nth_fibo(4)`:
# - `nth_fibo(4)` = `nth_fibo(3)` + `nth_fibo(2)` = 1 + 1 = 2.

# Now, combining the results for `nth_fibo(5)`:
# - `nth_fibo(5)` = `nth_fibo(4)` + `nth_fibo(3)` = 2 + 1 = 3.

# ### Result

# Thus, the 5th term of the Fibonacci series is 3.

# Here's a quick summary of the Fibonacci sequence for reference:
# - 0, 1, 1, 2, 3, 5, ...

# As seen, the 5th term is 3.