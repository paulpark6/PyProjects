# conditional files

x = input("give me a random number ")
x = int(x) # need to type cast to int
if x < 2:
    print("small\n")
elif x < 10:
    print("medium\n")
else :
    print("shits big asf")
print("all done");

# this code will talk about try and expcept keywords
# if 'try' works it skips 'except' 
# if 'try' fails it jumps to 'except'

try:
  f = open("C:/Users/03pau/Desktop/testfile.txt")
  try:
    print("writing file")
    f.write("hello world")
    print("writing succeded")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")