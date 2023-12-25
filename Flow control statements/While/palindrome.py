def palind(s):
    return s==s[::-1]
s="malayalam"
ans=palind(s)
if ans:
    print("yes")
else:
    print("No")
