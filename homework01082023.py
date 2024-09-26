from pywebio.input import input as pw_input
from pywebio.output import put_success, put_warning, toast

favorite_animal = str(pw_input('Enter your favorite animal', required=True)).strip(" '()").lower()
animal_name = str(pw_input(f'Enter the name of your {favorite_animal}', required=True)).strip(" '()1").title()

cat_unicode = '\U0001F408'
dog_unicode = '\U0001F436'
fish_unicode = '\U0001F41F'
hamster_unicode = '\U0001F439'
turtle_unicode = '\U0001F422'
misunderstanding_unicode = '\U0001F937'

can_pet_swim = False

if favorite_animal == 'turtle' or favorite_animal == 'fish':
    can_pet_swim = True

if can_pet_swim:
    put_success('We have to buy aquarium')

if favorite_animal == 'dog':
    put_success(f"I'm afraid when the dog barks {dog_unicode}")
elif favorite_animal == 'cat':
    put_success(f"Cats love to catch mice {cat_unicode}")
elif favorite_animal == 'hamster':
    put_success(f'Hamsters are small but they stuff their cheeks with food {hamster_unicode}')
elif favorite_animal == 'turtle':
    put_success(f'The turtle has a strong shell {turtle_unicode}')
elif favorite_animal == 'fish':
    put_success(f"Fish can't be fried {fish_unicode}")
else:
    put_warning(f"I don't know such an animal \n {misunderstanding_unicode * 3}")
    toast("TRY AGAIN")
