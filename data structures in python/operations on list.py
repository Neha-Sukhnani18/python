lst=['apple', 'guava', 'mango', 'banana', 'kiwi']

print("lenght of list:",len(lst))
print("first element:",lst[0])
print("last element:",lst[-1])

lst.append('papaya')
print("updated list :", lst)

lst.remove('guava')
print("updated list:", lst)

lst.sort()
print("sorted list:", lst)

lst.pop(1)
print("updated list:",lst)

lst.reverse()
print("reversed list:",lst)

print("multiplication on list:",lst*2)

lst=lst[:4]
print("sliced list:", lst)

lst.clear()
print("updated list:",lst)