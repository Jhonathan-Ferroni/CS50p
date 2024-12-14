def nutrition(food):
    # Dicionário com os alimentos e suas calorias
    calories_dict = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80,
    }

    # Formata a entrada para padronizar
    food = food.capitalize()

    # Retorna as calorias se a fruta existir, ou None
    return calories_dict.get(food)


def main():
    # Solicita a entrada do usuário
    food = input("Item: ")

    # Obtém as calorias com base no alimento
    calories = nutrition(food)

    if calories is not None:
        print(f"Calories: {calories}")


main()
