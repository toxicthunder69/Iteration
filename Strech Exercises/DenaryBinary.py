#Joseph Everden
#15/10/14
#Denary to Binary

place_value = 128
binary_string = ""
denary = int(input("Enter a value up to 255: "))
denary_start = denary
for count in range(0,8):
    if denary >= place_value:
        binary_value = str(int(denary // place_value))
        denary -= place_value
    else:
        binary_value = "0"
    if place_value > 0:
        place_value = place_value / 2
    binary_string += binary_value
print("The denary value {} is {} in 8-bit binary.".format(denary_start,binary_string))
