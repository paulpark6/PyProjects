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


x = 'finding matching things liQke 1 or 30 of 3'
y = re.findall('[0-9]+', x) # find all 0~9 digit or above
print(y)
y = re.findall('[AEFK]+',x) # find all upper case A E F K
print(y)
