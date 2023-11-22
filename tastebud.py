recipes =[["Epic Baba Ganoush", "eggplant", "garlic","lemon juice","tahini","olive oil","parsley","salt","cumin","paprika"],
          ["Rice Krispy Treats", "butter","marshmallow","rice krispies"]]
ingredients = []

print("Welcome to TasteBud!")
print("Please enter the ingredients you have on hand(type exit to stop input)")

ingredientInput = ""
loopCounter = 1
while ingredientInput != "exit":
    ingredientInput = input("Ingredient # "+str(loopCounter)+":")
    if ingredientInput == "exit":
        break

    ingredients.append(ingredientInput)
    loopCounter = loopCounter + 1

print("Ingredients entered:"+str(ingredients))

completeRecipes = []

numberOfIngredients = 0
for recipe in recipes:
    for recipeIngredient in recipe:
        if recipeIngredient in ingredients:
            numberOfIngredients = numberOfIngredients + 1
            print("Ingredient Detected "+recipeIngredient +" Ingredient number"+str(numberOfIngredients))
    print("length of recipe "+str(len(recipe)-1))
    print("length of recipe " + str(len(recipe) - 1))
    if numberOfIngredients == len(recipe)-1:
        completeRecipes.append(recipe)

print("These are the complete recipes you can make: "+str(completeRecipes))


