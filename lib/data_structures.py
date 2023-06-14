spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    food_name = [food["name"] for food in spicy_foods]
    return food_name


def get_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_food


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶'}"
        )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(
                f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶'}"
            )
    return None


def get_average_heat_level(spicy_foods):
    spicy_level = [food["heat_level"] for food in spicy_foods]
    return sum(spicy_level) / len(spicy_level)


def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = list(spicy_foods)
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods
