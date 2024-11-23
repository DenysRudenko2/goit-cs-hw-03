from bson import ObjectId
import random

# Функція для генерації випадкових характеристик
def generate_random_features():
    possible_features = [
        "ходить в капці",
        "дає себе гладити",
        "рудий",
        "вилізає на стіл",
        "любить рибу",
        "мурчить гучно",
        "ховається під ліжком",
        "грається з м'ячиком",
        "спить цілий день",
        "любитись на сонці"
    ]
    return random.sample(possible_features, k=random.randint(2, 5))

# Генерація масиву з 30 об'єктів
cats = []

for _ in range(30):
    cat = {
        "_id": ObjectId(),
        "name": random.choice(["Барсік", "Мурчик", "Сніжок", "Сірко", "Люцик", "Тимко", "Рижик", "Соня", "Лола", "Джек"]),
        "age": random.randint(1, 15),
        "features": generate_random_features()
    }
    cats.append(cat)

# for cat in cats:
#     print(cat)