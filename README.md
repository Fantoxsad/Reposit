# Reposit
from colorama import Fore
import time
from turtle import clear
import math
from traceback import print_tb
from random import randrange
import os 
import ctypes
from turtle import goto
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

dy = 0
money = 0
sleepplus = 100
health = 100
hungry = 0
hunWat = 0
water = 0
food = 0
energy = 100
exp = 0
DayCounter = 0
console = 0
ToCount = 0
god = 0
PlayerLevel = 0
NeedExp = 100
TraderVisit = 0
Zapiska = 0

notes = []


def Trader():
    global TraderVisit, food, water,TraderChose
    # cls()
    TraderVisit += 1
    print("Торговец: Не думал что кто-то зайдёт")
    time.sleep(0.2)
    print("Торговец: Все товары на полках. Если захочешь что-то спросить то спрашивай.")
    time.sleep(0.2)
    print("---------------------------------------------")
    time.sleep(0.2)
    print("1 - Бутылка воды (15 ед. воды)")
    time.sleep(0.2)
    print("2 - Большой кусок мяса (25 ед. еды)")
    time.sleep(0.2)
    print("3 - Небольшой кусок мяса (10 ед. еды)")
    time.sleep(0.2)
    print("4 - Записка охотника #4")
    if Zapiska != 0:
        time.sleep(0.2)
        print("5 - Не знаешь чьи это записки")
    time.sleep(0.2)
    print("---------------------------------------------")
    TraderChose = input("Выбор: ")
    

def Trader01(TraderChose):
    # cls()
    if TraderChose == 1:
        print("Бутылка воды стоит 20 Шарнов")
        print("--------------------------------------------")




def Stroll():
    global exp, food, health, energy, RandStroll
    RandStroll = randrange(1, 7)

    exp += 10

    if RandStroll == 1:
        print("Голос во тьме: Ты набрёл на разбойников. Они тебя ограбили.")
        energy -= 30
        health -= 20
        if food <= 20:
            print("----------------------------------")
            time.sleep(0.2)
            print("  -  HP " + Fore.RED + "- 20", Fore.RESET)
            time.sleep(0.2)
            print("  -  Еда " + Fore.RED + "- Вся еда", Fore.RESET)
            time.sleep(0.2)
            print("  -  Энергия " + Fore.RED + "- 30", Fore.RESET)
            food -= 20
            if food <= 0:
                food = 0
        else:
            print("----------------------------------")
            time.sleep(0.2)
            print("  -  HP " + Fore.RED + "- 20", Fore.RESET)
            time.sleep(0.2)
            print("  -  Еда " + Fore.RED + "- 20", Fore.RESET)
            time.sleep(0.2)
            print("  -  Энергия " + Fore.RED + "- 30", Fore.RESET)
            food -= 20
        input()

    elif RandStroll == 3:
        print("Голос во тьме: Ты набрёл на разбойников. Но победил их.")
        energy -= 20
        food += 30
        print("----------------------------------")
        time.sleep(0.2)
        print("  -  Еда " + Fore.GREEN + "+ 30", Fore.RESET)
        time.sleep(0.2)
        print("  -  Энергия " + Fore.RED + "- 20", Fore.RESET)
        input()


    elif RandStroll == 5:
        print("Голос во тьме: Вскоре ты нашёл хижину охотника. Видимо владельца давно не было внутри.")
        print("Голос во тьме: Ты молча взял еды и пошёл обратно.")
        energy -= 20
        food += 50
        health += 15
        print("----------------------------------")
        time.sleep(0.2)
        print("  -  HP " + Fore.GREEN + "+ 15", Fore.RESET)
        time.sleep(0.2)
        print("  -  Еда " + Fore.GREEN + "+ 50", Fore.RESET)
        time.sleep(0.2)
        print("  -  Энергия " + Fore.RED + "- 20", Fore.RESET)
        input()

    elif RandStroll == 4 or RandStroll == 2:
        print("Голос во тьме: Всё прошло как обычно.")
        energy -= 20
        health += 15
        print("----------------------------------")
        time.sleep(0.2)
        print("  -  HP " + Fore.GREEN + "+ 15", Fore.RESET)
        time.sleep(0.2)
        print("  -  Энергия " + Fore.RED + "- 20", Fore.RESET)
        input()
    
    elif RandStroll == 6 or RandStroll == 7:
        print("Голос во тьме: Вскоре ты нашёл лавку торговца.")
        print("Голос во тьме: Войти?.")
        print("-----------------------------------------------")
        print("1 - Войти")
        print("2 - Не входить")
        StrollAction = input("Выбор:")
        if StrollAction == 1:
            print("Ты вошёл в магазин.")
            Trader()
    


