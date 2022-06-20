# python has no command for declaring variables
num = input("What is your number: ")
print("this is the number you typed " + num)
# print("this is the number you typed " + int(num)) # <- you cannot print int and str at same time

# conditionals
x = 5
if x > 1:
    # this prints with no new line but instead prints '' so end=' ' will print space
    print(x, end='')
    print(' is greater than 1\n')
print('I am out of if statement now because I did not indent')

for i in range(5):  # this is a for loop where i = 0 until i < 5
    if i > 3:
        print(i, end=' ')
        print('is greater than 3')
    else:
        print(i)
    print('done with i=', i)
print('All done')
