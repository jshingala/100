import random
USA = ["DL", "PA", "NJ"]

print(USA[0])

USA.append("CA")
print(USA)

friend = ["David", "Priya", "Jenil", "Taekjin", "Neirel", "Prabhav"]
random  = random.choice(friend)
print(f"The person who pays the bill is {random}")