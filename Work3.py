#  Требуется вычислить, сколько раз встречается некоторое
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# from random import randint
# n=int(input('Введите длинну массива: '))
# a=[randint(1,10) for _ in range(n)]
# print(a)
# x=int(input("Введите число для поиска: "))
# counter=0
# for i in a :
#     if i==x:
#         counter+=1
# print(counter)        
# ******************************************************************************
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X   
# from random import randint 
# n=int(input('Введите длинну массива: '))
# a=[randint(1,10) for _ in range(n)]
# print(a)
# x=int(input("Введите число для самых близких значений: "))
# min=a[0]
# for i in range(n):
#     if(a[i]==x):
#         min=i
#     elif(x>a[i]):
#         if(min<a[i]):
#             min=a[i]
#     elif(x<a[i]):
#         if(min>a[i]):
#             min=a[i]        
# print(min)
    
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ●  – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ●  – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английQ, Zские, либо только русские буквы.        

# dit=dict()
# dit['1']="A",'E','I','O','U','L','N','S','T','R','А','В','Е','И','Н','О','Р','С','Т'
# dit['2']='D','G','Д','К','Л','М','П','У'
# dit['3']= 'B','C','M','P','Б','Г','Ё','Ь','Я'
# dit['4']='F','H','V','W','Y','Й','Ы'
# dit['5']='Ф','Щ','Ъ','K','Ж','З','Х','Ц','Ч'
# dit['8']='J','X','Ш','Э','Ю'
# dit['10']='Q','Z','Ф','Щ','Ъ'

# slovo=input("Введите слово: ")
# slovo=list(slovo.strip().upper())
# count=0
# for k,v in dit.items():
#     for i in slovo:
#         if(i in v):
#             count+=int(k)
# print(count)
            














