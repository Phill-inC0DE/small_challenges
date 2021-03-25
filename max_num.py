def max_num1(num1, num2, num3): 
  if num1 > num2 and num3:
    return num1
  elif num2 > num1 and num3:
    return num2
  elif num3 > num1 and num2:
    return num3
  else:
    return "It's a tie!"


print(max_num1(-10, 0, 10))
# prints 0
print(max_num1(-10, 5, -30))
# prints 5
print(max_num1(-5, -10, -10))
# prints -5
print(max_num1(2, 3, 3))
# prints 3

def max_num2(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

# Uncomment these function calls to test your max_num function:
print(max_num2(-10, 0, 10))
# prints 10
print(max_num2(-10, 5, -30))
# prints 5
print(max_num2(-5, -10, -10))
# prints -5
print(max_num2(2, 3, 3))
# prints "It's a tie!"

# WTF?! Whyyyyyyyy??? in max_num2 return shouldn't return any other
# number besides the one mentioned, so how does it return num3 in 
# the first print output.

# Secondly, both codes should work exactly the same yet they don't.
# If code2 is able to tell which is larger, why can't code1??? 

# ** other type of max_num **
def max_num3(nums):
  max_num = nums[0]
  for numbers in nums:
      if numbers > max_num:
        max_num = numbers
  return max_num

print(max_num3([50, -10, 0, 75, 20]))

# Also, max() is an easier option.


