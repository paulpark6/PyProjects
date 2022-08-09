from ast import IsNot
import email


def print_list(things):
    print('-------------------------------------')
    # List Data Structure
    ln = len(things)
    i = 0
    for thing in things:
        if i is 0:
            print('[',thing, ', ', end = '')
        if i is not 0 and i is not (ln - 1):
            print(thing, end = ', ')
        if i is (ln - 1):
            print(thing, ']')
        i += 1
    print('-------------------------------------')

# strings are immutable but lists are mutable
# need to make a new string when editing
# do not need to make a new list when editing

#         0       1       2        3      4
foods = ['Ramen','Pizza','Salmon','Beef','Pork']
print_list(foods)

foods[0] = 'Chicken'
foods[1] = 'Salad'

print_list(foods)

# range keyword
for i in range(10):
    print(i)

# concatenating lists using '+' and sliced using ':'
# creating an empty list
list = list()
print(type(list)) # <- all the list cammands you can use
for thing in dir(list):
    print(thing)

# list does not have to contain same type
list.append(1)
list.append(102)
list.append('book')
list.append(0)

element = 'book'

# checking if element is in list
print(element in  list)

# how you remove in lists -> removes only the first occurance
list.remove('book')

# sorting reuires data to be in same type
list.sort()
print_list(list)

print(sum(list)) # only for int values
print(min(list)) # only for int values
print(max(list)) # only for int values
print(len(list))

list_str = ['hello', 'bye', 'ask']
list_str.sort()
print_list(list_str)

str = 'hello bye good byes'
str_list = str.split() # when split has no parameters it will split all whitespace
print_list(str_list)
str = 'hello,bye,good,byes'
print_list(str.split(','))

email_info = 'from 03paulpark@gmail.com Sat Jan 03 2025'
list = email_info.split()
name = list[1].split('@')[0]
domain = list[1].split('@')[1]
date = list[2:]
print(name)
print(domain)
print(date)
