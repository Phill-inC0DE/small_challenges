def every_other_letter(word):
  every_other = ""
  for letter in range(0,len(word),2):
    every_other += word[letter]
  return every_other

print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print