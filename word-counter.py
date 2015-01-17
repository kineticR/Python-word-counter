def word_counter(sentence, word):
    counter = 0
    for i in range((len(sentence) - len(word) + 1)):
        print(sentence[i: i + len(word)])
        if sentence[i: i + len(word)] == word:          # print(sentence[i: i + len(word)]) - helpful visualization
            counter += 1
    return counter

print(word_counter("I wore my hat out. It is a great hat. I love my hat. How is your hat", "hat"))