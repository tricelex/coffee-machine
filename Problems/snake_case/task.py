word = input('')
new_word = ''
for x in word:

    if x.isupper():
        x = '_' + x.lower()
    new_word += x
print(new_word)
