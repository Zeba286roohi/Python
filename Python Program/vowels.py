x=input('Enter a word')
y={'a','e','i','o','u'}
result={}
for c in word:
    if c in y:
        result[c]=result.get(c,0)+1
        for k,v in result.items():
            print(k,"is present",v,"times")
