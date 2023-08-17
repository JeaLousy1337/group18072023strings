"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку
здійснюється за механізмом
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення,
    бал від 0 до 100 (інт чи флоат)
2 - стuворити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to yo
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
# ваш код нижче !!!!!!!! вище нічого не змінюємо
from pprint import pprint
from decimal import Decimal

students['Мартін Рабов'] = {
    'Пошта': 'Martin@gmail.com',
    'Вік': 15,
    'Номер телефону': '+380970079188',
    'Середній бал': 70.6
}

key, value, *other = students
total_score = 0
list_of_students = []

for key, value in students.items():
    if students[key]['Середній бал'] > 90:
        list_of_students = key, students[key]['Середній бал']
        print(list(list_of_students))
    total_score += students[key]['Середній бал']

for key in students:
    if not students[key]['Номер телефону']:
        students[key]['Номер телефону'] = '+380991848808'
        # print(key, students[key]['Номер телефону'], '- це номер телефону батьків, так як учень не записав свій.')

if students:
    final_score = Decimal(total_score / len(students)).quantize(Decimal('0.01'))
    print('Середній бал групи', final_score)

pprint(students)
