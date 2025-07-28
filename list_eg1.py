lst = ["deep", "ayush", "punith"]
print("original lst = ",lst)

lst.append("ankit")
lst.append("sharan")

print("modified lst (append) =", lst)

lst.insert(1, "gammana")
lst.remove("ankit")
print("modified lst (remove)=",lst)

# lst.remove("ramesh") #ValueError: list.remove (x): x not in list 
#print("modified lst =", lst)

lst.pop()
print("modified lst (pop)=",lst)

lst.pop(1)
print("modified lst (pop)=", lst)

del lst[1]
print("modified lst (del)=", lst)

# del lst
print("after del lst:", lst) #NameError: name 'lst' is not defined.