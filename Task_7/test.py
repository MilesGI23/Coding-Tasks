# og = "hello world"
# og1 =(og[:5])

# print(og1)

# my_dictionary = { 
#     "name ": "terry ",  # first item .key #second item .Values # to collect both it would be .items
#     "age" : 23,
#     "is funny": False
#     }

# print(my_dictionary["age"])

# cat = dict(name="kitty" , age=0.5)
# print(cat)

# cat["colour"] = "white "
# print(cat)

# popped_pair = cat.pop("colour")
# print(cat)
# print(popped_pair)

# string_list = ["john", "Mary", "Harry "]
# print(string_list)

# pet_list = ["cat", "dog", "hamster", "goldfish", "parrot"]
# print(pet_list[0])

# num_list = [1,4,2,7,5,9]
# print(num_list[1:2])



# name_list = ["james","Molly", "Chris", "peter", "Kim"]
# name_list[2] ="Tom"

# print(name_list)


# new_list = [34, 35,75,"coffe ",98.8]
# new_list.append("Tea")

# print(new_list)

# char_list = ['p','y', 't','h','o','n']
# del char_list[3]

# print(char_list)


# a = [1,2,3]
# b = [4,9,8]
# c = [a,b,"tea",16]

# print(c)
# import copy

# a = [[1,2,3],[4,5,6]]
# b = a[:]
# c = copy.deepcopy(a) 
# d = copy.copy(a)
# b[0][1]=10
# c[1][1]=12
# #print(a)
# #print(b)
# print(c)
# print(d)

# print("Example 2: ")

# fact1 = "The original name of Windows was Interface Manager."
# fact1 = fact1.upper()
# print(fact1)
# fact1 = fact1.lower()
# print(fact1)

# fact2 = "          The$first$electronic$computer$ENIAC$weighed$more$than$27$tons.          "
# # fact2 = fact2.replace("$", "WOW!")
# # print(fact2)
# fact2 = fact2.strip()
# print(fact2)

# alt_char = "The World is round"
# capitalized_string = ""

# for _ in range(len(alt_char)):
#     if _ % 2 == 0:
#         capitalized_string += alt_char[_].upper()
#     else:
#         capitalized_string += alt_char[_].lower()

# print(capitalized_string)

# alt_char = "The World is round"

# capitalized_string = ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(alt_char)])

# print(capitalized_string)

#print("Example 2: ")

# fact1 = "The original name of Windows was Interface Manager."
# fact1 = fact1.upper()
# print(fact1)
# fact1 = fact1.lower()
# print(fact1)


# fact2 = "          The$first$electronic$computer$ENIAC$weighed$more$than$27$tons.          "
# fact2 = fact2.replace("$", "WOW!")
# print(fact2)
# fact2 = fact2.strip()
# print(fact2)
# fact2 = fact2.split("WOW!")
# print(fact2)


# for _ in range(len(red_char)):
# #        if _ % 2== 0:
# #               cap_char += red_char[_].upper()
# #        else:
# #            cap_char += red_char[_].lower()   

# # print(cap_char)

# rc = red_char.split()


# for _ in range (len(rc)):
#       if _ % 2 == 0:
#             rc[_] = rc[_].upper()
      
# rc = ' '.join(rc)

# print(rc)

# menu = ["Cheese and Toast","Hot Dog", "Full English","Ham Sandwich"]

# stock = {
#             'Cheese and Toast':100, 
#             'Hot Dog':175, 
#             'Full English':75,
#             'Ham Sandwich': 25
#             }

# price = {
#             'Cheese and Toast':2.75,
#             'Hot Dog': 1.99,
#             'Full English': 5.59,
#             'Ham Sandwich': 1.89
#              } 

# total_stock = 0

# for items in menu:
#     item_value = stock[items] * price[items]
#     total_stock += item_value

# print(total_stock)

# red_char = "The world is round and i live on it"
# cap_char = ""

# for _ in range(len(red_char)):
#     if _ % 2 == 0:
#         cap_char += red_char[_].upper()
#     else:
#         cap_char += red_char[_].lower()

# print(cap_char) 

# rc = red_char.split()

# for _ in range(len(rc)):
#     if _ % 2 == 0:
#         rc[_] = rc[_].upper()

# print(' '.join(rc))
import math

num_list = ['4', '7','14','25','24','36' ]
new_num_listints = [int(elements) * 2 for elements in num_list]


print(new_num_listints)

 