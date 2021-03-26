# add an exclamation mark in the white space, from the end of the word until it reaches 20 characters.

def add_exclamation(word):
  for x in range(len(word),20):
    word += "!"
  return word

# OR

def add_exclamation1(word):
  while(len(word) < 20):
    word += "!"
  return word

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
