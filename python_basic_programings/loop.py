for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)

for i in range(0, 10, 2):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

count = 1
while count <= 5:
    print(count)
    count = count + 1  # Or count += 1

### ⚠️ Important: Make sure to include code inside the while loop that will eventually make the condition False. 
# Otherwise, you'll create an infinite loop, which will run forever and freeze your program. 
# In the example above, count = count + 1 is the line that ensures the condition count <= 5 will eventually become false.