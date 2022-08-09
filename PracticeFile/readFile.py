
### function takes in data that was read from a txt file and replaces all space with '_'
### function will dead with char
def underScore_char(data): 
    new_data= ''
    for char in data:
        if char == ' ':
            char = '_'
        new_data += char
    return new_data

### function takes in data that was read from a txt file and replaces all space with '_'
### function will dead with lines
def underScore_lines(data):
    new_data= ''
    for lines in data:
        new_data += lines.replace(' ', '_')
    return new_data

data = open("C:\GitHub-Projects\PyProjects\PracticeFile\\test.txt")
text = data.read()
#new_data = underScore_char(text)
new_data = underScore_lines(text)
print('the original data was:\n' , text , 
'\n', 'the new data is: \n' , new_data)



    