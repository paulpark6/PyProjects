# XML -> eXtensible Markup Language
import xml.etree.ElementTree as ET
# tripple quote string allows enter key
data = '''
<person>
<name> Chuck </name>
<name> Kidions </name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

# JavaScript Object Notation
# json returns a dictionary
import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
        },
    "email" : {
            "hide" : "yes"
            }
    }'''

info = json.loads(data)
print('Name:', info["name"]) # it is a dictionary
print('Hide:', info["email"]["hide"])