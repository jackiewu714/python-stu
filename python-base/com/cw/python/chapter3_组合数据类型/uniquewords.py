import string
import sys

# 对命令行中给定的所有文件，计算文件中每个字出现的不同的次数
words = {}
strip = string.whitespace + string.punctuation + string.digits + "\""
for filename in sys.argv[1:]:
    for line in open(filename, encoding="utf8"):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] = words.get(word, 0) + 1

for word in sorted(words):
    print("'{0}' occurs {1} times.".format(word, words[word]))
