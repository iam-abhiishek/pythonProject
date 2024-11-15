names = ['abhishek', 'monu', 'raj']
print(names)

nums = [1, 2, 3]
# print(nums)
#
# values = [names, nums]
# print(values)

nums.append(87)
# print(nums)

nums.insert(1,98)
print(nums)

nums.remove(2)
print(nums)

nums.pop(0)
print(nums)

nums.pop()
print(nums)

nums.append(23)
print(nums)

del nums[2:]
print(nums)

# nums.append([212, 323, 4343])
# print(nums)

nums.extend([212, 323, 4343])
print(nums)

print(min(nums))

print(max(nums))

print(sum(nums))

print(sorted(nums))

nums [0] = 99
print(nums)
