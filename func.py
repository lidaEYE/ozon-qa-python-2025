import requests
from collections import Counter

'''план
1. принимаем пол
2. принимаем работу
3. отсеиваем по работе
4. отсеиваем самого высокого
5. далее возвращаем самого высокого'''

url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)

gender = 'female'
job = 'yes'

if response.status_code == 200:
    heroes = response.json()
    print(f"Всего героев: {len(heroes)}")
else:
    print("Ошибка:", response.status_code)

height = 0
result_hero = 'a'

for hero in heroes:
    if hero["appearance"]["gender"].lower() != gender.lower():
        continue
    
    occupation = hero["work"]["occupation"].lower()

    if occupation in ["-", "none", "unemployed", ""]:
        employment_status = 'no'
    else:
        employment_status = 'yes'

    if employment_status != job:
        continue
    
    height_data = hero["appearance"]["height"]
    if isinstance(height_data, list) and len(height_data) >= 2:
        height_str = height_data[1]
        
        if "cm" in height_str:
            height_cm = float(height_str.replace("cm", "").strip())
            if height_cm > height:
                height = height_cm
                result_hero = hero
                continue 
        elif "meters" in height_str:
            height_cm = float(height_str.replace("meters", "").strip()) * 100
            if height_cm > height:
                height = height_cm
                result_hero = hero
                continue
        else:
            continue
print(f'конечный герой {result_hero}')


# проверка наличия работы
# обработка роста (если cm, то просто удаление cm, если meters, то перевод в cm и удаление ед.изм.)
# перебор по росту в новую переменную (тоже цикл)

# вывод результата



    
    




