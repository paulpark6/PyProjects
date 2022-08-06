#loop and iterations

print(0 is 0.0)

# while loops are indefinite loops -> it keeps going until statement is false
n = 0
while True:
    n = input('Input the number of iterations: ')
    try:  # if this causes error move to except
        # this will cause an error if input is a string literal not string_integer
        n = int(n)
        break
    except:  # when input was a string not integer
        print('type in a integer!')

# definite loops -> for keyword
for i in range(n):
    print(i)

for i in [5,4,3,2,1]:
    print(i)

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print(friend)

#"is" and "is not" operators "is" and "is not" will consider both type and equality of variable
print("helo" is not "bye"); # will print true
print("helo" is "bye"); # will print false
print(0 == 0.0) # this is true
print(0 is 0.0) # this is false

# finding the smallest value
min = None # none is a special type for saying nothing
data = [5,2,8,14,87,21,1,2,400]
for value in data:
    if min is None or min > value:
        min = value;
print('the smallest is ', min)

# scope of python is weird... still can access last wtf....
for stuff in data:
    last = stuff
print(last)
