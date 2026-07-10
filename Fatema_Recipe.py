import streamlit as st
import helper as h

st.title("🍽️ Wasfa App")
st.write("Manage your favorite recipes easily")

menu = st.sidebar.selectbox(
    "Choose option",
    [
        "Add Recipe",
        "View Recipes",
        "Search Recipe",
        "Random Recipe",
        "Sort by Rating",
        "Shopping List",
        "Cooking History"
    ]
)


if menu == "Add Recipe":

    name = st.text_input("Recipe Name")
    ingredients = st.text_input("Ingredients (comma separated)")
    prep_time = st.number_input("Preparation Time (minutes)", min_value=1)
    instructions = st.text_area("Instructions")

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    category = st.selectbox(
        "Category",
        ["Breakfast", "Lunch", "Dinner", "Dessert"]
    )

    rating = st.slider("Rating", 1, 5)

    if st.button("Add Recipe"):

        if name.strip() == "" or ingredients.strip() == "" or instructions.strip() == "":
            st.error("Please fill in all required fields.")

        else:
            h.add_recipe(
                name,
                ingredients,
                prep_time,
                instructions,
                difficulty,
                category,
                rating
            )

            st.success("Recipe added successfully 🎉")
            st.balloons()


elif menu == "View Recipes":

    recipes = h.view_recipes()

    if len(recipes) == 0:
        st.warning("No recipes found.")

    else:
        for _, row in recipes.iterrows():

            with st.expander(f"🍽️ {row['name']}"):

                st.write(f"🧂 Ingredients: {row['ingredients']}")
                st.write(f"⏱️ Preparation Time: {row['prep_time']} min")
                st.write(f"📖 Instructions: {row['instructions']}")
                st.write(f"🔥 Difficulty: {row['difficulty']}")
                st.write(f"🍴 Category: {row['category']}")
                st.write(f"⭐ Rating: {'⭐' * int(row['rating'])}")

                if st.button(
                    f"I cooked {row['name']} 🍽️",
                    key=f"view_{row['name']}"
                ):
                    h.save_history(row['name'])
                    st.success("Added to cooking history!")


elif menu == "Search Recipe":

    ingredient = st.text_input("Enter ingredient")

    if ingredient:

        results = h.search_recipe(ingredient)

        if len(results) == 0:
            st.warning("No recipes found with this ingredient.")

        else:

            for _, row in results.iterrows():

                with st.expander(f"🍽️ {row['name']}"):

                    st.write(f"🧂 Ingredients: {row['ingredients']}")
                    st.write(f"⏱️ Prep Time: {row['prep_time']} min")
                    st.write(f"📖 Instructions: {row['instructions']}")
                    st.write(f"🔥 Difficulty: {row['difficulty']}")
                    st.write(f"🍴 Category: {row['category']}")
                    st.write(f"⭐ Rating: {'⭐' * int(row['rating'])}")

                    if st.button(
                        f"I cooked {row['name']} 🍽️",
                        key=f"search_{row['name']}"
                    ):
                        h.save_history(row['name'])
                        st.success("Added to cooking history!")


elif menu == "Random Recipe":

    df = h.view_recipes()

    if len(df) > 0:

        recipe = h.random_recipe().iloc[0]

        st.balloons()

        st.subheader(recipe["name"])

        st.write("🧂 Ingredients:", recipe["ingredients"])
        st.write("⏱️ Prep Time:", recipe["prep_time"], "min")
        st.write("📖 Instructions:", recipe["instructions"])
        st.write("🔥 Difficulty:", recipe["difficulty"])
        st.write("🍴 Category:", recipe["category"])
        st.write("⭐ Rating:", "⭐" * int(recipe["rating"]))


        servings = st.number_input(
            "Number of Servings",
            min_value=1,
            value=1
        )

        st.write(
            "🧮 Scaled Ingredients:",
            h.scale_ingredients(
                recipe["ingredients"],
                servings
            )
        )


        if st.button(
            "I cooked this recipe 🍽️",
            key="random_recipe_button"
        ):
            h.save_history(recipe["name"])
            st.success("Added to cooking history!")


    else:
        st.warning("No recipes yet. Add one first!")


elif menu == "Sort by Rating":

    st.subheader("⭐ Recipes Sorted by Rating")

    st.dataframe(
        h.sort_by_rating()
    )


elif menu == "Shopping List":

    st.subheader("🛒 Shopping List")

    items = h.shopping_list()

    if len(items) == 0:
        st.info("No ingredients found.")

    else:

        for item, quantity in items.items():
            st.write(f"• {item}: {quantity}")


elif menu == "Cooking History":

    history = h.view_history()

    st.subheader("📜 Cooking History")

    if len(history) == 0:
        st.info("No cooking history yet.")

    else:
        for item in history:
            st.write("🍽️", item)
