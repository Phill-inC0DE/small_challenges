def exponents(bases, powers):
  new_lst = []
  for num in bases:
    for power in powers:
      new_lst.append(num ** power)
  return new_lst


print(exponents([2, 3, 4], [1, 2, 3]))