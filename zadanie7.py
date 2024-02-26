
words = ["Marek", "Jarek", "Dariusz", "Arkadiusz", "Max"]


filtered_words = list(filter(lambda word: len(word) > 5, words))

print(filtered_words)
