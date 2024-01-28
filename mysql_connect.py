# import mysql.connector

# class MYSQL:
#     def __init__(self) -> None:
#         self.data_base = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'muhammadzohid2007@'
#     )
#         self.new()
        
#     def new(self):
#         self.data_base.cursor().execute("show database;")
#         print(self.data_base.cursor().fetchall())
# obj = MYSQL()