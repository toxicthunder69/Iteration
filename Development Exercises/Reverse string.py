#Joseph Everden
#09/10/14
#Reverse String

string = input("Enter your text: ")
string_leng = len(string)
string = [string]
print(string_leng)
for count in range(0,string_leng,-1):
    letter = string[count]
    print(letter)
