result = 0
for x in range(1, 101):
    if x % 2 == 0:
        result += x
print(result)

total = 0
for even_num in range(2, 101, 2):
    total += even_num
print(total)