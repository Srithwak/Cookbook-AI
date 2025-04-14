import sys
import google.generativeai as genai

def main():
    if len(sys.argv) < 5:
        print("Error: Not enough arguments")
        return
    
    ingredients = sys.argv[1]
    meal_type = sys.argv[2]
    dish_name = sys.argv[3]
    cuisine = sys.argv[4]
    
    try:
        with open("API_KEY.txt", "r") as f:
            api_key = f.readline().strip()
        model = genai.GenerativeModel('gemini-2.0-flash-lite')
        genai.configure(api_key=api_key)
        
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
            prompt += f" using the following ingredients:\n{ingredients}\n\nRecipe:"

        response = model.generate_content(prompt)
        print(response.text)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()