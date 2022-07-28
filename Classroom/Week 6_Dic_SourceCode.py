my_dict1 = {1: 'apple', 2: 'ball'}
print(my_dict1)

# dictionary with mixed keys
my_dict2 = {'name': 'John', 1: [2, 4, 3]}
print(my_dict2)

# using dict()
my_dict3 = dict({1: 'apple', 2: 'ball'})
print(my_dict3)

# from sequence having each item as a pair
my_dict4 = dict([(1, 'apple'), (2, 'ball')])
print(my_dict4)


# retrieving elements
my_dict5 = {'name': 'Jack', 'age': 26}
print(my_dict5['name'])
print(my_dict5.get('age'))
print(my_dict5.get('address'))
# print(my_dict5['address'])

# Changing and adding Dictionary Elements
my_dict5['age'] = 27
print(my_dict5)

# add item
my_dict5['address'] = 'Downtown'
print(my_dict5)

# Removing elements from a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares.popitem())
print(squares.clear())

del squares
# print(squares)