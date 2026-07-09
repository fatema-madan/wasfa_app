import pandas as pd
import os


def view_recipes():
    df = pd.read_csv("recipes.csv")
    return df


def random_recipe():
    df = pd.read_csv("recipes.csv")
    return df.sample()


def search_recipe(ingredient):
    df = pd.read_csv("recipes.csv")
    return df[df["ingredients"].str.contains(ingredient, case=False, na=False)]


def add_recipe(name, ingredients, prep_time, instructions, difficulty, category, rating):
    df = pd.read_csv("recipes.csv")

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
    df.to_csv("recipes.csv", index=False)


# Sort recipes by rating
def sort_by_rating():
    df = pd.read_csv("recipes.csv")
    return df.sort_values(by="rating", ascending=False)


# Scale ingredients
def scale_ingredients(ingredients, servings):
    items = ingredients.split(",")

    scaled = []

    for item in items:
        scaled.append(f"{servings} x {item.strip()}")

    return ", ".join(scaled)


# Shopping List with aggregation
def shopping_list():
    df = pd.read_csv("recipes.csv")

    shopping = {}

    for ingredients in df["ingredients"]:
        for item in ingredients.split(","):
            item = item.strip()

            if item in shopping:
                shopping[item] += 1
            else:
                shopping[item] = 1

    return shopping


# Save cooking history
def save_history(recipe_name):
    with open("history.txt", "a") as f:
        f.write(recipe_name + "\n")


# View cooking history
def view_history():

    if not os.path.exists("history.txt"):
        return []

    with open("history.txt", "r") as f:
        return [line.strip() for line in f.readlines()]
