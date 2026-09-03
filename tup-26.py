# Problem Statement:
# Average temperature

# Answer:
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

common = ()

for value in tuple1:
    if value in tuple2 and value not in common:
        common += (value,)

print(common)
