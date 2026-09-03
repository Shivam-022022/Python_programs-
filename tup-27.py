# Problem Statement:
# Store runs scored in 10 matches and calculate:

# Answer:
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

merged = tuple1 + tuple2
result = ()

for value in merged:
    if value not in result:
        result += (value,)

print(result)
