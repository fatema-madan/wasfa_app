import pandas as pd
import os


def view_recipes():
    df = pd.read_csv("data/recipes.csv")
    return df


def random_recipe():
    df = pd.read_csv("data/recipes.csv")
    return df.sample()


def search_recipe(ingredient):
    df = pd.read_csv("data/recipes.csv")
    return df[df["ingredients"].str.contains(ingredient, case=False, na=False)]


def add_recipe(name, ingredients, prep_time, instructions, difficulty, category, rating):
    df = pd.read_csv("data/recipes.csv")

    new_row = {
        "name": name,
        "ingredients": ingredients,
        "prep_time": prep_time,
        "instructions": instructions,
        "difficulty": difficulty,
        "category": category,
        "rating": rating
    }

    df.loc[len(df)] = new_row
    df.to_csv("data/recipes.csv", index=False)


# Stretch Goal 1: Sort by Rating
def sort_by_rating():
    df = pd.read_csv("data/recipes.csv")
    return df.sort_values(by="rating", ascending=False)


# Stretch Goal 2: Scale Ingredient Quantities
def scale_ingredients(ingredients, servings):
    items = ingredients.split(",")

    scaled = []
    for item in items:
        scaled.append(f"{servings} x {item.strip()}")

    return ", ".join(scaled)


# Stretch Goal 3: Shopping List
def shopping_list():
    df = pd.read_csv("data/recipes.csv")

    shopping = []

    for ingredients in df["ingredients"]:
        shopping.extend(ingredients.split(","))

    return [item.strip() for item in shopping]


# Stretch Goal 4: Cooking History
def save_history(recipe_name):
    file = "data/history.txt"

    with open(file, "a") as f:
        f.write(recipe_name + "\n")


def view_history():
    file = "data/history.txt"

    if not os.path.exists(file):
        return []

    with open(file, "r") as f:
        return f.readlines()
