# Store scores of a batsman in 10 matches and calculate:
# • Highest score
# • Lowest score
# • Total runs
# • Average runs
# • Number of centuries (≥100)
# • Number of half-centuries (50–99)

scores = []

for i in range(10):
    scores.append(int(input("Enter score: ")))

highest = scores[0]
lowest = scores[0]
total = 0
centuries = 0
half_centuries = 0

for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    total += score

    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

average = total / len(scores)

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)