def ReadingNotes():
    global nota
    cls()
    nota = 1   
    print("Ваши записки")
    while nota <= len(notes):

        print(nota, ")", notes[nota - 1] )
        nota += 1
        time.sleep(0.1)
    input()


def note():
    global exp
    exp += 5
    print("  - Что будешь писать?")
    otv = input("  - Ответ - ")
    notes.append(otv)
    print("  - Вы написали:", otv)
    input()


def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

def GameOver():
    cls()
    print("GAME OVER")
    input()
    exit(0)

def Win():
    cls()
    print("YOU WIN!")
    input()
    exit(0)

def Ifer():
    if energy <= 0:
        GameOver()
    if health <= 0:
        GameOver()
    if dy >= DayCounter:
        Win()
    if hunWat >= 100:
        GameOver()
    if hungry >= 100:
        GameOver()








def cls():
    os.system('CLS')


def Sleep():
    global exp, food, energy, health, dy
    if food <= 2:
        print("Недостаточно.")
        input()
        menu()
    health += 10
    exp += 10
    food -= 3
    dy += 0.5
    print("  -  Вы поспали.")
    time.sleep(0.5)
    print("  -  HP" + Fore.GREEN + " + 10", Fore.RESET)
    time.sleep(0.5)
    print("  -  Опыт" + Fore.GREEN + " + 10", Fore.RESET)
    time.sleep(0.5)
    print("  -  Еда" + Fore.RED + " - 3", Fore.RESET)
    time.sleep(0.5)
    if energy <= 100:
        print("  -  Энергия" + Fore.GREEN + " +", sleepplus - energy, Fore.RESET)
        energy = 100
    input()

def Arena():
    global exp, food, energy, health, e, f, en, he, wa, water, dy
    e = randrange(1, 20)
    f = randrange(-10, 25)
    en = randrange(-30, -5)
    he = randrange(-20, 0)
    wa = randrange(-30, 20)
    exp += e
    dy += 1
    print("  - Опыт" + Fore.GREEN + " +", e, Fore.RESET)
    if f < 0:
        time.sleep(0.5)
        food += f
        print("  - Еда" + Fore.RED + " -", f - f - f, Fore.RESET )
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        food += f
        print("  - Еда" + Fore.GREEN + " +", f, Fore.RESET )
        time.sleep(0.5)
    if wa < 0:
        water += wa
        print("  - Вода" + Fore.RED + " -", wa - wa - wa, Fore.RESET)
    else:
        water += wa
        print("  - Вода" + Fore.GREEN + " +", wa, Fore.RESET)

    if en < 0:
        energy += en
        print("  - Энергия" + Fore.RED + " -", en - en -en, Fore.RESET )
        time.sleep(0.5)
    if he < 0:
        health += he
        print("  - HP" + Fore.RED + " -", he - he - he, Fore.RESET )
        time.sleep(0.5)
    else:
        health += he
        print("  - HP" + Fore.GREEN + " +", he, Fore.RESET )
        time.sleep(0.5)
    input()

    

def hunt():
    global exp, food, energy, FoCol, dy
    if energy <= 29:
        print("Недостаточно.")
        input()
        menu()
    FoCol = randrange(10, 35)
    exp += 15
    food += FoCol
    energy -= 30
    dy += 1
    print()
    print()
    print()
    print("  -  Охота прошла успешно.")
    time.sleep(0.5)
    print("  -  Опыт " + Fore.GREEN + "+ 15", Fore.RESET)
    time.sleep(0.5)
    print("  -  Еда " + Fore.GREEN + "+", FoCol ,Fore.RESET)
    time.sleep(0.5)
    print("  -  Энергия " + Fore.RED + "- 30", Fore.RESET)
    input()

