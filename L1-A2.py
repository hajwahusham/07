# empty dictionary
my_dict = {}

# dictionary with intger keys
my_dict = {1:'apple', 2:'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2,3,4]}

my_dict = {'name': 'Jack', 'age': 26}

# output jack
print(my_dict['name'])
print(my_dict.get('age'))

#update value
my_dict['age'] = 27
print(my_dict)

#add item
my_dict['address'] = 'downtown'
print(my_dict)

#remove a particular object
my_dict.pop('age')
print(my_dict)

#access a particular element
print("address: ", my_dict.get('address'))

#remove all elemnts
my_dict.clear()
print(my_dict)