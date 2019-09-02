dictionary = {
}

with open('declaration.txt', 'r') as declarationFile:
    for line in declarationFile:
        for word in line.split():  # list of words
            word = word.replace(",", "")
            word = word.replace(".", "")
            word = word.replace(":", "")
            word = word.replace(" ", "")
            word = word.lower()
            # print(word)
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary.update({word: 1})

with open('file.txt', 'w') as file:
    for key in sorted(dictionary.keys()):
        line = key + " :: " + str(dictionary[key]) + "\n"
        file.write(line)
