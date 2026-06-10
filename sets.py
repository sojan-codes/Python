#quick recall list=> [], tuple=> (), dic => {}, set => {with data only}

my_set = {1,2,3,4,5}
data = {}

my_fruits = {'apple', 'banana', 'mango', 'banana'}

print(my_set)


# my_fruits.add("grapes")
# my_fruits.remove("apple")

print(my_fruits)

print(type(data))
print(type(my_set))
# print(type(my_dic))


#list into set
list_data = [1,2,3,4,5,5]

list_into_set = set(list_data)
print(list_into_set)

#tuple into set
tuple_data = (1,2,3,4,5,6)

tuple_into_set = set(tuple_data)
print(tuple_into_set)

#dict into set
dic_data = {
    "name": "Sojan Buddhacharya",
    "age": 20
}

dic_into_set = set(dic_data)
print(dic_into_set)

