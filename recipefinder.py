recipes =[["Epic Baba Ganoush", "eggplant", "garlic","lemon juice", "tahini", "olive oil","parsley", "salt", "cumin", "paprika"],
          ["Rice Krispy Treats", "butter", "marshmallow", "rice krispies"],["Baked Chicken","chicken","butter","salt","pepper","garlic powder","paprika"]]
ingredients = []




print("Welcome to TasteBud!")
print("Please enter the ingredients you have on hand(type exit to stop input)")

ingredientInput = ""
loopCounter = 1
while ingredientInput != "exit":
    ingredientInput = input("Ingredient # "+str(loopCounter)+":")
    if ingredientInput == "exit":
        break

    ingredients.append(ingredientInput.lower())
    loopCounter = loopCounter + 1

print("Ingredients entered:"+str(ingredients))

completeRecipes = []



numberOfIngredients = 0
for recipe in recipes:
    for recipeIngredient in recipe:
        if recipeIngredient in ingredients:
            numberOfIngredients = numberOfIngredients + 1
            #print("Ingredient Detected "+recipeIngredient +" Ingredient number"+str(numberOfIngredients))
    #print("length of recipe "+str(len(recipe)-1))
    #print("length of recipe " + str(len(recipe) - 1))
    if numberOfIngredients == len(recipe)-1:
        completeRecipes.append(recipe)


print("These are the complete recipes you can make: "+str(completeRecipes))


print("These are the recipes you are almost able to make")
almostCompleteRecipes = []
missingIngredients = []
numMissing = 0

for recipe in recipes:
    numMissing = 0
    missingIngredients = []
    for recipeIngredient in recipe:
        if recipeIngredient not in ingredients:
            numMissing = numMissing + 1
            missingIngredients.append(recipeIngredient)
            #print(recipeIngredient + " was missing!!!")
    if numMissing >1:
        print(missingIngredients.pop(0)+" Shopping List:")

        for missingIng in missingIngredients:
            print("- " + missingIng)

print("Thank you for using tastebud!!!!!")





