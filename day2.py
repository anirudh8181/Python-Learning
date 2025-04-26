

#----------------strings-----------------------

name=input("enter the name :")
result=len(name)

#finds a particular character at a index position
result1=name.find("ni")

#finds a particular character at a index position
result2=name.rfind("ni")

print(result)
print(result1)
print(result2)

#capitalizes first letter of the word
print(name.capitalize())

#capitalizes the entire word
print(name.upper())

#lower case fun
print(name.lower())

#isdigit checks if the strings are digits and return true or false
print(name.isdigit())

#isalpha Checks if all characters are letters
print(name.isalpha())

#isalnum checks if all characters are alphanumneric
print(name.isalnum())


#few more important methods

'''
replace(old, new)	Replaces substring	'a-b-c'.replace('-', '+') → 'a+b+c'

strip()	Removes whitespace from both ends	' hi '.strip() → 'hi'

lstrip()	Removes leading whitespace	' hi'.lstrip() → 'hi'

rstrip()	Removes trailing whitespace	'hi '.rstrip() → 'hi'

replace(old, new)	Replaces substring	'a-b-c'.replace('-', '+') → 'a+b+c'

split(delimiter)	Splits string into a list	'a,b,c'.split(',') → ['a', 'b', 'c']

join(list)	Joins list into a string	'-'.join(['a', 'b', 'c']) → 'a-b-c'

count(sub)	Counts occurrences	'banana'.count('a') → 3

startswith(prefix)	Checks if string starts with prefix	'hello'.startswith('he') → True

endswith(suffix)	Checks if string ends with suffix	'hello'.endswith('lo') → True

'''

#----------------string slicing-------------------

text = "Python"

print(text[1:4])   # 'yth' → from index 1 to 3 (end is exclusive)
print(text[:3])    # 'Pyt' → from beginning to index 2
print(text[3:])    # 'hon' → from index 3 to end
print(text[-4:-1]) # 'tho' → from -4 to -2

print(text[::-1])
