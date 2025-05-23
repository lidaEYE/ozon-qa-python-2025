import requests

# Функция поиска самого высокого героя 
def tallest_hero(gender: str, job: str):
    
    # Проверка корректности запроса
    if gender not in ['male', 'female'] or job not in ['yes', 'no']:
        print('Неверный запрос. Попробуйте снова.')
        return

    # Запрос к api
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)

    # проверка статус кода
    if response.status_code == 200:
        heroes = response.json()
    else:
        print("Ошибка:", response.status_code)

    # Объявление двух переменных: для максимального роста и для конечного героя
    max_height = None
    result_hero = None

    # Конвертация yes/no в булевое значение
    has_job = job.lower() == 'yes'

    # Обработка параметров всех героев
    for hero in heroes:
        # Проверка пола героя
        if hero["appearance"]["gender"].lower() != gender.lower():
            continue
        
        # Проверка наличия работы у героя
        occupation = hero["work"]["occupation"].lower()
        employment_status = occupation not in ["-", "none", "unemployed", ""]
        
        if employment_status != has_job:
            continue
        
        # Обработка роста героя 
        height_data = hero["appearance"]["height"]
        if isinstance(height_data, list) and len(height_data) >= 2:
            height_str = height_data[1]
            
            # Если рост в сантиметрах
            if "cm" in height_str:
                height_cm = float(height_str.replace("cm", "").strip())
            
            # Если рост в метрах
            elif "meters" in height_str:
                height_cm = float(height_str.replace("meters", "").strip()) * 100
            else:
                continue

            if max_height is None or height_cm > max_height:
                max_height = height_cm
                result_hero = hero
                continue

    print(f'Самый высокий супергерой: {result_hero["name"]}. Рост супергероя: {result_hero["appearance"]["height"][1]}.')

if __name__ == "__main__":
    gender = input("Введите пол супергероя (male/female): ")  
    job = input("У супергероя есть работа? (yes/no): ")
    tallest_hero(gender, job)