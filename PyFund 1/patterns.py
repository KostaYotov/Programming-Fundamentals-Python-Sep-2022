number = int (input())

for i in range (1, number+1):
    for j in range(i):
        print("*", end = "")
    print()
for i in range ( number-1, 0, -1):
    for j in range(i):
        print("*", end = "")
    print()
# for i in range ( number-2, -1, -1):
#     for j in range(i,-1,-1):
#         print("*", end = "")
#     print()
