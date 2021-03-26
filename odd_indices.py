# interates through each number and only prints out the odd indexs.

# My version:
def odd_indices1(lst):
  new_lst = []
  for num in lst:
    if (lst.index(num) % 2 == 1):
      new_lst.append(num)
  return new_lst

# OR

# Codecademy version:
def odd_indices2(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

print(odd_indices1([4, 3, 7, 10, 11, -2]))
# prints: [3, 10, -2]