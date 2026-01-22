list1=[]
a=1
user_count=int(input("Введите кол-во чисел:  "))
while a==1:
    if user_count > 1000:
        print("нужно кол-во чисел не больше 1000!")
        break
    for i in range(1,user_count+1):
        user_number = (input(f"Введите {i} число (надо минимум 1 число оконч. на 4):  "))
        if int(user_number) > 30000:
            print("Нельзя писать числа больше 30000!")
            break
        if int(user_number) % 10 == 4:
            list1.append(user_number)
    sort_list1=sorted(list1)
    print(f'Минимальное число оканчивающиеся на 4 это: {sort_list1[:1]}')

    a-=1

#Задача 2

# per=()
# user_str = input('Введите массив из 11 элементов: ')
# if len(user_str)==11:
#         for i in user_str:
#             if i.isalpha():
#                 per=i.upper()
#             else:
#                 per+=i
#                 print(per,end="")
#         else:
#             print("Некорректное число символов!")

#задача 3

# per=""
# user_str = input('Введите массив из 12 элементов: ')
# if len(user_str)==12:
#     for i in user_str:
#         if i.isdigit():
#              i="!"
#              print(i,end="")
#         else:
#             print(i,end="")

#задача 9

# count=0
# text=['book','bro','text','just']
# for i in text:
#     if i[:1]=='b':
#        count+=1
# print(f'Кол-во слов начинающихся с буквы {count}')

#задача 10

# count=0
# mass=['r','k','t','z']
# for i in mass:
#     if i == 'r' or i == 'k' or i == 't':
#         count+=1
# print(f'В массиве количество букв r,k,t: {count}')

#задача 11

# count=0
# mass=["42",'@','*',';',':']
# for i in mass:
#     if i == "*" or i == ":" or i == ';':
#         count+=1
# print(f'В массиве количество символов : , ; , * : {count}')
