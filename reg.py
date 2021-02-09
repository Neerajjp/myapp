import re

text_to_search = '''
abcdefghijklmnoprstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * * ? { } [ ] \ | ( )

codescreen.com

321-234-333
123.456.556

Mr. Neeraj
Mr Jareen
'''
sentence= 'Start a sentence and bring it to end'

patterns = re.compile(r'^abc$XYZ') #compile allows us to store raw string to a variable. r'.' will show
#error because . itself is a regular expression. To solve add a backslash before the regex. r'\.' will show correct matches.
# can also strings before the '\' to combine. eg: to get codescreen.com

matches = patterns.finditer(text_to_search) #finditer brings all the matches inside a iter;
#'re.compile'-2 arguments- 1-string tobe searced, 2- Where to search in.
for match in matches:
	print(match) #o/p of for loop- match in span(1,4); text_to_speech[0]-enter(blankspace), 1-a, 4

print(text_to_search[0:4])
