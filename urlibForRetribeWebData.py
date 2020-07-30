import urllib.request, urllib.parse, urllib.error
data = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

counts =dict()
for line in data:
    words=line.decode().split()
    print(line.decode().strip()) #print data
    for word in words:
        counts[word] =counts.get(word,0)+1
print(counts)

data = urllib.request.urlopen('https://www.dr-chuck.com/page1.htm') #retrive web html data
for l in data:
    print(l.decode().strip())