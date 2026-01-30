print("hello Linux")

'''user_age = int(input("how old are you : "))

if user_age > 18:
    print ("welcome to course")

elif user_age == 18:
    print("welcome")

else:
    print("you age smaler than 18 old")'''

''''lenguage_list = ["python","java","c++"]
for lang in lenguage_list:
    print( f"my fovourite language is " + lang)
'''


#for i in range(1, 11):
    #print (f"my number is " + str(i))


'''Write a script where:

    You have a variable called status_code.

    If it's 200, print "Success! Page loading..."

    If it's 404, print "Error: Page not found."

    If it's 500, print "Error: Server is down."

    Else (for any other number), print "Unknown status."'''

# The server status

'''server_status = 200  # Just a single number

if server_status == 200:
    print("Success! Page loading...")
elif server_status == 404: # Changed 400 to 404 to match your goal
    print("Error: Page not found")
elif server_status == 500:
    print("Error: Server is down")
else:
    print("Unknown status")'''

'''
# A dictionary maps a "Key" to a "Value"
responses = {
    200: "Success!",
    404: "Not Found",
    500: "Server Error"
}

print(responses[404]) # This prints: Not Found

'''


sonlar = [12, 34, 56, 45, 67, 23, 2, 78, 99, 21, 67, 99]
max_num1 = sonlar[0]
max_num2 = sonlar[-1]
'''for num in sonlar:
    if num > max_num:
        max_num = num
        
    
print(f"the big number is : {max_num}")'''


for num in sonlar:
    if num > max_num1:
        max_num2 = max_num1
        max_num1 = num
    elif num < max_num1 and num > max_num2:
        max_num2 = num

print(f"engkatta sonlar 1-si {max_num1},2-si {max_num2}")