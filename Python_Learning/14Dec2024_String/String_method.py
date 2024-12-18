name = "!!!Hello world!!!!@@"
print(name.upper())
print(name.lower())
print(name.rstrip("@,!"))
print(name.replace("Hello world","how r u"))
print(name.split())

heading = "lets gO to market"
print(heading.capitalize())
print(len(heading))
print((heading.center(20)))
print(len(heading.center(20)))

print(name.endswith("@"))
print(heading.endswith("ts",0,4))

str1 = "Hes name is Dan He is an honest man"
print(str1.find("is"))
print(str1.find("dfdfd"))
str2 = "hi\n"
print(str2.isalpha())
print(str2.islower())
print(str2.isprintable())
# print(str1.index("ishh"))

str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())

print(8, end=" ")
