
## find how to write to files...

### function takes in data that was read from a txt file and replaces all space with '_'
### function will dead with lines
def underScore_lines(data):
    new_data= ''
    for lines in data:
        new_data += lines.replace(' ', '_')
    return new_data


location = input('enter file location!')
try: 
    data = open(location)
except:
    print('location unavailable')
    quit()

new_data = underScore_lines(data)
print(new_data)
#print('the original data was:\n' , text , '\n', 'the new data is: \n' , new_data)




    