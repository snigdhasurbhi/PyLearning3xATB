#list of letter i want to print, if we know how to make function then we can use fliter
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
row = ""
#find filters vowels
def let_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter.lower() in vowels else False
    return letter in vowels
filtered_vowels_letter = filter(let_vowels, letters)
print(list(filtered_vowels_letter))
result = (let_vowels("o"))
print(result)

