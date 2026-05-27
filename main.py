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
normal_data = "Quest"
merged_list = (normal_data)
merged_tuple = [normal_data]

print(merged_list)
print(merged_tuple)

#dictionaries
my_dic = {
    "name" : "Sojan Buddhacharya",
    "age" : 20,
    "class" : "bachelor 4th sem"
}

my_tuple = tuple(my_dic.items())
my_list = list(my_dic.items())

print(my_tuple)
print(my_list)

#tuple into dictionaries

tuple_into_dic = (
    ("name","Hari Bahadur"),
    ("age", 20)
)

list_into_dic = [
    ["name","Ram Bahadur"],
    ["age", 21]
]

list_into_dic_data = dict(list_into_dic)
tuple_into_dic_data = dict(tuple_into_dic)

print(list_into_dic_data)
print(tuple_into_dic_data)


