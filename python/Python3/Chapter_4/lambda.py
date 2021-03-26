animals = ['lion', 'rabbit', 'dog', 'cat']

# Without lambda
def print_word(words, func):
    for word in words:
        print(func(word))
        
def emphasize(word):
    return f"{word}!!!"

print_word(animals, emphasize)

# With lambda
print_word(animals, lambda word: word.capitalize() + "!!!!!!!!!")