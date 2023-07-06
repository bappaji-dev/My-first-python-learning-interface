from function import student

# import requests
# import math
# r = requests.get('https://www.python.org/downloads/')
# print(r.status_code)
# print(help(requests))

language = "python"
if language == "python":
    print(language)

# loops
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("found")
        break
    print(num)

for num in nums:
    if num == 3:
        print("found")
        continue
    print(num)

for num in nums:
    for letter in "abc":
        print(num, letter)

for i in range(1, 11):
    print(i)

# while loop
x = 0
while x < 10:
    print(x)
    x += 1
while True:
    if x == 100:
        break
    print(x)
    x += 1
