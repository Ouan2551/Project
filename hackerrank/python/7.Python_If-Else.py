x = int(input())
if x % 2 != 0:
    print("Weird")
elif x >= 2 and x <= 5:
    print("Not Weird")
elif x >= 6 and x <= 20:
    print("Weird")
else:
    print("Not Weird")