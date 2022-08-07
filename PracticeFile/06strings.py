# strings data type

from string import whitespace


str = "string gone"
char_0 = str[0]
print(str)
print(char_0)

# getting length of string
print(len(str))

print('\nprinting with while loop with index number')
i = 0;
while i < len(str):
    letter = str[i]
    print(i, ': ', letter)
    i += 1

print('\nprinting with for loop')
for char in str:
    print(char)

print('\n\n slicing strings\n\n')
# slicing strings
#    0123456789
s = 'MontyPythn'
print(s[0:4]) # does not include index 4
print(s[5:103]) # goes to the end
print(s[5:]) # goes to the end
stuff = s[0:5]
print(stuff, 'Python')

print('p' in s) # asking is 'p' is in s?
print('pyth' in s) # asking is 'pyth' is in s?

cmp = input('say anything!: ')
if cmp < 'paul':
    print(cmp, ' is comes before paul')
elif cmp > 'paul':
    print(cmp, 'comes after paul')
else:
    print(cmp, 'is equal to paul')

# string library -> string is an object
name = 'Paul Park'
low_name = name.lower()
hi_name = name.upper()
print(name, low_name, hi_name)


# search online for string methods
pos = name.find('Pa') # find the first occurance of Pa
new_name = name.replace('Paul', 'Junwon')
print(name) # name is unchanged
print(new_name)

white_space = '    Good Day Fm Days   '
print(white_space.lstrip()) # removes left white spaces
print(white_space.rstrip()) # removes right white spaces
print(white_space.strip()) # removes start and end white spaces

# .startswith('______')
print(name.startswith('Paul'))

email = "03paulpark@gmail.com Sat Jan 5 09:13:16 2003"
pos_a = email.find('@')
pos_space = email.find(' ', pos_a) # starting from pos_a find the next space
domain = email[pos_a + 1 : pos_space]
print(domain)

