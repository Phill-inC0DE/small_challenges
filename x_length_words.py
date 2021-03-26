# checks to see if each word has the correct number of characters allocated.
# and returns true or false, if they do or don't.

def x_length_words(sentence, x):
  new_sent = sentence.split()
  for word in new_sent:
    if len(word) < x:
      return False
  return True

print(x_length_words("i like apples", 2))
# prints: False
print(x_length_words("he likes apples", 2))
# prints: True