def watCol():
    global exp, food, energy, water, WaCol, dy
    if energy <= 14:
        print("Недостаточно.")
        input()
        menu()
    WaCol = randrange(15, 35)
    water += WaCol
    energy -= 15
    exp += 10
    dy += 1
    time.sleep(0.5)
    print("  -  Опыт " + Fore.GREEN + "+ 10", Fore.RESET)
    time.sleep(0.5)
    print("  -  Вода " + Fore.GREEN + "+", WaCol ,Fore.RESET)
    time.sleep(0.5)
    print("  -  Энергия " + Fore.RED + "- 15", Fore.RESET)
    input()

def ERROR():
    print(Fore.RED)
    while True:
        print("ERROR ERROR ERROR ERROR ERROR ERROR")
        print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
        print("ERROR ERROR ERROR ERROR ERROR ERROR")
        print("ERROR ERROR ERROR ERROR")
        print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
        print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
        print("ERROR")
        print("ERROR ERROR ERROR ERROR ERROR")
        print("ERROR")
        print("ERROR ERROR ERROR ERROR ERROR ERROR")
        print("ERROR ERROR ERROR")
        print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")

def fish():
    global exp, food, energy, water, dy
    if energy <= 14:
        print("Недостаточно.")
        input()
        menu()
    exp += 7
    food += 5
    energy -= 15
    dy += 0.5
    print()
    print()
    print()
    print("  -  Рыбалка прошла успешно.")
    time.sleep(0.5)
    print("  -  Опыт " + Fore.GREEN + "+ 7", Fore.RESET)
    time.sleep(0.5)
    print("  -  Еда " + Fore.GREEN + "+ 5", Fore.RESET)
    time.sleep(0.5)
    print("  -  Энергия " + Fore.RED + "- 15", Fore.RESET)
    input()

def snek():
    global exp, food, energy, health, hungry, HuRan, dy
    if food <= 29:
        print("Недостаточно.")
        input()
        menu()
    HuRan = randrange(15, 35)
    health += 15
    exp += 10
    food -= 30
    hungry -= HuRan
    energy += 30
    dy += 0.25
    print()
    print()
    print()
    print("  -  Вы поели.")
    time.sleep(0.5)
    print("  -  HP " + Fore.GREEN + "+ 15", Fore.RESET)
    time.sleep(0.5)
    print("  -  Опыт " + Fore.GREEN + "+ 10", Fore.RESET)
    time.sleep(0.5)
    print("  -  Голод " + Fore.GREEN + "-", HuRan ,Fore.RESET)
    time.sleep(0.5)
    print("  -  Еда " + Fore.RED + "- 30", Fore.RESET)
    time.sleep(0.5)
    print("  -  Энергия " + Fore.GREEN + "+ 30", Fore.RESET)
    input()

def wat():
    global exp, food, energy, health, water, hunWat, UnWat, dy
    if water < 15:
        print("Недостаточно.")
        input()
        menu()
    UnWat = randrange(20, 45)
    health += 15
    exp += 10
    water -= 15
    hunWat -= UnWat
    food -= 4
    energy += 30
    dy += 0.25
    print()
    print()
    print()
    print("  -  Вы попили.")
    time.sleep(0.5)
    print("  -  HP " + Fore.GREEN + "+ 15", Fore.RESET)
    time.sleep(0.5)
    print("  -  Опыт " + Fore.GREEN + "+ 10", Fore.RESET)
    time.sleep(0.5)
    print("  -  Еда " + Fore.RED + "- 4", Fore.RESET)
    time.sleep(0.5)
    print("  -  Вода " + Fore.RED + "- 15", Fore.RESET)
    time.sleep(0.5)
    print("  -  Жажда " + Fore.GREEN + "-", UnWat ,Fore.RESET)
    time.sleep(0.5)
    print("  -  Энергия " + Fore.GREEN + "+ 30", Fore.RESET)
    input()
        
