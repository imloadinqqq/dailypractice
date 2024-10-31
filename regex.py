import re

print(re.search("1\+1=2", "The following statement is true: 1+1=2"))
print(re.search("J..k", "Jack is a boy"))
print(re.findall("[Gg]r[ae]y", "Grayson drives a grey sedan"))
print(re.findall("[+-]", "1+1-2+1"))
print(re.findall("[0-9a-fA-F]", "The HTML code for white is #FFFFFF"))
print(re.findall("q[^u]", "Qatar is home to quite a lot of Iraqi citizens, but is not in Iraq"))
print(re.findall("[\s\d]", "1 + 2 = 3"))
print(re.findall("[\D]", "1 + 2 = 3"))

# repetition
print(re.findall("<[A-Za-z][A-Za-z0-9]*>", "<HTML><h1>Title</h1>Regex is <b>Awesome</b></HTML>"))
print(re.findall("<[A-Za-z]+>", "Watch out for invalid <HTML> tags like <1> and <>!"))