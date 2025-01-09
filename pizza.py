print("Welcome to the pythonbcode ")
size =input("Please select your size pizza for the pizza,L,M,S")
extracheese= input("do you want extr cheese")
veggiepizza= input("Do want the veggie in it ")

bill =0

if size =='s':
    bill+= 15
elif size == 'm':
    bill += 19
elif size == 'l':
    bill +=33

else:
    print("Invalid choice")

if extracheese == 'y':
    if size == 's':
        bill += 2
    else:
        bill +=5


if veggiepizza == 'y':
    if size == 's':
        bill+=10

print(f"Your bill is : ${bill}")