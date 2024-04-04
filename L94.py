#Leena and Elise
#L94.py

#Cake Recipe
lemon_cake = {"Flour":1,"Eggs":2,"Sugar":3,"Butter":4,"Baking Powder":5,"Baking Soda":6, "Lemons":7,"Milk":8,"Vanilla Extract":9}
red_velvet_cake = {"Flour":1,"Cocoa Powder":2,"Butter":3,"Oil":3,"Sugar":4,"Vanilla Extract":5,"Eggs":6,"Food Coloring":7,"Milk":8,"White Vinegar":9}

same=[]

for ing in lemon_cake:
    if ing in red_velvet_cake:
        same.append(ing)
print(same)


