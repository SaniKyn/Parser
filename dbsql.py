from models import *
import json


# with db:
#     db.create_tables([Muscle, Exercise])

# all_save_datas - функция сохраняет значения с JSON
def all_save_datas(data):
    count = 1
    for name_muscle, val_exc in data.items():
        Muscle.create(name=name_muscle)
        for j in val_exc:
            for k, p in j.items():
                Exercise.create(name=k, info_how=p['how_to_do_it'], level=p['level'], expense_id=count)
        count += 1


# add_muscle - функция добавляет в таблицу Exercise упражнения
def add_exercise(name, info_how, level, name_mus="nothing"):
    mus_exist = True
    try:
        cat_mus = Muscle.select().where(Muscle.name == name_mus.capitalize().strip()).get()
    except DoesNotExist as de:
        mus_exist = False
    if mus_exist:
        Exercise.create(name=name,
                        info_how=info_how,
                        level=level,
                        expense_id=cat_mus)


# add_muscle - функция добавляет в таблицу Muscle группу мышцы
def add_muscle(name='nothing'):
    Muscle.create(name=name.capitalize().strip())


# del_exercisee - это функция удаляет из таблицы Exercise упражнения
def del_exercise(name='nothing'):
    Exercise.get(Exercise.name == name).delete_instance()


# del_muscle- функция удаляет из таблицы Muscle упражнения
def del_muscle(name='nothing'):
    Exercise.get(Muscle.name == name).delete_instance()


choise = input(
    'Что вы хотите сделать? '
    '(Добавить всё с JSON, добавить новое упражнения, добавить новое гурппу мышц, удалить упражнения или удалить '
    'группу мышцы): ').lower()
if choise == 'добавить всё с JSON'.lower():
    with open('new_json.json', 'r') as file:
        file_json = json.load(file)
    all_save_datas(file_json)
elif choise == 'добавить новое упражнения':
    name_exec = input('Введите название упражнения: ')
    info_how_exec = input('Введите как делать упражнения: ')
    level_exec = input('Введите уровень сложности упражнения(Beginner, Intermediate, Expert): ')
    name_mus_exec = input('Введите обязательно группу мышцы для упражнения: ')
    add_exercise(name_exec, info_how_exec, level_exec, name_mus=name_mus_exec)
elif choise == 'добавить новое гурппу мышц':
    add_mus = input('Введите обязательно группу мышцы: ')
    add_muscle(add_mus)
elif choise == 'удалить упражнения':
    del_name_exec = input('Введите название упражнения: ')
    del_exercise(del_name_exec)
elif choise == 'удалить группу мышцы':
    del_name_mus = input('Введите группу мышцы: ')
    del_muscle(del_name_mus)


# Road Cycling