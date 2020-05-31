#!/usr/bin/env python3

# ---------------------------------------------------------
# PROJECT:  Russian cities quiz
# AUTHOR:   Sergei Voron <mrsergeyvoron@gmail.com>
# UPDATE:   01 Jun 2020
# REVISION: v0.1
# ---------------------------------------------------------

import random

regions_cities_dict = {
'Амурская область' : 'Благовещенск',
'Архангельская область' : 'Архангельск',
'Астраханская область' : 'Астрахань',
'Белгородская область' : 'Белгород',
'Брянская область' : 'Брянск',
'Владимирская область' : 'Владимир',
'Волгоградская область' : 'Волгоград',
'Вологодская область' : 'Вологда',
'Воронежская область' : 'Воронеж',
'Ивановская область' : 'Иваново',
'Иркутская область' : 'Иркутск',
'Калининградская область' : 'Калининград',
'Калужская область' : 'Калуга',
'Кемеровская область' : 'Кемерово',
'Кировская область' : 'Киров',
'Костромская область' : 'Кострома',
'Курганская область' : 'Курган',
'Курская область' : 'Курск',
'Ленинградская область' : 'Санкт-Петербург',
'Липецкая область' : 'Липецк',
'Магаданская область' : 'Магадан',
'Московская область' : 'Москва',
'Мурманская область' : 'Мурманск',
'Нижегородская область' : 'Нижний Новгород',
'Новгородская область' : 'Новгород',
'Новосибирская область' : 'Новосибирск',
'Омская область' : 'Омск',
'Оренбургская область' : 'Оренбург',
'Орловская область' : 'Орел',
'Пензенская область' : 'Пенза',
'Псковская область' : 'Псков',
'Ростовская область' : 'Ростов-на-Дону',
'Рязанская область' : 'Рязань',
'Самарская область' : 'Самара',
'Саратовская область' : 'Саратов',
'Сахалинская область' : 'Южно-Сахалинск',
'Свердловская область' : 'Екатеринбург',
'Смоленская область' : 'Смоленск',
'Тамбовская область' : 'Тамбов',
'Тверская область' : 'Тверь',
'Томская область' : 'Томск',
'Тульская область' : 'Тула',
'Тюменская область' : 'Тюмень',
'Ульяновская область' : 'Ульяновск',
'Челябинская область' : 'Челябинск',
'Ярославская область' : 'Ярославль',
'Еврейская автономная область' : 'Биробиджан'
}



def rcq():
    regions = list(regions_cities_dict.keys())
    for i in [1, 2, 3, 4, 5]:
        region = random.choice(regions)
        city = regions_cities_dict[region]
        city_guess = input("Какая столица субъекта федерации " + region + "? ")

        if city_guess == city:
            print("Правильно!!!")
        else:
            print("Не правильно (. Столица " + region + " город " + city )

    print("Игра закончена!!!")


if __name__ == '__main__':
    rcq()