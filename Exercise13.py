import re
words = []
file = open("Exercise13.txt", "r", encoding="utf8")
for i1 in file:
    line = re.findall(r"\w+", str(i1))
    for i2 in line:
        words.append(i2)
file.close()
couples = []
n = len(words)
i1 = 0
start = 1
while i1 < n:
    bool = False
    n = len(words)
    i2 = start
    while (i2 != n) and not bool:
        if len(words[i1]) + len(words[i2]) == 20:
            couples.append([words[i1], words[i2]])
            words.pop(i2)
            words.pop(i1)
            bool = True
        i2 += 1
    if not bool:
        start += 1
        i1 += 1
for i in couples:
    print(i)
