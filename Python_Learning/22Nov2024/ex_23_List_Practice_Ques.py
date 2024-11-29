# movie1 = input("enter 1st movie name\n")
# movie2 = input("enter 2nd movie name\n")
# movie3 = input("enter 3rd movie name\n")
#
# list = [movie1, movie2, movie3]
# print(list)


# movies = []
# movies.append(input("enter movie 1"))
# movies.append(input("enter movie 2"))
# movies.append(input("enter movie 3"))
# print(movies)

# program to check palindrome exists in a list

list = [1, 2, 3]
list2 = [1, 2, 1]
list3 = list2.copy()
list1 = list.copy()
list1.reverse()
list2.reverse()
print(list1)
print(list2)

if list == list1:
    print("it is a palindrome")
elif list2 == list3:
    print("it is a palindrome")
else:
    print("its not")
