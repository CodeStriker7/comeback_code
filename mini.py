# a = [1,2,3]
# #b = a.copy() 
# b= a[:]
# #b = list(a)
# a = [1,2,3,4,5]

# print(a)
# print(b)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = [x ** 2 for x in numbers if x % 2 == 0]
# print(result)

num1 = int(input("son kiriting: "))
num2 = int(input("son kiriting: "))
amal = input("amalni kiriting(/,*,-,+): ")


if amal == '/':
	natija = num1 / num2
elif amal == '*':
	natija = num1 * num2
elif amal == '-':
	natija = num1 - num2
elif amal == '+':
	natija = num1 + num2
else:
	print("Xato amal kiritildi")
print(natija)


