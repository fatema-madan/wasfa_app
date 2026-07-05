# 🍽️ Wasfa App

## Problem Statement
Many people find it difficult to organize and manage their favorite recipes in one place. Recipes are often scattered across notes, apps, or paper, making them hard to access and search.

---

## Solution
Wasfa App is a Streamlit-based application that allows users to store, manage, and explore recipes easily using a CSV file.

---

## Features
- Add new recipes to the collection  
- Search recipes by ingredient  
- View all recipes  
- View a random recipe suggestion  
- Categorize recipes (Breakfast, Lunch, Dinner, Dessert)  
- Rate recipes and manage ratings  
- Sort recipes by rating  
- Scale ingredient quantities based on servings  
- Generate a shopping list from recipes  
- Track cooking history of viewed recipes

---

## Project Structure & Files

- **Fatema_Recipe.py** → Main Streamlit application (UI + user interaction)
- **helper.py** → Backend functions (add, search, sort, random recipe, etc.)
- **recipes.csv** → Stores all recipe data
- **history.txt** → Stores cooking history (recipes viewed by user)

---

## Technologies Used
- Python
- Streamlit
- Pandas
- CSV file storage

---

## How to Run

1. Install required libraries:
  - pip install streamlit pandas

2. Run the application:
  - streamlit run Fatema_Recipe.py

---

## Try the application online

[Wasfa App](https://wasfabh.streamlit.app/)
