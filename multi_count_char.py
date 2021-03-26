# counts how many time a pattern of string characters appears in a word.

def count_multi_char_x(word, x):
  splits = word.split(x)
  return (len(splits)-1) 

print(count_multi_char_x("mississippi", "iss"))
# prints: 2
print(count_multi_char_x("apple", "pp"))
# prints: 1