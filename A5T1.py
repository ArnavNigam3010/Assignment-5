dict = {"Alice":"95","Bob":"93","Charlie":"96"}
name = input("Enter the student's name : ")
name = name.capitalize()
if name in dict.keys():
    print("{}'s marks: {}".format(name,dict[name]))
else:
    print("Student not found")