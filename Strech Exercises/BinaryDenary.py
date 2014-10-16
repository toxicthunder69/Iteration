#Joseph Everden
#16/10/14
#Binary to Denary

place_value = 128
denary = 0
binary_string = input("Enter an 8-bit binary number: ")
binary_list = list(binary_string)
for count in range(0,8):
    denary_value = int(binary_list[count]) * place_value
    place_value /= 2
    denary += int(denary_value)
print("The 8-bit binary numer {} is {} in denary.".format(binary_string,str(denary)))
