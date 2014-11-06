#Joseph Everden
#05/11/2014
#Square number

display = []
num = int(input("Enter a number to square upto: "))
for count in range(1,num):
    square = count * count
    display.append(square)
display_leng = len(display)
rows = num // 5
remain = num % 5
for count in range(0,rows):
    for count in range(0,5):
        string = str(display[count])
        print("{0:>8}".format(string),end="")
for count in range(0,remain):
    string = str(display[count])
    print("{0:>8}".format(string),end="")
    
    
