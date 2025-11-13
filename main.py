name = input()
Willow = ['ё','у','е','ы','а','о','э','я','и','ю','Ё','У','Е','Ы','А','О','Э','И','Ю','Я']
print(len(name)) # считает кол-во символов
count = 0 # считает кол-во букв
for char in name:  
    if char.isalpha():  
        count += 1  
print(count) 
count1 = 0 # считает кол-во гласных
count2 = 0 # считает кол-во согласных
for i in name:
    if i in Willow:
        count1 += 1
    elif i.isalpha():
        count2 += 1

print(f'Гласных: {count1}')
print(f'Согласных: {count2}')


name2 = name.split() # считает кол-во слов
print(len(name2))

print(max(name.split(), key=len)) # ищет самое длинное слово