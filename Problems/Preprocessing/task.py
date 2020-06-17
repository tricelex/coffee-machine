#  Posted from EduTools plugin
# word = 'Nobody expects the Spanish inquisition!'
word = input()

word = word.strip()
word = word.lower()
word = word.replace(',', '')
word = word.replace('.', '')
word = word.replace('!', '')
word = word.replace('?', '')

print(word)
#
# txt = "     banana     "
#
# x = txt.lstrip()
#
# print(txt)
