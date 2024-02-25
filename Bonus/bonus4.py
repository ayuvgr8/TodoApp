# Data mutability #tuples

filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt']

# Replacing the String in Python little bit difficult, and we came to know the concept here that is Immutability
# we use function .replace to replace the character in the string
# suppose we need to replace ' .(dot by dash -) ' so we use filename.replace('.'__old , '-' __new  , 1 __count)
# If we want to use tuples then we use (round brackets) to make list immutable

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)