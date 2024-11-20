import re

regex = "[A-Z]{1,7}[A-Z0-9*]{5}"

txt = "ABCDEFG1234*"
txt2 = "A1234*"

x = re.match(regex, txt)
y = re.match(regex, txt2)

print(re.match("^[0-9]{5}(?:-[0-9*]{4})?$","64082-1111"))
print(re.match("^[0-9]{5}(?:-[0-9*]{4})?$", "64082")) 

# print(x, y)

#number 6

regex2 = "a{2,4}b{0,4}c{1,2}"


z = re.match(regex2, "aabcc")

# print(z)

print(re.match("[a-z]+(oon)$", "spoon"))


print(re.match("#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", "#FFF"))

print(re.match("[a-z][+*]\s+[A-Z]\.", "a* Z."))

print(re.match("(https?:)//[a-z]+\.[a-z]+\.com", "https://google.web.com"))

############################
# Task 3

print(re.match("\([\d]{3}\)\s[\d]{3}(?:-)[\d]{4}", "(816) 547-8375"))

print(re.match("[\d]{3}(?:-)[\d]{2}(?:-)[\d]{4}", "777-77-7777"))

print(re.match("\d*[013579]", "35"))

print(re.match("^a(a|b)+a$", "abaaabba"))

############################
# Task 4

text = "Tom, tired? Go to bed. Now!!"
tokens = re.findall(r'\w+(?: \w+)*|\w+', text)
print(tokens)

text2 = "It’s12hard4to567put100a43feeling23into90words,456but879when35you444get here,5879you’ll1000get000it."
tokens = re.split(r'\d+', text2)
print(tokens)
