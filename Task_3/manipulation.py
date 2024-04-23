str_manip = input("Hi, Can you name me 5 countries in europe..? ")

print(input(str_manip))
length_of_str_manip = (len(str_manip))
print("the length of this sentence is:", length_of_str_manip)


last_letter = (str_manip[-1])
print("last_letter:", last_letter)

str_manip_RP = str_manip.replace(last_letter, "@")
print("last_letter_replacement @:", str_manip_RP )

print("last_three_characters:", str_manip[-1:-4:-1])

print("first_3_character_last_2:", ( str_manip[:3] + str_manip[-3:]))