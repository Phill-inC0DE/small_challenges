# My version
def delete_starting_evens1(lst):
  for num in lst:
    if num % 2 == 0:
      lst.remove(num)
    else:
      break 
  return lst

# Correct version
def delete_starting_evens2(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens2([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens2([4, 8, 10]))