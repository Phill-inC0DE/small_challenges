# Prints out the given word backwards.

# example 1
def reverse_string(word):
  return word[::-1]

# OR

# example 2
def reverse_string1(word):
  reverse_str = ""
  for i in range(len(word)-1, -1, -1):
    reverse_str += word[i]
  return reverse_str

print(reverse_string("Codecademy"))
# prints: ymedacedoC
print(reverse_string("Hello world!"))
# prints: !dlrow olleH
print(reverse_string(""))
# prints: