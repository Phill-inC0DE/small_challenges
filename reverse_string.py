# example 1
def reverse_string(word):
  return word[::-1]

# example 2
def reverse_string1(word):
  reverse_str = ""
  for i in range(len(word)-1, -1, -1):
    reverse_str += word[i]
  return reverse_str

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print