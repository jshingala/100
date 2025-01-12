import random
USA = ["DL", "PA", "NJ"]

print(USA[0])

USA.append("CA")
print(USA)

friend = ["David", "Priya", "Jenil", "Taekjin", "Neirel", "Prabhav"]
friend[-1]= "Jay"

random  = random.choice(friend)
print(f"The person who pays the bill is {random}")

print(len(friend))

dirty_dozen= ["Spinach", "Strawberries", "Kale", "Nectarines", "Apple", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes","Celery", "Potatoes"]

fruits= ["Strawberries", "Apple", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables= ["Spinach", "Kale", "Nectarines", "Tomatoes", "Celery", "Potatoes"]

dd = [fruits, vegetables]
print(dd[1][1])