cities = ["mumbai", "pune", "chennai", "jaipur", "patna"]

# def print_list(list):
#     print(len(list))
# #     # return list
#
# def list_elements(list):
#     for items in list:
#         print(items, end=" ")
#
# # print_list(cities)
# list_elements(cities)

# wap to print factorial of number (n is parameter)

# def factorial(n, i, j):
#     while i <= n:
#         j = j * i
#         i = i + 1
#     print(j)
#
# # factorial(int(input("enter ur number\n")),1)
# factorial(4,1,1)

# def factorial(n, i, j):
#     for i in range(1, n+1):
#         j = j * i
#         i = i + 1
#     print(j)
#
# # factorial(int(input("enter ur number\n")),1)
# factorial(5,1,1)

# wap to convert usd to inr
# def usd_conversion(usd):
#     inr_val = usd * 83
#     print(usd, "usd =", inr_val, "inr")
#
# usd_conversion(2)

#wap to find even or odd

def even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
        # return num

even_odd(11)
