#List datastructure- ordered, changeable, allow duplicate values
fruits=["Mangoes","Banana", "Oranges"]

fruits[2]="Grape"
print(f"I love eating {fruits[0]}")
print(f"I love eating {fruits[2]}")
print(f"I love eating {fruits}")

for i in fruits:
    print(i)

#tuple DS- ordered and unchangeable

cars = ("mercedes","Lamborghini","Porche")

print(cars)


#Sets DS- its unordered, unchangeable and unindexed

colors={"green","yellow","blue","orange","grey"}
print(colors)

#Dictionary-its ordered, changeable, do not allow duplicates

student = {
    "name": "Jacktone",
    "course": "CS",
    "Age": "27",
    "Uni": "KCA"
}

print(student["course"])