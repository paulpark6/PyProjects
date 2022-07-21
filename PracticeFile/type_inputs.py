# type() -> tells you what time it is
a = "hello"
b = 'c'
c = 1
d = 2.03
print(type(a),"\n", type(b),"\n", type(c),"\n", type(d))

# type converstions in Python
print(float(19) + 100)

# string conversion
str = '123'
str2 = "123"
num = 7
str = int(str)
print("Printing number plus string str:", num + str, "\n")

# user inputs
name = input('what is your name: ')
print("hello ", name)
# you can also convert use input
age = input('what is your age: ')

# inputs are always string
print(name, " will be ", int(age) + 10, " years old after 10 years")

