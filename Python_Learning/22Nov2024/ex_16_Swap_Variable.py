a = 10
b = 20

# a, b = b, a
#
# print(a, b)

a = a ^ b
print(a)
b = a ^ b
print(b)
a = a ^ b
print(a)

print(a, b)