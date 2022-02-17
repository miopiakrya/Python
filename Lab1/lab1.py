#1
#Напишите скрипт, который преобразует введенное с клавиатуры вещественное число в денежный формат. Например, число 12,5 должно
#быть преобразовано к виду «12 руб. 50 коп.». В случае ввода отрицательного числа выдайте сообщение «Некорректный формат!»
#путем обработки исключения в коде.

num = float(input())

if num < 0:
    print("Некорректный формат!")
else:
    print("%d руб. %d копеек" % (num, (num - int(num)) * 100))
    
#2
#Написать скрипт, который выводит на экран «True», если элементы программно задаваемого списка представляют собой возрастающую
#последовательность, иначе – «False».

num = [1, 2, 3, 4]
checker = 0

for i in range(len(num) - 1):
    if (num[i] > num[i + 1]):
        checker = 1

if (checker == 1):
    print("False")
else:
    print("True")

#3
#Напишите скрипт, который позволяет ввести с клавиатуры номер дебетовой карты (16 цифр) и выводит номер в скрытом виде: первые и
#последние 4 цифры отображены нормально, а между ними – символы «*» (например, 5123 **** **** 1212).
 
num = input()

if (len(num) != 16):
    print("Введена не дебетовая карточка!")
else:
    num = num[:4] + " **** **** " + num[12:]
        
print(num)

#4
#Напишите скрипт, который разделяет введенный с клавиатуры текст на слова и выводит сначала те слова, длина которых превосходит 7
#символов, затем слова размером от 4 до 7 символов, затем – все остальные.

num = input()

wordLen = 0
word = ""

print ("\nСлова с 7 или более буквами: ")
for i in range(len(num)):
    word += num[i]
    wordLen += 1
    if (num[i] == " " or i == len(num) - 1):
        if (wordLen >= 7):
            print(word, wordLen)
        
        word = ""
        wordLen = 0
        
        
print ("\nСлова от 4 до 7 букв: ")
for i in range(len(num)):
    word += num[i]
    wordLen += 1
    if (num[i] == " " or i == len(num) - 1):
        if (wordLen >= 4 and wordLen < 7):
            print(word, wordLen)
        
        word = ""
        wordLen = 0
        
        
print ("\nСлова менее 4 букв: ")
for i in range(len(num)):
    word += num[i]
    wordLen += 1
    if (num[i] == " " or i == len(num) - 1):
        if (wordLen < 4):
            print(word, wordLen)
        
        word = ""
        wordLen = 0

#5
#Напишите скрипт, который позволяет ввести с клавиатуры текст предложения и сформировать новую строку на основе исходной, в
#которой все слова, начинающиеся с большой буквы, приведены к верхнему регистру. Слова могут разделяться запятыми или пробелами.
#Например, если пользователь введет строку «город Донецк, река Кальмиус», результирующая строка должна выглядеть так: «город
#ДОНЕЦК, река КАЛЬМИУС».

num = input()
out = ""

checker = 0

print ("\n")

for i in range(len(num)):
    if (num[i].isupper()):
        if (num[i - 1] == " " or num[i - 1] == ","):
            checker = 1
    
    if (checker == 1):
        out += num[i].upper()
        
        if (num[i] == " "):
            checker = 0
    else:
        out += num[i]

print (out)

#6
#Напишите программу, позволяющую ввести с клавиатуры текст предложения и вывести на консоль все символы, которые входят в этот
#текст ровно по одному разу.

num = input()
out = ""

checker = 0

for i in range(len(num)):
    for j in range(len(out)):
        if (out[j] == num[i]):
            checker = 1
            
    if (checker == 0):
        out += num[i]
    
    checker = 0

print (out)

#7
#Напишите скрипт, который обрабатывает список строк-адресов следующим образом: сначала определяет, начинается ли каждая строка
#в списке с префикса «www». Если условие выполняется, то скрипт должен вставить в начало этой строки префикс «http://», а затем
#проверить, что строка заканчивается на «.com». Если у строки другое окончание, то скрипт должен вставить в конец подстроку «.com». В
#итоге скрипт должен вывести на консоль новый список с измененными адресами. Используйте генераторы списков.

list = ["myname","www.myname","www.myname.com","myname.com"]

output_list = [i + ".com" if not i.endswith('.com') else i for i in ["http://" + i if i.startswith('www.') else i for i in list]]
print("\n".join(output_list))

#8
#Напишите скрипт, генерирующий случайным образом число n в диапазоне от 1 до 10000. Скрипт должен создать массив из n целых
#чисел, также сгенерированных случайным образом, и дополнить массив нулями до размера, равного ближайшей сверху степени двойки.
#Например, если в массиве было n=100 элементов, то массив нужно дополнить 28 нулями, чтобы в итоге был массив из 28 = 128 элементов
#(ближайшая степень двойки к 100 – это число 128, к 35 – это 64 и т.д.).

import random

n = int(random.random() * 10000)
saveNumb = n

digit = 2

while digit < n:
    digit *= 2
    
out = [0] * digit

for i in range(n):
    out[i] = int(random.random() * 100)
    
while n != digit:
    out[n] = 0
    n += 1

print("Выпавшее число: %d\nБлижайшая степень двойки: %d\nРазмер массива: %d" % (saveNumb, digit, len(out)))

