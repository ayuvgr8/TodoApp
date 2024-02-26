# how to print them in alphabetical order
waiting_list = ['sen', 'ben', 'ten']
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}. {item.title()}"
    print(row)

list1 = [1, 2111, 333, 433, 53, 62, 7, 8, 9]
sorted_list = sorted(list1)
print(sorted_list)
print(waiting_list.sort(reverse=True))