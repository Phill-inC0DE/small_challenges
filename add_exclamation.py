def add_exclamation(word):
  for x in range(len(word),20):
    word += "!"
  return word

# OR

def add_exclamation1(word):
  while(len(word) < 20):
    word += "!"
  return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn