recipes =[["Recipe Name", "Ingredient 1", "Ingredient 2"],
          ["Recipe Name 2", "Ingredient 1"]]
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

print("")


print("Ingredients entered:"+str(ingredients))

