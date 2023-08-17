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
    'Середній бал': 86.6
}

total_score = 0

for key, value in students.items():
    if 18 <= students[key]['Вік'] <= 40:
        print(key + ', найстарша людина групи', value)
    elif students[key]['Середній бал'] >= 90:
        print(key + ', в цієї людини найвищий бал у групі', value)
    elif not students[key]['Номер телефону']:
        students[key]['Номер телефону'] = '0991848808'
        print(key, students[key]['Номер телефону'], '- це номер телефону батьків, так як учень не записав свій.')
    total_score += students[key]['Середній бал']

final_score = Decimal(total_score / len(students)).quantize(Decimal('0.01'))

if students:
    print('Середній бал групи', final_score)

'Список всієї групи, з данними студентів'

pprint(students)
