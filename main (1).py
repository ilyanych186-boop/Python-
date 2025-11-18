'''
Задание 1
'''
lists = [1,'Привет', False, 3.14]
lists.append('мир')
lists.insert(0,67)
list2 = [2,'World', True]
lists.append(list2)
lists.insert(-1, (12,5))
print(lists[1])
lists.pop(5)
count = lists.count(1)
"""
Задание 2
"""
dict1 = {'name' : 'Ilya', 67 : 'age', 'counter': 'Russia'}
dict1['rost'] = 176
dict1[(98,56,82)] = [1,3,52]
print(dict1['rost'])
del dict1[67]
print('словарь', list(dict1.keys()))
'''
задание 3
'''
l = [1,56,3254,4,7,6,5,89,12,139,76,77]
for i in l:
    if i == 139:
        break
    if i % 2 != 0:
        print(i)
'''
Задание 4
'''
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
count_lst = 0
for num in lst:
    if num < 30 and num % 3 == 0:
        print(num)
    else:
        count_lst += num

print('Это числа, которые меньше 30 и делятся на 3 без остатка:',num)
print('Это число которые не соответствовали требованием и они суммировались:',count_lst)
'''
Задание 5
'''
def month_to_season(month):
    seasons = {1:'зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'весна', 6:'лето', 7:'Лето', 8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень', 12:'Зима'}
    if month in seasons:
        return seasons[month]
    else:
        return 'Нету такого номера месяца'

print(month_to_season(14))


