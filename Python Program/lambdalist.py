lst=[2,3,4,5]

result=list(map(lambda n:n*2,lst))
print(result)

#decor strinh

def decorfun(fun):
    def inner(n):
        result=fun(n)
        result += "How are you"
        return result
    return inner
def hello(name):
    return "Hello" +name

print(hello("john"))
