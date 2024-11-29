# student = ["abhishek", 11, 23.5]
# print(student)
#
# student[0] = "ballu"
# print(student)
# print(student[1 : 4])
# student.sort() #TypeError: '<' not supported between instances of 'int' and 'str'
# print(student)  #TypeError: '<' not supported between instances of 'int' and 'str'

# print(student[5]) #IndexError: list index out of range
#
# list = [2, 9, 3]
# # list.sort()
# # print(list)
#
# list.append(4)
# print(list)

# str_list = ["hello", "dance", "song"]
char_list = ['s', 'a', 'j', 'b']
# char_list.sort(reverse=True)
# char_list.reverse()
char_list.insert(1, 9)
# char_list.reverse()
# char_list.sort(reverse=True) TypeError: '<' not supported between instances of 'int' and 'str'
char_list.remove(9)
# char_list.pop(2)
char_list[0] = 'w'  # list are mutable
print(char_list)



