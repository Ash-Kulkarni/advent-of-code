import re
from typing import NamedTuple
import itertools
# Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
# Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
# Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8

class Ingredient(NamedTuple):
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

def get_data():
    pattern = re.compile(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
    with open('input.txt') as f:
        data = f.read()

    ingredients = []
    for m in re.finditer(pattern, data):
        name, capacity, durability, flavor, texture, calories = m.groups()
        ingredients.append(Ingredient(name, int(capacity), int(durability), int(flavor), int(texture), int(calories)))
    return ingredients


class IngredientAmount(NamedTuple):
    ingredient: Ingredient
    amount: int

def get_cookie_score(ingredients_amounts):
    capacity = durability = flavor = texture = calories = 0
    for ia in ingredients_amounts:
        i = ia.ingredient
        amount = ia.amount
        capacity += i.capacity * amount
        durability += i.durability * amount
        flavor += i.flavor * amount
        texture += i.texture * amount
        calories += i.calories * amount
    return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture), calories

def main():
    kitchen_ingredients = get_data()
    ingredient_permutations = [i for i in itertools.product(range(101), repeat=len(kitchen_ingredients)) if sum(i) == 100]
    highest_score = 0
    for ip in ingredient_permutations:
        score, calories = get_cookie_score([IngredientAmount(i, a) for i, a in zip(kitchen_ingredients, ip)])

        if calories != 500:
            continue
        if score > highest_score:
            highest_score = score
    print(highest_score)

if __name__ == "__main__":
    main()
