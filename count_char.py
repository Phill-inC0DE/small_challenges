# counts how many times a character appears in a string.

def count_char_x(word, x):
  counter = 0
  for letter in word:
    if letter == x:
      counter += 1
  return counter

print(count_char_x("mississippi", "s"))
# prints: 4
print(count_char_x("mississippi", "m"))
# prints: 1
