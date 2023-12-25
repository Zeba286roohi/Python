#printing all letter except 'o' 'v'
i=0
a="codevidya"
while i<len(a):
    if a[i]=='o' or a[i]=='v':
        i=i+1
        continue
    print("Current letters are:",a[i])
    i=i+1
#break statements soon it sees 'd'
i=0
a="Codevidhya"
while i<len(a):
    if a[i]=='i':
        i=i+1
        break
    print("Current letters are:",a[i])
    i=i+1

i=0
a="codevidhya"
while i<len(a):
    i=i+1
    pass
print("Values of i",i)
