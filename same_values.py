# if the value of the value in the first list matches the value of the second, print out the index.

def same_values(lst1, lst2):
  new_lst = []
  for index in range(0, len(lst1)):
    if (lst1[index] == lst2[index]):
      new_lst.append(index)
  return new_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# prints: [0, 2, 3]