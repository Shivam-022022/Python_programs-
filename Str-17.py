# Anagram Check
# Check whether two strings are anagrams.

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

if sorted(string1) == sorted(string2):
    print("Anagrams")
else:
    print("Not anagrams")
