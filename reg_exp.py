Charcter Classes

'.'- Any character
'\d'- Digit(0-9)
'\D'- Not a digit
'\w'- Word character(a-z, A-Z, 0-9, _)
'\W'- Not a word character
'\s'- Whitespace(space, tab, newline)
'\S'- Not a Whitespace

Below are called Anchors. They dont actually matches any of the matches; 
but, rather invisible positions before or after characters. We can use it conjuctions with other patterns
for searching for.

'\b'- Word boundary- between '\w' and '\W', ie; indicated by Whitespaces or alphanumeric charcater.
For combining different matches using more than one condition like startswith or endswith
'\B'- Not Word boundary
'^'- Beginning of a string
'$'- End of a string

Other categories- Special Charcters, Sets, groups, Popular functions.

print('test git success!')
https://www.dataquest.io/blog/regex-cheatsheet/- For reference
