# program that prints the top 10 words in the file

path = input('enter file path here')
try:
    data = open(path)
except:
    print('Error 404\nFile not found!')
    quit()
word_bank = dict()
for line in data:
    words = line.split()
    for word in words:
        word_bank[word] = word_bank.get(word, 0) + 1

amount = list()
for key, val in word_bank.items():
    tuple = (val, key)
    amount.append(tuple)

amount = sorted(amount, reverse = True)

for val, key in amount[:10]:
    print(key, val)
    