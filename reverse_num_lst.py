# My Version:
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[0:] == lst2[::-1]:
      return True
    else:
      return False
      
# Codecademy version:
def reversed_list1(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# There is a function reversed() that can make things easier.