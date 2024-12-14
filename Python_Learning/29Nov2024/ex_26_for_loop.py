# # wap to print elements in a list using loop
#
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for num in list:
#     print(num)

# wap to search a number x in tuple using loop

tuple = (1, 2, 3, 45, 6, 7, 99)
num = 45
index = 0

for el in tuple:
    if el == num:
        print("number is found", el)
        break
    else:
        print("finding")
        index = index + 1