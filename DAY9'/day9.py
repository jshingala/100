dict = { 
    "Bug": "An error in the program",
    "Functions": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something again and again"
}

dict["Dog"]= "Is an animal"
print(dict)

eDict={}

dict["Bug"]= "An error"
print(dict)

for thing in dict.items():
    print(thing)


captails ={
    "France": ["Paris", "Little", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}



for i, j in captails.items():
    print(j[1])

nestedList= ["a", "b", ["c", "d"]]

print(nestedList[2][1])

nestDict = {
    "China": {
        "numVisted": 2,
        "citiesVisted" : 3,
    },
    "India": {
        "numVisted": 2,
        "citiesVisted" : 3
    },
}

for i, j in nestDict.items():
        print(i)
        print(j)
        



