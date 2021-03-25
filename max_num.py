def max_num1(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

# Uncomment these function calls to test your max_num function:
print(max_num1(-10, 0, 10))
# prints 10
print(max_num1(-10, 5, -30))
# prints 5
print(max_num1(-5, -10, -10))
# prints -5
print(max_num1(2, 3, 3))
# prints "It's a tie!"


# ** other type of max_num **
def max_num2(nums):
  max_num = nums[0]
  for numbers in nums:
      if numbers > max_num:
        max_num = numbers
  return max_num

print(max_num2([50, -10, 0, 75, 20]))

# Also, max() is an easier option.


