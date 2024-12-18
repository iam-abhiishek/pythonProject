import time

timestamp = time.strftime("%H,%M,%S")
print(timestamp, type(timestamp))

timestamp1 = int(time.strftime("%H"))
timestamp2 = int(time.strftime("%M"))
timestamp3 = int(time.strftime("%S"))
print(timestamp1, timestamp2, timestamp3)
if 0 < timestamp1 <=11 and 00 < timestamp2 << 59:
    print("good morning")
elif 12 <= timestamp1 <=18 and 00 < timestamp2 << 59:
    print("good evening")
else:
    print("good night")