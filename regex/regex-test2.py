#!/usr/bin/python


##### -- #!/usr/local/bin/python3

import re

regextest = "\.(.*)\{\R\W*(background-color|color)\:\W\$(.*)\;.*\}"

regex = r'(.*) are (.*?) .*'
regex2 = r'\.(.*)\{\R\W*(background-color|color)\:\W\$(.*)\;.*\}'
regex3 = r'\.(.*)\{\n\W*(background-color|color)\:\W\$(.*)\;\W\}'

regex4 = r'(background-color|color)'

regex5 = r'/(.*) are (.*?) .*/gm'

# Virker i regex101.com for python
regex6 = r'\.(.*)\{\n\W*(background-color|color)\:\W\$(.*)\;\W\}'

line = "Cats are smarter than dogs"

line2 = '''
Cats are smarter than dogs

Cats are smarter than dogs

'''

line3 = '''
.fdk-color-primary {
    color: $color-primary; }

.fdk-bg-color-primary {
    background-color: $color-primary; }

.fdk-color-primary-light {
    color: $color-primary-light; }

.fdk-bg-color-primary-light {
    background-color: $color-primary-light; }

.fdk-color-primary-lighter {
    color: $color-primary-lighter; }

.fdk-bg-color-primary-lighter {
    background-color: $color-primary-lighter; }
'''

matchObj = re.match( regex, line2, re.MULTILINE)
#matchObj = re.match( regex, line)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   # print ("matchObj.group(1) : ", matchObj.group(1))
   # print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


# if re.findall('color', line3, re.M):
#      print('found color!')



str = 'an example word:cat!!'
#match = re.search(r'background', line3)
match = re.search(regex4, line3)


# If-statement after search() tests if it succeeded
if match:
  print 'found group: ', match.group() ## 'found word:cat'
else:
  print 'did not find'



#str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
#tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)

tuples = re.findall(regex6, line3)
#print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
   print tuple[0]  ## css classname
   print tuple[1]  ## (background-color|color)
   print tuple[2]  ## color var
   print "---"