#Joseph Everden
#09/10/14
#Custom Average

total = 0
averaged = int(input("Enter how many numbers are to be averaged: "))
for count in range(averaged):
    num = int(input("Enter number {0}: ".format(count + 1)))
    total = total + num
print(total / averaged)
