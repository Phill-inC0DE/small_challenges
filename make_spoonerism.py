def make_spoonerism1(word1, word2):
  new_string1 = ""
  new_string2 = ""
  new_string1 += word2[0] + word1[1:]
  new_string2 += word1[0] + word2[1:]
  complete = new_string1 + " " + new_string2
  return complete

def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a