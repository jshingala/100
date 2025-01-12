fruits= ["Apple", "Pear", "Berries"]

for fruit in fruits:
    print(fruit)



student_scores = [1200, 45, 66, 77 , 88, 9229, 66, 55 , 43, 80]

totalScore= sum(student_scores)

suma=0

for i in student_scores:
    suma += i

print(suma)

for i in range(30):
    print(int((i/2)+1)*2)

# to find the max scores
maxScore= 0
for i in student_scores:
    if maxScore < i:
        maxScore = i

print(maxScore)


# For loops for the range
suma2 = 0
for i in range(100):
    suma2+=i

print(suma2)

# Fizz Buzz game
for i in range(1,101):
    if i % 3 == 0 and i % 5  == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)