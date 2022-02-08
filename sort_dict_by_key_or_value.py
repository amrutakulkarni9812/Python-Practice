# Sort by key
d = {2:3, 1:89, 4:5, 3:0}
sd = sorted(d.items())
print("Sorted by key-------------")
for k,v in sd:
    print(k,v)
print(" ")
# Sort by key descending
d = {2:3, 1:89, 4:5, 3:0}
sd = sorted(d.items(), reverse= True)
print("Sorted by key descending -------------")
for k,v in sd:
    print(k,v)
print(" ")
# Sort by value
d = {2:3, 1:89, 4:5, 3:0}
sd = sorted(d.items(), key = lambda x:x[1])
print("Sorted by value -------------")
for k,v in sd:
    print(k,v)
print(" ")
# Sort by value descending
d = {2:3, 1:89, 4:5, 3:0}
sd = sorted(d.items(), key = lambda x:x[1], reverse= True)
print("Sorted by value descending -------------")
for k,v in sd:
    print(k,v)
