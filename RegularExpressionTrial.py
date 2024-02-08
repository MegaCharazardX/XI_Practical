import re

def displaymatch(match):
    if match is None:
        return "Invalid Email Address"
    return "Valid Email Address" #'<Match: %r, groups=%r>' % (match.group(), match.groups())

email = re.compile(r"^\b[a-zA-Z0-9]+@[a-z]+.[a-z]\b")
print(displaymatch(email.match("1adfasdf23@gmail.com")))
input()
