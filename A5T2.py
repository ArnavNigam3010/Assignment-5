list = []
for i in range(1,11):
    list.append(i)
print("Original list: ",list)
list1 = list[0:5]
print("Extracted first five elements of list: ", list1)
print("Reversed extracted elements: ", list1[::-1])