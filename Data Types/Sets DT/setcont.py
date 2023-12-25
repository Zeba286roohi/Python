#superset():
s1={10,20,30,40}
s2={10,20}
s3={10,20,50,60}
s1.issuperset(s2)#true
s1.issuperset(s3)#false

#issubset():

s1.issubset(s2)

#intersection()
s1={10,20,30,40}
s2={10,20}
s3=s1.intersection(s2)
print(s3)

s3=s1.union(s2)
print(s3)

#difference()
s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.difference(s2)
print(s3)#it will consider s1 remaining ele
s4=s2.difference(s1)
print(s4)#it will consider s2 remaining ele

#symmetric():

s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.symmetric_difference(s2)
print(s3)#collectively takes ele



