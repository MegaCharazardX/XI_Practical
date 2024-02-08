import re

def displaymatch(match):
    if match is None:
        return "Invalid Email Address"
    return "Valid Email Address" #'<Match: %r, groups=%r>' % (match.group(), match.groups())

email = input("Enter the email :")
domain = re.compile(r"^[A-Za-z0-9_]+@edupillar.com")

print(displaymatch(domain.match(email)))
input()

input()