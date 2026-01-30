# Task 1
# import sys
# print(sys.version)
# python version

# Task 2
# if 5 > 2:
#  print("Five is greater than two!") 
# if 5 > 2:
#         print("Five is greater than two!") this is true

# print("Python is fun!") print("Really!") this error becouse ; not 
# print("Python is fun!"); print("Really!") this true because ; = next 

# print("Hello World!", end=" ")
# print("I will print on the same line.")

# print("I have big ", end="\n")  #end="\n" this is defoult
# print("House")


# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*" * i ,"*" * j)
#         print()
#     print()


# This is tree
# qator = int(input("tree qancha katta bulsin: "))
# for i in range(1, qator + 1):
#     for s in range(qator - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()

# for o in range(2):
#     for s in range(qator - 2):
#         print(" ", end="")
#     print("*" * (qator // 3))


qator = int(input("Archa qancha katta bo'lsin: "))

for i in range(1, qator + 1):
    for s in range(qator - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

oyoq_kengligi = qator // 3
if oyoq_kengligi % 2 == 0:
    oyoq_kengligi += 1

for o in range(qator // 4 + 1):
    for s in range(qator - (oyoq_kengligi // 2) - 1):
        print(" ", end="")
    print("*" * oyoq_kengligi)