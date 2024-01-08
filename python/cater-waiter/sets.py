"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name: str, dish_ingredients: list) -> tuple:
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list) -> str:
    return "".join(f"{drink_name} {'Cocktail' if ALCOHOLS.intersection(set(drink_ingredients)) else 'Mocktail'}")


def categorize_dish(dish_name: str, dish_ingredients: list) -> str:
    category_name = ["VEGAN", "VEGETARIAN", "PALEO", "KETO", "OMNIVORE"]
    for index, cat in enumerate([VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE]):
        if cat.issuperset(set(dish_ingredients)): return f"{dish_name}: {category_name[index]}"


def tag_special_ingredients(dish: tuple) -> tuple:
    return (dish[0], SPECIAL_INGREDIENTS.intersection(set(dish[1])))


def compile_ingredients(dishes: list) -> set:
    ingr = set()
    for dish in dishes:
        ingr = ingr | dish
    return ingr


def separate_appetizers(dishes: list, appetizers: list) -> list:
    return list(set(dishes).difference(set(appetizers)))


def singleton_ingredients(dishes: list, intersection: set) -> set:
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    ingr = set()
    for dish in dishes:
        ingr = ingr.union(dish.difference(intersection))
    return ingr
