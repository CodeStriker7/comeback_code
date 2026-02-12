word = {'bad','worse', 'well'}  # set
print(type(word))
for w in word:
	print(w, len(w))




users = {'Hans': 'active', 'Éléonore': 'active', '景太郎': 'inactive'}  # dict
print(type(users))

for user, status in users.copy().items():
	if status == "inactive":
		del users[user]
		print(users)


active_user = {}
for user, status in users.items():
	if status == 'active':
		active_user[user] = status
		print(active_user)

# range function
for i in range(2, 10):
	if i % 2 == 0:
		print('this num is even: ', i )
	else:
		print('this num is odd : ', i )
print('else change continue')
# else change continue
for i in range(2, 10):
	if i % 2 == 0:
		print('this num is even: ', i )
		continue
	print('this num is odd : ', i )


#2 
for n in range(2, 20):
	for x in range(2, n):
		if n % x == 0:
			print(f"{n} equal {x} *  {n // x}")
			break
	else:
		print( n, " is the prime number ")


# pass 
def future_funksion():
	pass

#def future():

# error becouse expected an indented block after function definition 
#pass: "Shunchaki o'tib ket va keyingi qatordan davom et".



print(my_function.__doc__)

#Function Annotations
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
# MYPY mypy day4.py  mypy error dastur.py:4: error: Incompatible return value type (got "str", expected "int")

def qo_shish(a, b):
    return a + b

# Bu qism faqat fayl bevosita ochilganda ishlaydi
if __name__ == "__main__":
    print("Test: 2 + 3 =", qo_shish(2, 3))

#boshqa faylda import qo_shish , u faqat funksiyani oladi
#lekin print qismini ishga tushirmaydi.becouse __name__ != main in another file