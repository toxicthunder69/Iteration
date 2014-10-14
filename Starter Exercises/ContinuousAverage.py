#Joseph Everden
#09/10/14
#Continuous Average

num = 0
total = 0
tally = 0
print("Enter as many numbers as you want, enter -1 to get the average.")
while num != -1:
    num = int(input("Enter a number: "))
    tally = tally + 1
    total = total + num
print("The average is {0}.".format(total / tally))
