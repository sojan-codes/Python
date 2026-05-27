data = ('apple', 'banana', 'orange')
data2 = ['apple', 'banana', 'orange']

#list into tuple 

data_tuple = tuple(data)
print(data_tuple)

#tuple into list

data_list = list(data)
print(data_list)

#string data type into tuple and list

my_string = "Hello World"

my_string_tuple = tuple(my_string)
my_string_list = list(my_string)

print(my_string_tuple)
print(my_string_list)

rev_string_tuple = ''.join(my_string_tuple)
rev_string_list = ''.join(my_string_list)

print(rev_string_tuple)
print(rev_string_list)

#similarly
# normal_data = "Quest"
# merged_list = (normal_data)
# merged_tuple = [normal_data]

# print(merged_list)
# print(merged_tuple)


