'''Reading Files'''

from sys import argv

script, filename = argv
#filename = 'ex15_sample.txt'

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close() # it should be closed.

print("Type the filename again.")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()