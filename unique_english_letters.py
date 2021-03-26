# Counts how many unique characters are in the allocated string.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  counter = 0
  letter_lst = []
  for letter in word:
    if letter in letters and letter not in letter_lst:
      letter_lst.append(letter)
  counter += len(letter_lst)
  return counter   

print(unique_english_letters("mississipi"))
# prints: 4
print(unique_english_letters("Apple"))
# prints: 4