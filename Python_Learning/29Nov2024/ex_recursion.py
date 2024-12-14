# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("end")
#
# show(3)
from operator import index

#write a recursive function to print sum of first n natural number
#
# def sum_of_num(n):
#     if(n == 0):
#         return 0
#     return sum_of_num(n-1) + n
#
# sum = sum_of_num(10)
# print(sum)

# write a recursive function to print all element in list
list = [1, 2, 3, 4]
def print_list(list, index):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list, index+1)

print_list(list, 0)