def blo():
    global exp, energy, health, hunWat, dy
    health -= 20
    exp -= 15
    hunWat -= 25
    energy -= 40
    dy += 1
    print()
    print()
    print()
    print("  -  Это было больно.")
    time.sleep(0.5)
    print("  -  HP " + Fore.RED + "- 20", Fore.RESET)
    time.sleep(0.5)
    print("  -  Опыт " + Fore.RED + "- 15", Fore.RESET)
    time.sleep(0.5)
    print("  -  Жажда " + Fore.GREEN + "- 25", Fore.RESET)
    time.sleep(0.5)
    print("  -  Энергия " + Fore.RED + "- 40", Fore.RESET)
    input()

def CHEATS():
    print(Fore.RED)
    while True:
        print("НЕ ЧИТЕРИ")
        


def ERRORLIMITED():
    cls()
    print(Fore.RED)
    print("ERROR")
    print(Fore.RESET)
    input()


def GameConsole():
    cls()
    print(Fore.RESET)
    global food, water, hunWat, energy, health, hungry, exp, command, god, ToCount, PlayerLevel
    command = str(input("Print the command>>>"))
    if command == 'godmode':
        if god >= 1:
            god = 0
            print("GodMode OFF")
            input()
        elif god <= 0:
            god = 1
            print("GodMode ON")
            input()
    elif command == 'set water to':
        ToCount == int(input("Print count>>>"))
        water = ToCount
    elif command == 'set food to':
        ToCount == int(input("Print count>>>"))
        food = ToCount
    elif command == 'set energy to':
        ToCount == int(input("Print count>>>"))
        energy = ToCount
    elif command == 'set hungry to':
        ToCount == int(input("Print count>>>"))
        hungry = ToCount
    elif command == 'set hunWat to':
        ToCount == int(input("Print count>>>"))
        hunWat = ToCount
    elif command == 'set exp to':
        ToCount == int(input("Print count>>>"))
        exp = ToCount
    elif command == 'It just works':
        ERROR()
    elif command == 'Sv_Cheats 1':
        CHEATS()
    elif command == 'help':
        print("GodMode - Активирует режим бога. В нём ты можешь хоть жизни в -1000 увести. ВСЕ ОГРАНИЧЕНИЯ ОТКЛЮЧЕНЫ!!")
        print("set [Параметр] to - Позволяет поставить определённое число на определённый пораметр.")
        input()
    elif command == 'TqGandalfWhite':
        print("  -  Уровень " + Fore.YELLOW + "+ 1")
        PlayerLevel += 1
    else:
        ERRORLIMITED()





