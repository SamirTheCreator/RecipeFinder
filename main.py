'''
This program lets user create his own recipes and works as a recipe book,
the user can either look up the recipe by the name or the products.
'''
import pickle #saving and retrieving recipes from a "book"

class Recipe:
   def __init__(self, name, description, products, calories, nutrition, steps):
    self.name = name
    self.description = description
    self.products = products
    self.steps = steps
    self.calories = calories
    self.nutrition = nutrition

def recipeMenu(recipe):
    print("1. See ingredients\n2. See steps")
    choice = input()
    match choice:
        case '1':
            for product in recipe.products:
                print(product, ": ", recipe.products[product])
        case '2':
            cook(recipe)

def addRecipe():
    print("Name: ")
    name = input()
    print("Number of ingredients")
    num = int(input())
    products = {}
    for i in range(num):
        print("Name: ")
        name = input()
        print("Quantity: ")
        quantity = int(input())
        products[name] = quantity
    print("Decription: ")
    desc = input()
    print("Calories: ")
    calories = input()
    print("Nutrition (%): ")
    nutrition = input()
    print("Number of steps: ")
    num1 = int(input())
    steps = []
    for i in range(num1):
        print("input step ", i, ": ")
        step = input()
        steps.append(step);
    
    recipes = []
    recipes.append(Recipe(name, desc, products, calories, nutrition, steps))
    add(recipes)

def add(recipes):
    with open('book.pkl', 'rb') as inp:
        while True:
            try:
                recipe = pickle.load(inp)
            except EOFError:
                break
            recipes.append(recipe)

    with open('book.pkl', 'wb') as outp:
        for recipe in recipes:
            pickle.dump(recipe, outp, pickle.HIGHEST_PROTOCOL)
    
def showListOfRecipes():
    with open('book.pkl', 'rb') as inp:
        while True:
            try:
                recipe = pickle.load(inp)
            except EOFError:
                break
            print(recipe.name)

def cook(recipe):
    i=1
    for step in recipe.steps:
        print("Step ", i, "\n", step)
        i+=1
        x = input()

def searchByName(name):
    found = False
    with open('book.pkl', 'rb') as inp:
        while True:
            try:
                recipe = pickle.load(inp)
            except EOFError:
                break
            if recipe.name == name:
                found = True
                break;
        if found:
            recipeMenu(recipe)
        else:
            print("Not found")

def searchByProducts(products):
    found = False
    recipe = Recipe()
    with open('book.pkl', 'rb') as inp:
        while True:
            try:
                recipe = pickle.load(inp)
            except EOFError:
                break
            if recipe.products == products:
                found = True
                break;
        if found:
            recipeMenu(recipe)
        else:
            print("Not found")


def menu():
    print("1. Find recipe by the name\n2. Find recipe by products\n3. Add recipes\n4. Show list of recipes")
    choice = input()
    match choice:
        case '1':
            print("Enter the name of the recipe ")
            name = input()
            searchByName(name)
        case '2':
            print("Enter the number of products")
            num = int(input())
            dict = {}
            for i in range(num):
                print("Name: ")
                name = input()
                print("Quantity: ")
                quantity = input()
                dict[name] = quantity
        case '3':
            addRecipe()
        case '4':
            showListOfRecipes()
def driver():
    recipes = []
    products = {
        "Bacon": 2,
        "Garlic":2,
        "Spaghetti":1,
        "Grated Parmesano":1,
        "Eggs":1,
        "Fresh parsley":2

    }
    steps = {
        "Add bacon and water to a skillet and bring to a simmer.",
        "Continue simmering until water is evaporated, then continue to cook the bacon until crispy.",
        "Remove bacon from pan and reserve the drippings.",
        "Saute garlic in that same skillet until golden brown, then add to a bowl with 1 tablespoon bacon fat, eggs, egg yolk, Parmesan and pepper. Mix well.",
        "Meanwhile, cook the spaghetti or linguine pasta until al dente. Once cooked, drain pasta and reserve 1 cup of the cooking water.",
        "Slowly pour the hot cooking water into the egg mixture. Then pour over the hot pasta and toss to coat. Add crumbled bacon."
    }
    recipes.append(Recipe("Pasta Carbonara", "Pasta carbonara typically features a creamy sauce that’s made with pancetta, garlic, pasta water, cheese and eggs. The egg-based sauce is cooked by combining it with the piping hot spaghetti pasta and a little of the cooking water.", products, 155, 0.4, steps))
    add(recipes)
    
    menu()



driver()