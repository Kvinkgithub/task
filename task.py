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