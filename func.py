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

        # Собираем все occupation

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
    
    # Возвращаем отсортированный список
#print(occupations)

# Собираем все единицы измерения роста


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


