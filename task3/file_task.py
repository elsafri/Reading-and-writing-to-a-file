with open('1.txt', encoding='UTF8') as file1:
    text1 = file1.readlines()
    list_of_count = [len(text1)]
with open('1.txt', encoding='UTF8') as file1:
    data1 = file1.read()
with open('2.txt', encoding='UTF8') as file2:
    text2 = file2.readlines()
    list_of_count.append(len(text2))
with open('2.txt', encoding='UTF8') as file2:
    data2 = file2.read()
with open('3.txt', encoding='UTF8') as file3:
    text3 = file3.readlines()
    list_of_count.append(len(text3))
with open('3.txt', encoding='UTF8') as file3:
    data3 = file3.read()
max_count = mid_count = min_count = 0
max_count = max(list_of_count)
min_count = min(list_of_count)
for element in list_of_count:
    if element != max_count:
        if element != min_count:
            mid_count = element
with open('result.txt', 'w', encoding='UTF8') as file4:
    if len(text1) == max_count:
        file4.write(f'Имя файла: 1.txt\nКоличество строк:{max_count}\n{data1}\n')
    elif len(text2) == max_count:
        file4.write(f'Имя файла: 2.txt\nКоличество строк:{max_count}\n{data2}\n')
    elif len(text3) == max_count:
        file4.write(f'Имя файла: 3.txt\nКоличество строк:{max_count}\n{data3}\n')
with open('result.txt', 'a', encoding='UTF8') as file4:
    if len(text1) == mid_count:
        file4.write(f'Имя файла: 1.txt\nКоличество строк:{mid_count}\n{data1}\n')
    elif len(text2) == mid_count:
        file4.write(f'Имя файла: 2.txt\nКоличество строк:{mid_count}\n{data2}\n')
    elif len(text3) == mid_count:
        file4.write(f'Имя файла: 3.txt\nКоличество строк:{mid_count}\n{data3}\n')
    if len(text1) == min_count:
        file4.write(f'Имя файла: 1.txt\nКоличество строк:{min_count}\n{data1}')
    elif len(text2) == min_count:
        file4.write(f'Имя файла: 2.txt\nКоличество строк:{min_count}\n{data2}')
    elif len(text3) == min_count:
        file4.write(f'Имя файла: 3.txt\nКоличество строк:{min_count}\n{data3}')





