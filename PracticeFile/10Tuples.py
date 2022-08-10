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
print(d.items())
for (k,v) in d.items():
    print(k,v)
