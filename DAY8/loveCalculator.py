def calculate_love_score(name1, name2):
    name1= name1.lower()
    name2= name2.lower()
    name = name1 + name2
    count = 0
    count1= 0
    trueLetter= "true"
    loveLetter= "love"

    for i in name:
        if i in trueLetter:
            count+= 1
    
    for i in name:
        if i in loveLetter:
            count1 +=1
        

    print(f"{count}{count1}")

calculate_love_score("true", "love")