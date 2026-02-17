class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Для +=
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    # Для ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Для if point:
    def __bool__(self):
        return self.x != 0 or self.y != 0
    
    def __str__(self):
        return f"({self.x}, {self.y})"


points = [Point(1,2), Point(3,4), Point(5,6)]

# Сумма
total = Point(0,0)
for i in points:
    total += i
print(f"Сумма: {total}") 

# Сравнение
p1 = Point(2,3)
p2 = Point(2,3)
p3 = Point(4,5)

print(f"p1 == p2: {p1 == p2}")  # True
print(f"p1 == p3: {p1 == p3}")  # False

# Проверка на ноль
zero = Point(0,0)
not_zero = Point(1,0)

print(f"zero: {bool(zero)}")      # False
print(f"not_zero: {bool(not_zero)}")  # True




# list1=[]
# a=1
# user_count=int(input("Введите кол-во чисел:  "))
# while a==1:
#     if user_count > 1000:
#         print("нужно кол-во чисел не больше 1000!")
#         break
#     for i in range(1,user_count+1):
#         user_number = (input(f"Введите {i} число (надо минимум 1 число оконч. на 4):  "))
#         if int(user_number) > 30000:
#             print("Нельзя писать числа больше 30000!")
#             break
#         if int(user_number) % 10 == 4:
#             list1.append(user_number)
#     sort_list1=sorted(list1)
#     print(f'Минимальное число оканчивающиеся на 4 это: {sort_list1[:1]}')
#     a-=1

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

import  random
class Warrior:
    def __init__(self, name_warrior, health, location, item):
        self.name_warrior = name_warrior
        self.health = health  # 100
        self.location = location
        self.item = item

    def get_damage(self, damage):
        """Получение урона"""
        self.health -= damage
        print(f'{self.name_warrior} получает {damage} урона. Осталось здоровья: {self.health}')

    def use_item(self):
        global heal_used
        global otkup_used
        if self.item == 'Зелье здоровья' and not heal_used:
            for i in range(1):
                if self.health <= 90:
                    self.health += 10
                    heal_used = True
                    print('Вы использовали зелье и восстановили 10 HP')
        if self.item == 'Горсть монет' and not otkup_used:
            item_choice = input('Хочешь откупиться от удара в этом ходу? y/n : ')
            if item_choice == 'y':
                global otkup_available
                otkup_available = True
                otkup_used = True
                print('Вы откупились от удара!')

White_warrior = Warrior('ВОИН Света', 100, 'Светлая сторона', 'none')
Dark_warrior = Warrior('ВОИН Тьмы', 100, 'Тёмная сторона', 'none')

game_over1 = False
otkup_available = False
otkup_used = False
heal_used = False

def attaka_White():
    global game_over1
    White_warrior.use_item()
    a = random.randint(6, 10)
    if a >= Dark_warrior.health:
        print(f'{Dark_warrior.name_warrior} вмэр')
        game_over1 = True
        return
    Dark_warrior.get_damage(a)

def attaka_Dark():
    global game_over1
    global otkup_available
    if otkup_available:
        print("Вас не ударили из-за откупа!")
        otkup_available = False
        return
    a = random.randint(6, 10)
    if a >= White_warrior.health:
        print(f'{White_warrior.name_warrior} вмэр')
        game_over1 = True
        return
    White_warrior.get_damage(a)

def menu():
    global White_warrior
    print('Магаз')
    print('1-Щит(30% шанс отразить удар) \n2-Зелье востоновления здоровья(Востонавливает 10хп)\n3-Кубик D20(Если выпадет число больше 10,врагу наносится 10 урона,если же меньше 10 то наносится тебе\n4-Горсть монет(Воин может откупится от 1 атаки)')
    user_choice = int(input('Введите число желаемого предмета: '))
    if user_choice == 1:
        White_warrior = Warrior('ВОИН Света', 100, 'Светлая сторона', 'Щит')
        print('Вы взяли Щит')
    if user_choice == 2:
        White_warrior = Warrior('ВОИН Света', 100, 'Светлая сторона', 'Зелье здоровья')
        print('Вы взяли Зелье здоровья')
    if user_choice == 3:
        White_warrior = Warrior('ВОИН Света', 100, 'Светлая сторона', 'Кубик D20')
        print('Вы взяли Кубик D20')
    if user_choice == 4:
        White_warrior = Warrior('ВОИН Света', 100, 'Светлая сторона', 'Горсть монет')
        print('Вы взяли Горсть монет')

print('GAME COOL\nВы играете за светлую сторону\n')
menu()
while not game_over1:
    attaka_White()
    if game_over1:
        break

    attaka_Dark()
    if game_over1:

        break


text = '"Не верю77! ск431аза7л" - К. Стани57славский'
summa = 0
text_no_digits = ""

# Считаем цифры и убираем их
for simvol in text:
    if simvol.isdigit():
        summa += int(simvol)
    else:
        text_no_digits += simvol

# Делаем текст в кавычках заглавными
result = ""
in_quotes = False  # начинаем снаружи кавычек

for simvol in text_no_digits:
    if simvol == '"':
        # Проверяем,где мы сейчас
        if in_quotes == True:  # если уже внутри кавычек
            in_quotes = False  # выходим
        else:  # если снаружи кавычек
            in_quotes = True  # входим
        result += simvol  # добавляем кавычку

    # Если мы внутри кавычек
    elif in_quotes == True:
        if simvol.isalpha():
            result += simvol.upper()
        else:
            result += simvol  # иначе оставляем как есть

    # Если снаружи кавычек
    else:
        result += simvol

# Результат
print(result)
print(f"\nСумма всех цифр: {summa}")

