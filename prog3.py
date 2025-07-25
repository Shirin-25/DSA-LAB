n=5
lst=[1,2,3,4,5]
print("first element",lst[0])
print("last element",lst[-1])
print("all element")
for i in lst:
    print(i,end='')
print("\n reversed list")
lst.reverse()
for i in lst:
    print(i,end='')