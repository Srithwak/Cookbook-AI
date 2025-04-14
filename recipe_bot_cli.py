import google.generativeai as genai

genai.configure(api_key="AIzaSyCO3YkbCrs6oNtQ3r1H35yXSLszxPqyx6g")

model = genai.GenerativeModel('gemini-2.0-flash-lite')

def generate_recipe(ingredients, meal_type="any", dish_name="", cuisine="any"):
    prompt = f"Generate a recipe"
    if dish_name:
        prompt += f" for {dish_name}"
    else:
        prompt += f" for {meal_type} using the following ingredients:\n{ingredients}"

    if cuisine != "any":
        prompt += f" with a {cuisine} cuisine."
    elif not dish_name:
        prompt += "."
    else:
        prompt += " using the following ingredients:\n{ingredients}\n\nRecipe:"

    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("Welcome to the Recipe Bot!")
    ingredients_input = input("Enter your ingredients separated by commas:\n")
    meal_type_input = input("Pick between: Breakfast, lunch, Dinner, Snack, any?):\n").lower()
    specific_dish_input = input("Any specific dish?:\n").lower()
    cuisine_input = input("What cuisine type would you prefer? (e.g., Italian, Mexican, Indian, or any):\n").lower()

    recipe = generate_recipe(ingredients_input, meal_type_input, specific_dish_input, cuisine_input)
    print("\nHere's your recipe:\n")
    print(recipe)