str = "djlnisnjns"

print(str[::-1])


mydict = {1:"A", 2:"B"}
mydict[3] = "c"
mydict[5] = '4'
mydict[4] = '3'
mydict["djl"] = "clever"
mydict[(1, 2, 3)] = "number"
print(mydict)
print(mydict.get(1))
mydict.clear()
print(mydict)

myset = {1, 2, 3, 4, (1, 3), "djl"}
print(myset)


myset1 = set("abcdgh5628")
myset2 = set("abchjk3679")
print(myset1 | myset2)
print(myset1 & myset2)
print(myset1 - myset2)
print(myset2 - myset1)
print(myset1 ^ myset2)


