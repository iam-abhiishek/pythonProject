# wap to print 1 to 100

# i = 1
#
# while i <= 100:
#     print(i)
#     i += 1

# wap to print 100 to 1

# i = 100
#
# while i >= 1:
#     print(i)
#     i -= 1

# wap to print multiplication of 3

# i = 1
# while i <= 10:
#     print(3 * i)
#     i = i + 1

# i = 1
# num = int(input("enter ur number\n"))
# while i <= 10:
#     print(num * i)
#     i = i + 1

# wap to print values of list
#
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0
# while index <= len(list)-1:
#     print(list[index])
#     index = index + 1

# wap to find a number in tuple using loop

# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
#
# i = 0
# num = 16

# while i < len(tuple):
#     if tuple[i] == num:
#         print(num)
#         break
#     else:
#         i = i + 1

# while i < len(tuple):
#     if tuple[i] == num:
#         print("found at index", i,"is" ,num)
#     else:
#         print("finding")
#     i = i + 1

i = 0
# while i <= 5:
#     if i == 3:
#         i = i + 1
#         continue #skip in current iteration
#     print(i)
#     i = i + 1

while i <= 10:
    if i % 2 == 0:
        i = i + 1
        continue #skip in current iteration
    print(i)
    i = i + 1
