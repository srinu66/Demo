
thislist = ["apple", "banana", "cherry"]

print(thislist)

thislist.append("Lemon")
print(thislist)

thislist.insert(0,"Orange")
print(thislist)

thislist.remove(thislist[3])
print(thislist)

fruits = thislist.copy()
print(fruits)

fruits.insert(0, "cherry")
print(fruits)

thislist.sort()
print(thislist)

myList = [20, 95, 55, 63, 93, 121, 140, 220, 35]
myList.sort()
print(myList)

myList.sort(reverse=True)
print(myList)

for x in myList:
    print(x)


i=0
while(i<100):
    i=i+1
print(i)
myList = myList.insert(0,i+1)






