# Checks if the given name is in the first string, if not it will return false.

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie"))
# prints: True
print(check_for_name("My name is jamie", "Jamie"))
# prints: True
print(check_for_name("My name is Samantha", "Jamie"))
# prints: False
