import os

fileName = 'test.txt'

# create file
txt = open(fileName, 'x')

# write on file
txt.write('This is a test!')

# Read and print the file
txt = open(fileName, 'r')
print(txt.read())

txt.close()

# If the file exists, delete 
if os.path.exists(fileName):
  os.remove(fileName)
  print('.txt has just been deleted.')
else:
  print('cannot delete the file.')
