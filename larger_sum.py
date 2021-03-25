def larger_sum(lst1, lst2):
  list1 = 0
  list2 = 0
  for num1 in lst1:
    list1 += num1
  for num2 in lst2:
    list2 += num2  
  if list1 >= list2:
    return lst1
  else:
    return lst2

def larger_sum1(lst1, lst2):
    sum1 = sum(lst1)
    sum2 = sum(lst2)
    if sum1 >= sum2:
        return lst1
    else:
        return lst2
  
print(larger_sum1([1, 9, 5], [2, 3, 7]))