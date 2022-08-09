
### function takes in data that was read from a txt file and replaces all space with '_'
def underScore(data): 
    new_data= ''
    for char in data:
        if char == ' ':
            char = '_'
        new_data += char
    return new_data


data = open("C:\GitHub-Projects\PyProjects\PracticeFile\\test.txt")
text = data.read()
new_data = underScore(text)
print('the original data was:\n' , text , 
'\n', 'the new data is: \n' , new_data)



    