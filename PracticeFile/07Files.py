# reading files

# opening functrion to help read file

# file = open(filename, mode) 
## mode = 'r' if we are reading file 
##'w' if we are writing to the file
## 'r+' read or write mode
## 'a+' read of append mode

# reading files .txt as sequence of lines
path = "C:\GitHub-Projects\PyProjects\PracticeFile\\test.txt"
file_path = input("enter file path: ")
try:
    file = open(file_path)
except:
    print('wrong file path\ncannot find file')
    quit() # need to put this because file will blow up if file has wrong path
# thing = file.read()
# print(thing)
# can only read file once! then its over
count = 1

#for stuff in file:
#    # print('line Count', count)
#    print(stuff.rstrip())
#    count += 1

for line in file:
    line = line.rstrip()
    if not 'paul' in line:
        continue
    print(line)
