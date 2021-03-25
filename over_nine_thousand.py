def over_nine_thousand(lst):
  sum = 0
  for num in lst:
    sum += num
    if (sum > 9000):
      break
  return sum


print(over_nine_thousand([8000, 900, 120, 5000]))