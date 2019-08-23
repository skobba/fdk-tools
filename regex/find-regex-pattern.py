#!/usr/local/bin/python3

# Need python3 
# brew install python3
# ---- #!/usr/local/bin/python3

import re

# Find python version osx -> which python

# print("*** REGEX ***")

regex = "\.(.*)\{\R\W*(background-color|color)\:\W\$(.*)\;.*\}"
# print(regex)

file = open('input.scss')
text = file.read()
file.close()

print(text)

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


# m = re.match(regex, text)




'''

Regex:
\.(.*)\{\n\r

### COLOR
*** FROM ***
.fdk-color-primary {
    color: $color-primary; }

*** TO ***
.fdk-color-primary {
   @include themify($themes) {
       color: themed('color-primary');
   }
}

### BACKGROUND-COLOR
.fdk-bg-color-primary {
    background-color: $color-primary; }

.fdk-bg-color-primary {
   @include themify($themes) {
       background-color: themed('color-primary');
   }
}



'''