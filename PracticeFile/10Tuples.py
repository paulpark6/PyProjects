# tuples are like sequence that functions like list
x = ('a', 'b', 3)
assert(x[1] == 'b')

# tuples are immutable -> they are more efficient
try:
    x[1] = 't'
except:
    print('cannot modify a tuple!')
# tuples only count, and index
(x,y) = ('hello', 'world')
assert(x == 'hello')
assert(y == 'world')

d = dict()
d['one'] = 1
d['two'] = 2
# d.items() is like list of tuples
for (k,v) in d.items():
    print(k,v)

assert((0,1,2) < (5,-1,2)) # only checks first element in this case
assert((0,1,2) > (0,-1,2)) # checks first and second

d = dict()
d = {'b':1, 'a' :100, 'c':22}
print(d)
sorted_d = sorted(d.items())
print(sorted_d)

# creates a temp list
temp = list()
for (k,v) in d.items(): # changes value and keys and store to temp list as list of tuples
    temp.append((v, k))
print(temp)

temp = sorted(temp, reverse = True) # sorted decend
print(temp)