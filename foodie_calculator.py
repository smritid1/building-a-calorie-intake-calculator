#import json 
# Import the json module to work with JSON files 
# # Open the nutrition.json file in read mode and load its content into a dictionary 
#with open('nutrition.json', 'r') as json_file: 
#    nutrition_dict = json.load(json_file) # Load the JSON content into a dictionary







import json

# Load JSON file
with open('nutrition.json', 'r') as file:
    nutrition_dict = json.load(file)


# Function to calculate nutrition
def nutritional_summary(food_dict):
    totals = {
        "calories": 0,
        "total_fat": 0,
        "protein": 0,
        "carbohydrate": 0,
        "sugars": 0
    }

    for food, grams in food_dict.items():
        if food not in nutrition_dict:
            return food

        data = nutrition_dict[food]

        for key in totals:
            totals[key] += (data[key] * grams) / 100

    return totals


# ----------- INPUT PART -----------

foods = {}

print("Enter food items (type 'done' to finish):")

while True:
    name = input("Food name: ")

    if name.lower() == "done":
        break

    grams = float(input("Grams: "))

    foods[name] = grams


# ----------- PROCESS -----------

result = nutritional_summary(foods)


# ----------- OUTPUT -----------

if isinstance(result, str):
    print("Food not found:", result)
else:
    print("\nNutritional Summary:")
    for key, value in result.items():
        print(key, ":", round(value, 2))