#prova
# open a file txt and read it
# return a list of words
file = open("example.txt", "r")
words = file.read().split()
file.close()

print(words)

e_file = []
for word in words:
    if word[0] == "E":
        e_file.append(word)
        words.remove(word)
print(words)
print(e_file)

#create a file txt and write it with the list of words that start with E separatete by endline
file = open("example2.txt", "w")
for word in e_file:
    file.write(word + "\n")
file.close()


