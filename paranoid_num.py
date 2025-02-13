# "The Paranoid Number Detector" 🤯
# Goal:
# Detect if a number is "paranoid." A number is paranoid if:
# - It contains the digit 7.
# - The sum of its digits is odd.
# - It is not a multiple of 5.

def is_paranoid(num):
    num_str = str(num)

    if "7" in num_str: 
        digit_sum = 0 

        for digit in num_str:  
            digit_sum += int(digit)

        return (digit_sum % 2 != 0) and (num % 5 != 0) 

    return False

# Test cases
print(is_paranoid(13))   # ❌ False (no 7)
print(is_paranoid(17))   # ✅ True (contains 7, sum=8 is even, not paranoid)
print(is_paranoid(77))   # ❌ False (contains 7 but multiple of 5)
print(is_paranoid(713))  # ✅ True (contains 7, sum=11 is odd, not a multiple of 5)
print(is_paranoid(175))  # ❌ False (contains 7 but multiple of 5)
print(is_paranoid(71))   # ✅ True (contains 7, sum=8 is even, so should be False)