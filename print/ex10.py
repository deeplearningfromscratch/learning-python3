'''What Was That?'''

tabby_cat = "\tI'm tabbed in." # \ is escape sequences.
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''  # """""" and '''''' are the same.

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

'''
What makes \\ special compared to the other ones? 
It’s simply the way you would write out one backslash (\) character. Think about why you would need this.
'''