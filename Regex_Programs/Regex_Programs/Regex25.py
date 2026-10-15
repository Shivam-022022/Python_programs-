import re

paragraph = ("Aarav Sharma (Roll No: 101) scored 85 marks. "
             "Diya Patel (Roll No: 102) scored 92 marks. "
             "Rohan Mehta Kumar (Roll No: 103) scored 78 marks.")

pattern = r"([A-Z][a-z]+(?: [A-Z][a-z]+)*) \(Roll No: (\d+)\) scored (\d+) marks"

print(f"{'Name':<20}{'Roll No':<10}{'Marks'}")
print("-" * 36)
for name, roll, marks in re.findall(pattern, paragraph):
    print(f"{name:<20}{roll:<10}{marks}")
