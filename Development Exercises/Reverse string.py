#Joseph Everden
#09/10/14
#Reverse String
num = 0
string = input("Enter your text: ")
string_leng = len(string)
string = [string]
for count in range(string_leng,0,-1):
    print(string[count])