def menu():
    while True:
        global dy, health, food, energy, hunWat, hungry, water, UR, UT, console, god, exp, NeedExp, PlayerLevel, money
        if god == 0:
            Ifer()
        cls()
        if god == 0:
            health = clamp(health, 0, 100)
            food = clamp(food, 0, 100)
            energy = clamp(energy, 0, 150)
            water = clamp(water, 0, 100)
            UT = randrange(1, 20)
            UR = randrange(1, 15)
        print("День ", dy)
        if god == 0:
            hunWat += UT
            hungry += UR
            hunWat = clamp(hunWat, 0, 100)
            hungry = clamp(hungry, 0, 100)
            if exp >= NeedExp:
                exp = 0
                NeedExp += 50
                PlayerLevel += 1
                print("  -  Уровень " + Fore.YELLOW + "+ 1")
                print(Fore.RESET)
                input()
                goto
                
        print()
        time.sleep(0.1)
        print("Голод =", hungry,"%")
        time.sleep(0.1)
        print(Fore.CYAN + "Жажда =", hunWat,"%")
        time.sleep(0.1)
        print(Fore.RED + "hp =", health)
        time.sleep(0.1)
        print(Fore.GREEN + "Еда =", food)
        time.sleep(0.1)
        print(Fore.CYAN + "Вода =", water)
        time.sleep(0.1)
        print(Fore.LIGHTYELLOW_EX + "Монеты (Шарны) =", money)
        time.sleep(0.1)
        print(Fore.BLUE + "Энергия =", energy)
        time.sleep(0.1)
        print(Fore.YELLOW + "XP =", exp, Fore.RESET)
        time.sleep(0.1)
        print(Fore.YELLOW + "LEVEL =", PlayerLevel, Fore.RESET)
        print()
        # print(Fore.BLACK + 'BLACK')
        # print(Fore.BLUE + 'BLUE')
        # print(Fore.CYAN + 'CYAN')
        # print(Fore.GREEN + 'GREEN')
        # print(Fore.LIGHTBLACK_EX + 'LIGHTBLACK_EX')
        # print(Fore.LIGHTBLUE_EX + 'LIGHTBLUE_EX')
        # print(Fore.LIGHTCYAN_EX + 'LIGHTCYAN_EX')
        # print(Fore.LIGHTGREEN_EX + 'LIGHTGREEN_EX')
        # print(Fore.LIGHTMAGENTA_EX + 'LIGHTMAGENTA_EX')
        # print(Fore.LIGHTRED_EX + 'LIGHTRED_EX')
        # print(Fore.LIGHTWHITE_EX + 'LIGHTWHITE_EX')
        # print(Fore.LIGHTYELLOW_EX + 'LIGHTYELLOW_EX')
        # print(Fore.MAGENTA + 'MAGENTA')
        # print(Fore.RED + 'RED')
        # print(Fore.RESET + 'RESET')
        # print(Fore.WHITE + 'WHITE')
        # print(Fore.YELLOW + 'YELLOW')
        print()
        time.sleep(0.1)
        print("Куда едешь?")
        time.sleep(0.1)
        print("-----------------")
        time.sleep(0.1)
        print("1 - Охота")
        time.sleep(0.1)
        print("2 - Спать")
        time.sleep(0.1)
        print("3 - Рыбалка")
        time.sleep(0.1)
        print("4 - Перекус")
        time.sleep(0.1)
        print("5 - Собрать воду")
        time.sleep(0.1)
        print("6 - Битва на арене")
        time.sleep(0.1)
        print("7 - Пить")
        time.sleep(0.1)
        print("8 - Пить жидкую боль")
        time.sleep(0.1)
        print("9 - Написать записку")
        time.sleep(0.1)
        print("10 - Прочитать записки")
        time.sleep(0.1)
        print("11 - ИДИ ГУЛЯЙ!!!")
        time.sleep(0.1)
        if console == 1:
            print("12 - Консоль")
        print("-----------------")
        time.sleep(0.1)

        action = input("Вариант:")
        # action = int(action)

        if action == '1':
            hunt()
        elif action == '2':
            Sleep()
        elif action == '3':
            fish()
        elif action == '4':
            snek()
        elif action == '5':
            watCol()
        elif action == '6':
            Arena()
        elif action == '7':
            wat()
        elif action == '8':
            blo()
        elif action == '9':
            note()
        elif action == '10':
            ReadingNotes()
        elif action == '11':
            Stroll()
        elif action == '12' and console == 1:
            GameConsole()
        elif str(action) == 'console off':
            console = 0
        elif str(action) == 'console on':
            console = 1






print("=============================")
print("Добро пожаловать Тексто-земие")
print("--------Цель выживать--------")
print("=============================")
time.sleep(0.5)
print("1 = 10 дней")
time.sleep(0.5)
print("2 = 15 дней")
time.sleep(0.5)
print("3 = 20 дней")
time.sleep(0.5)
print("4 = 25 дней")
time.sleep(0.5)
print("5 = 30 дней")
time.sleep(0.5)
print("6 = Выход")
time.sleep(0.5)
print("------------------")
var = int(input("Выбор:"))

if var == 6:
    exit(0)
elif var == 1:
    DayCounter = 10
    menu()
elif var == 2:
    DayCounter = 15
    menu()
elif var == 3:
    DayCounter = 20
    menu()
elif var == 4:
    DayCounter = 25
    menu()
elif var == 5:
    DayCounter = 30
    menu()


