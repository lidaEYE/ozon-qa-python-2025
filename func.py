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

gender = 'male'
job = 'yes'

if response.status_code == 200:
    heroes = response.json()
    print(f"Всего героев: {len(heroes)}")
else:
    print("Ошибка:", response.status_code)

filtered_heroes = []
for hero in heroes:
    if hero["appearance"]["gender"].lower() != gender.lower():
        continue
    
    occupation = hero["work"]["occupation"].lower()

    if occupation in ["-", "none", "unemployed", ""]:
        employment_status = "no"
    else:
        employment_status = "yes"

    if employment_status != job:
        continue
    
    height_data = hero["appearance"]["height"]
    if isinstance(height_data, list) and len(height_data) >= 2:
        height_str = height_data[1]
        
        if "cm" in height_str:
            height_cm = float(height_str.replace("cm", "").strip())
        elif "meters" in height_str:
            height_cm = float(height_str.replace("meters", "").strip()) * 100
        else:
            continue
        filtered_heroes.append((height_cm, hero))


# проверка наличия работы
# обработка роста (если cm, то просто удаление cm, если meters, то перевод в cm и удаление ед.изм.)
# перебор по росту в новую переменную (тоже цикл)

# вывод результата


occupations = set()
    
for hero in heroes:
    occupation = hero["work"]["occupation"]
        
        # Пропускаем пустые значения
    if not occupation or occupation == "-":
            continue
            
        # Разделяем строку по запятым/точкам с запятой
    for job in occupation.split(", "):
        for sub_job in job.split("; "):
            if sub_job.strip():
                occupations.add(sub_job.strip())
    
    

# Собираем единицы измерения из второго элемента массива height
units = []
for hero in heroes:
    height_data = hero["appearance"]["height"]
    if isinstance(height_data, list) and len(height_data) >= 2:
        metric_height = height_data[1]  # Берём второй элемент (например, "188 cm")
        unit = metric_height.strip()[-2:].lower()  # Последние 2 символа
        units.append(unit)

        if unit == 'kg':
            print(hero)
# метры необходимо перевести в см


# Подсчитываем и выводим результат
units_count = Counter(units)
print("Статистика единиц измерения роста (метрическая система):")
for unit, count in units_count.most_common():
    print(f"{unit} - {count}")


