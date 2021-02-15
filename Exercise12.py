text = ""
text2 = ""
file = open("Exercise12.txt", "r", encoding="utf8")
for i in file:
    text = text + i
file.close()
n = len(text)
for i in range(n-1, -1, -1):
    text2 = text2 + chr(128 - ord(text[i]))
print(text2)
