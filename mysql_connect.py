# import mysql.connector

# try:
#     db = mysql.connector.connect(
#         host = "localhost",
#         user = "your username", # root
#         password= "your password",
#         database= "db_name"
#     )
#     if db.is_connected():
#         print("ulanish muvaffaqiyatli amalga oshdi")
#     cursor= db.cursor()
#     sql = "INSERT INTO users (name, task_count) VALUES (%s, %s)"
#     val = ("coder", 4)

#     cursor.execute(sql,val)
#     db.commit()
#     print(f"{cursor.rowcount} ta malumot push")

# except mysql.connector.Error as err:
#     print(f"Xatolik yuz berdi: {err}")


# finally:
#     if 'db' in locals() and db.is_connected():
#         db.close()
#         print("ulanish yopildi")

