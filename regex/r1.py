import re

string='search inside of this text please !'
pattern=re.compile('this')
a=re.search('this',string) #returns an object with the start and end index, gives none if no match
b=pattern.search(string) #another method
print(a.span())
print(a.start(),a.end(), a.group()) # is usefull for multiple searches
print(b)
c=pattern.findall(string)
d=pattern.fullmatch(string) #only if entire string is same / other than match(for 0 or more matches)
print(c,d)