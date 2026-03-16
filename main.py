# AIM: Develop a Python program that reads a text file and
# prints words of specified lengths (e.g., three, four,
# five, etc.) found within the file.

# Coders: Saniya Shaikh 
# Date:13-02-2026

print("--- Extracting Words from Text File ---\n")

with open("story.txt", "r") as file:
    content = file.read()

words = content.split()

length = int(input("Enter Length of words: "))

unique_words = set()

for word in words:
    word = word.lower()

    if len(word) == length:
        unique_words.add(word)

result = sorted(unique_words)

print("Words with length", length, "are:", result)

