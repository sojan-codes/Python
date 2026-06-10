i = 0

while(i<=10):
    print(i)
    i = i + 1

counter = 1

while True:
    print(counter)

    counter = counter + 1
    if counter > 10:
        break

fruits = ['apple', 'banana', 'mango']

for f in fruits:
    print(f)

print('----- using continue statement -----')
for i in range(10):
    if i == 5:
        continue
    print(i)
    
print('----- using break statement -----')
for i in range(10):
    if i == 5:
        break
    print(i)
