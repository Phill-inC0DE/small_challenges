# cycles through each base number & returns them powered by each of the powers digits.

def exponents(bases, powers):
  new_lst = []
  for num in bases:
    for power in powers:
      new_lst.append(num ** power)
  return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))
# prints: [2, 4, 8, 3, 9, 27, 4, 16, 64]