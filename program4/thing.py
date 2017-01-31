a = [1,2,3,4,5]
b = [5,4,3,2,1]
x = zip(a,b)
newlist = []
for item in x:
    newlist.extend(item)
print (newlist)