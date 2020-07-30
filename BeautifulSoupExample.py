import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

##ignore ssl certificate error

ctx =ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode =ssl.CERT_NONE


url = input('Enter')
html =urllib.request.urlopen(url, context=ctx).read()
soup =BeautifulSoup(html, 'html.parser')

#retribe all of span tag
# add on list
lst =list()
tags =soup('span')
for tag in tags:
    print(tag.contents)
    lst.append(tag.contents)
print(lst)
##flattened
updatelst = flattened = []
for sublist in lst:
    for val in sublist:
        flattened.append(val)


        # Printing modified list
updatelst = [int(i) for i in updatelst]
print("Modified list is : " + str(updatelst))
print(updatelst)
print("SUM:", sum(updatelst))



