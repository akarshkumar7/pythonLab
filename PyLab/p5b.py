import re

ph_regex=re.compile(r'\+\d{12}')
mail_regex=re.compile(r'\S+\@\S+')

with open('emailphone.txt','r') as f:
    for line in f:
        pmatch=ph_regex.findall(line)
        for match in pmatch:
            print(match)

        ematch=mail_regex.findall(line)
        for match in ematch:
            print(match)



