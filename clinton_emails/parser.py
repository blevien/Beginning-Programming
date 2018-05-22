
with open("hillary-clinton-emails-august-31-release_djvu.txt", "r") as emails:
    unique_words = []
    ignore = ["-", ",","'","”","'",".",'"',"!","-", "(", ")"]

    for line in emails:
        line = line.replace("\n", "").split(" ")
        for word in line:
            for c in word:
                if c in ignore:
                    word = word.replace(c, "")

            if word not in unique_words:
                unique_words.append(word)

    print("There are", len(unique_words), "unique words in this file")

    print("The unique words are:")
    print("---------------------")
    for word in unique_words:
        print(word)
