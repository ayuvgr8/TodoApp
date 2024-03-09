filenames = ["1.reports", "1.presentation", "1.doc"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)

new = []

for i in [1, 2, 3]:
    new.append(i + 10)

print(new)


new = [i for i in ['a', 'b', 'c']]
print(new)


names = ["john smith", "jay santi", "eva kuki"]

names = [name.title() for name in names]
print(names)