#9
#Напишите программу, имитирующую работу банкомата. Выберите структуру данных для хранения купюр разного достоинства в заданном
#количестве. При вводе пользователем запрашиваемой суммы денег, скрипт должен вывести на консоль количество купюр подходящего
#достоинства. Если имеющихся денег не хватает, то необходимо напечатать сообщение «Операция не может быть выполнена!».
#Например, при сумме 5370 рублей на консоль должно быть выведено «5*1000 + 3*100 + 1*50 + 2*10».

bank = [10, 10, 10, 10]

numb = int(input())
saveNumb = numb

while numb != 0:
    if (numb - 1000 >= 0 and bank[0] > 0):
        bank[0] -= 1
        numb -= 1000
    elif (numb - 100 >= 0 and bank[1] > 0):
        bank[1] -= 1
        numb -= 100
    elif (numb - 50 >= 0 and bank[2] > 0):
        bank[2] -= 1
        numb -= 50
    elif (numb - 10 >= 0 and bank[3] > 0):
        bank[3] -= 1
        numb -= 10
    else:
        print ("Банк не может выдать Вам такую сумму.")
        break;

if (numb == 0):    
    print ("%d = %d * 1000 + %d * 100 + %d * 50 + %d * 10" % (saveNumb, 10 - bank[0], 10 - bank[1], 10 - bank[2], 10 - bank[3]))

#10
#Напишите скрипт, позволяющий определить надежность вводимого пользователем пароля. Это задание является творческим: алгоритм
#определения надежности разработайте самостоятельно.

password = input()

digitCheck = 0
alphaCheck = 0
upperCheck = 0
lowerCheck = 0
duplicateCheck = 0

for i in range(len(password)):
    if (password[i].isdigit()):
        digitCheck = 1
    if (password[i].isalpha()):
        alphaCheck = 1
    if (password[i].isupper()):
        upperCheck = 1
    if (password[i].islower()):
        lowerCheck = 1
    
if (digitCheck == 0):
    print("Вы не добавили цифры в пароль.")

if (alphaCheck == 0):
    print("Вы не добавили буквы в пароль.")
    
if (upperCheck == 0 and alphaCheck == 1):
    print("У вас нет букв из верхнего регистра.")
    
if (lowerCheck == 0 and alphaCheck == 1):
    print("У вас нет букв из нижнего регистра.")

#11
#Напишите генератор frange как аналог range() с дробным шагом.

def frange(a, b, c):
    while a < b:
        yield a
        a += c

for x in frange(1, 5, 0.1):
    print(x)

#12
#Напишите генератор get_frames(), который производит «оконную декомпозицию» сигнала: на основе входного списка генерирует набор
#списков – перекрывающихся отдельных фрагментов сигнала размера size со степенью перекрытия overlap. 

def get_frames(signal, size, overlap):
    for i in range(size):
        yield signal
        
        signal += overlap    

for frame in get_frames(1, 1024, 0.5):
    print(frame)

#13
#Напишите собственную версию генератора enumerate под названием extra_enumerate. В переменной cum хранится накопленная сумма на момент текущей
#итерации, в переменной frac – доля накопленной суммы от общей суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
#вывод будет таким: (1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1).

def extra_enumerate(x):
    sum = 0
    totalSum = 0
    
    for i in range(len(x)):
        totalSum += x[i]
        
    for i in range(len(x)):
        sum += x[i]
        frac = sum / totalSum
        
        yield x[i], sum, frac
        
x = [1, 3, 4, 2]

for elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)

#14
#Напишите декоратор non_empty, который дополнительно проверяет списковый результат любой функции: если в нем содержатся пустые
#строки или значение None, то они удаляются. Пример кода:
#@non_empty
#def get_pages():
 #return ['chapter1', '', 'contents', '', 'line1'].

def non_empty(func):
    
    def some():
        
        thisStr = func()
        someStr = []
    
        for i in range(len(thisStr)):
            if (thisStr[i]):    
                someStr.append(thisStr[i])
        
        return someStr
            
    return some
   
@non_empty
def get_pages():
    return ["chapter1", "", "contents", "", "line1"]
    
num = get_pages()

print(num)

#15
#Напишите параметризированный декоратор pre_process, который осуществляет предварительную обработку (цифровую фильтрацию)
#списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в коде (по умолчанию равен 0.97).

def non_empty(a = 0.97):
    def something(func):
        def some(s):
        
            thisStr = s
    
            for i in range(len(thisStr)):
                thisStr[i] = thisStr[i] - a * thisStr[i - 1] 
        
            func(s)
        
            return thisStr
            
        return some
    
    return something
   
@non_empty(a = 0.93)
def plot_signal(s):
    for sample in s:
        print(sample)
    
s = [1, 2, 3, 4, 5]

plot_signal(s)

#16
#Напишите скрипт, который на основе списка из 16 названий футбольных команд случайным образом формирует 4 группы по 4
#команды, а также выводит на консоль календарь всех игр (игры должны проходить по средам, раз в 2 недели, начиная с 15 сентября
#текущего года). Даты игр необходимо выводить в формате «15/09/2021, 22:45».

import random
import datetime

teams = ["A", "B", "C", "D", "E", "F", "G", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]

random.shuffle(teams)
dates = datetime.datetime(2022, 9, 15, 13, 30)
groups = []
    
for i in range(4):
    groups.append(teams[i*4:i*4+4])
        
print("Группы:")
    
for i in groups:
    print(i)

print("\nИгры:")
for i in teams:
    print(i, dates.strftime("%d/%m/%Y %H:%M"))
    dates += datetime.timedelta(days=14, hours=4)

