# dictionary ADT collection
# keys and values can be anything

# making a dictionary
comp = dict()
comp['mouse'] = 1000
comp['monitor'] = 144
comp['keyboard'] = 70
print(comp)

# updating values
comp['keyboard'] += 30
print(comp)

# getting values using key
print(comp['mouse'])

new_dict = {'one': 1, 'two':2, 'three': 3}
print(new_dict)

# checking if key is inside dictionary
print('four'in new_dict)

# example of historam data
names_dict = dict()
names = ['Paul', 'Park', 'Junwon', 'Shibal', 'Park', 'Paul' , 'Gessekki', 'JotKKa' , 'Junwon']
for name in names:
    if name not in names_dict:
        names_dict[name] = 1
    else:
        names_dict[name] += 1
print(names_dict)

# solving this code with get: same code as above
names_dict2 = dict()
for name in names:
    names_dict2[name] = names_dict2.get(name, 0) + 1 #.get(key, default value) + 1 will increment if kay is found
print(names_dict2)

print(names_dict2.get('woeifjwoiefj',0))
print(names_dict2.get('Shibal'))
print(names_dict2.get('Shibal', 4)) # will not change the value like this
print(names_dict2)
# updating known values in dictionaries
new_shibal = {'Shibal': 100} # create new dictionary with keys and values
names_dict2.update(new_shibal) # use update
print(names_dict2)

# loop that build dictionary

## count_words(text) given the text it returns a dictionary of all the words and the count for each word 
def count_words(text):
    words = dict()
    for word in text.split():
        words[word] = words.get(word, 0) + 1
    return words
data = open("C:\GitHub-Projects\PyProjects\PracticeFile\\test.txt")
print('\n\ncounting words\n\n')
word_dictionary = count_words(data.read())

# looping through dictionary

for key in word_dictionary:
    print(key, word_dictionary[key])

# turnint keys into lists
print(list(word_dictionary))
# getting keys in dictionary
print(word_dictionary.keys())
# getting values of each key, same order as the key
print(word_dictionary.values())

for key,value in word_dictionary.items():
    print(key, value)