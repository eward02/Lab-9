#Elise Ward and Leena
#L91.py

#dictionaries
d1 = {"hello":"goodbye","hi":"bye","hey":"see you"}
d2 = {"cat":True, "dog":False}
d3 = {10:1, 20:2,30:3, 40:4}
d4 = {1.4:2.4, 1.2:2.2, 4.6:3.6}
                  
#create get function
def my_get_method(dictionary,key):
    if key in dictionary:
        print(dictionary[key])

#call function
my_get_method(d1,"hello")
print(d1.get("hello"))

my_get_method(d2,"dog")
print(d2.get("dog"))

my_get_method(d3,30)
print(d3.get(30))

my_get_method(d4,1.4)
print(d4.get(1.4))
