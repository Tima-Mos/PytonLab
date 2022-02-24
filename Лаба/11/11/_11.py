string="google.com"
lenn=len(string)
for i in string:
    if string.count(i)!=0:
        print('<'+i+'>:',string.count(i),end=', ')
    for a in string:
        string=string.replace(i,'')
