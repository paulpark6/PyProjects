
# writing a python webbrowser ---

import socket 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates socket but not associate
#                   host         port
mysock.connect(('data.pr4e.org', 80)) # hos is phone number and port is like the phone extension
# extended socket and connected to webserver using port 80
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode()) 
mysock.close()


# HTTP - Hypertext Transfer Protocol

# what happens when you click on a link on a webpage?

# clicking on hyperlinks
# browser sends the request
# webserver answers in the HTML format to browser
# gives the webpage

# using urllib 
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print(fhand) # encoded url -> object like a file
word_count = dict()
for line in fhand: # decode process
    dec_line = line.decode()
    print(dec_line.rstrip())
    words = dec_line.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
top_10 = sorted([(v,k) for  k,v in word_count.items()], reverse = True)

print(word_count)
print(top_10)

# reading webpages
print('\n\nreading webpages\n')
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
for line in fhand:
    print(line.decode().strip())

