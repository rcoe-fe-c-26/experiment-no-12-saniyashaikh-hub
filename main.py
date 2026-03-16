# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder:Saniya Shaikh 
# Date:13/02/26

print("--- Extracting Words from Text File ---\n")

length = int(input())

with open("story.txt", "r") as file:
    text = file.read()

words = text.split()

result = sorted(set(w.lower() for w in words if len(w) == length))

print(f"Words with length {length} are: {result}")

