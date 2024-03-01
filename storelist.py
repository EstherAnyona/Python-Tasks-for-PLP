#This program stores a list of words and uses list comprehension to create a new list that contains only the words that have an odd number of characters.

word_list = ["beautiful", "treasure", "heartfelt", "sweet", "amazing"]
odd_length_words = [word for word in word_list if len(word) % 2!= 0]

print("Words with odd number of characters:", odd_length_words)

