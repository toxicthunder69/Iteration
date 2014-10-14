#Joseph Everden
#09/10/14
#Asterisk table

stars = int(input("How many stars per row? "))
rows = int(input("How many rows? "))
star = ""
for count in range(stars):
    star = star + "*"
for count in range(rows):
    print(star)
