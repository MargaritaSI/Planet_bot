import re

town1 = ['Арзамасъ','Анапя','Москва'] # создать словари в отд файлах или как-то загрузить модуль с городами
town2 =[]

first_city =  'Арзамасъ'.strip()
first_city =  re.sub("[ъйыь]", "", first_city)
answer_city = 'Анапя' # тестовый пример

def next_city(answer_city): #

    for letters in first_city:
        if first_city[-1] == answer_city[1]:
            if first_city in town1 and first_city not in town2:
                town1.remove(first_city)
                town2.append(first_city)
    return 'call next city or print "end" if you want stop it'

while answer_city != 'end'.lower() or len(town1) != 0: #функция while  должна запускать города до прерывания
    next_city(answer_city)
    if answer_city == 'end'.lower() or len(town1) == 0:
        break






