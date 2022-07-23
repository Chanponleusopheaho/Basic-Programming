# not duplicates in every element (not the same element)
# Can add or remove but can't modify 
# perform mathematical set operations like union 
# Can Not put the list inside the sets
# un order cuz didn't has sorting 
my_set = {1,4,3,5}
my_set.update([6,7,8,"Hello"]) # add only 1 argument but update can many argument 
my_set.discard(4) # delete number 4 if no element it doesn't care
my_set.remove(3) # but remove if no element it will error 
print(my_set) 
# union mean put it together 
A ={1,2,3,4}
B ={2,4,6,8}
print(A|B)
print(A.union(B))
print(B.union(A))
# intersection put element the same together 
print(A&B)
print(A.intersection(B))
print(B.intersection(A))
# set different 
print(A-B) # is what A different from B

# Symmetric Difference 
print(A^B) # is what difference from A and B combine together 
