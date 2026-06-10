string = 'hello world'
rev = string[::-1]
print(rev)

var = string[::-1]
print(var)

rev = ''
for char in string:
    rev = char + rev
    # print(rev)
print(rev)

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
rev = reverse_string(string)
print(rev)
print(string[1:])
# print(len(string))

def factorial(data):
    if data == 0:
        return 1
    else:
        return data * factorial(data - 1)
print(factorial(5))