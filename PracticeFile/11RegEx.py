# regular expressions

# smart searching...
# like crtl + f
# need to import re
import re

file = open('C:\GitHub-Projects\PyProjects\PracticeFile\\test.txt')
for line in file:
    line  = line.strip()
    if re.search('and', line):
        print(line)
