# removes every other letter, every odd index is removed.

def every_other_letter(word):
  every_other = ""
  for letter in range(0,len(word),2):
    every_other += word[letter]
  return every_other

print(every_other_letter("Codecademy"))
# prints: Cdcdm
print(every_other_letter("Hello world!"))
# prints: Hlowrd
print(every_other_letter(""))
# prints:
