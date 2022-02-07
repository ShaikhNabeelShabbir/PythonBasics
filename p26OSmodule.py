
str = input("Please enter your details \n")

file = open("demo.txt", 'a+')
file.write("\n"+str)
file = open("demo.txt", 'r')
list = file.read()
print(list)
words = list.split()
l = len(words)
print("Number of words", l)

unique_words = set(words)
print(unique_words)
print("number of unique words", len(unique_words))

words_a = []
for word in unique_words:
    if word[0].lower() == 'a':
        words_a.append(word)

print("word with a", words_a)
print("word with a", len(words_a))
