letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Créer un mot et calculer son score
def word_score(word):
    score = 0
    for letter in word:
        if letter in letters:
            score += numbers[letters.index(letter)]
        else:
            print(f"Lettre '{letter}' non trouvée dans la liste des lettres.")
    return score

# Convertir les lettres en nombres
def convert_to_numbers(word):
    new_word = ""
    for letter in word:
        if letter in letters:
            new_word += str(numbers[letters.index(letter)])
        else:
            print(f"Lettre '{letter}' non trouvée dans la liste des lettres.")
    return new_word

print(word_score("abc"))  # Cela devrait imprimer 3, car a=0, b=1, c=2
print(convert_to_numbers("abc"))  # Cela devrait imprimer "012", car a=0, b=1, c=2
