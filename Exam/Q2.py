# Generate a Python function for a movie ticket booking system that checks eligibility based on age.
# The function should accept age as input and return "allowed" if age is greater than or equal to 18, otherwise return "not allowed".
# Include sample function calls and print their outputs to demonstrate correctness.

def check_eligibility(age):
    if age >= 18:
        return "allowed"
    else:
        return "not allowed"

# Sample function calls
print(check_eligibility(20))
print(check_eligibility(18))
print(check_eligibility(15))


# 4. Explanation (Simple)

# The function check_eligibility(age) takes one input → age

# The condition age >= 18 checks if the person is 18 or older

# If true → returns "allowed"

# If false → returns "not allowed"


# 5. Output

# 20 → allowed ✔

# 18 → allowed ✔

# 15 → not allowed ✖