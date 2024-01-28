import mysql.connector 

class Books:
    def __init__(self) -> None:
        self.choise_databse = 'None'
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='muhammadzohid2007@',
        )
        self.cursor = self.db.cursor()  # Kursorni klass qisminida e'lon qilamiz
    
    def ShowDB(self):
        self.cursor.execute('SHOW DATABASES')  # Kursorni ishlatish
        databases = self.cursor.fetchall()  # fetchall() metodini to'liq foydalanish
        self.new_database = list()
        for db in databases:
            word = ''
            for i in db:
                word += i
            self.new_database.append(word)
        for i in self.new_database:
            print(i)
    
    def useDataBase(self,database_name):
        self.cursor.execute('SHOW DATABASES')  # Kursorni ishlatish
        databases = self.cursor.fetchall()  # fetchall() metodini to'liq foydalanish
        self.new_database = list()
        for db in databases:
            word = ''
            for i in db:
                word += i
            self.new_database.append(word)
        if database_name in self.new_database:
            self.cursor.execute(f"use {database_name}")
            print(f"DataBase tanlandi.Siz {database_name} DataBase sidasiz.")
            self.choise_databse = database_name
        else:
            print("Bunaqa DataBase mavjud emas.")
    

    def ShowTables(self):
        if self.choise_databse != 'None':
            self.cursor.execute('show tables;')
            table = self.cursor.fetchall()
            self.tables = list()
            for i in table:
                word = ''
                for j in i:
                    word += j
                self.tables.append(word)
                print(word)
        else:
            print("Siz oldin biror bir DataBasening tanlang.")
            
    def ChoiseDatabase(self):
        if self.choise_databse == 'None':
            return 'Siz hech qanaqa DataBase tanlamagansiz.'
        else:
            return f"Siz {self.choise_databse}ni tanlagansiz."
    
    def ShowTableElements(self):
        if self.choise_databse != 'None':
            input_tables = input("Table nomini kiriting: ")
            self.cursor.execute('show tables;')
            table = self.cursor.fetchall()
            self.tables = list()
            for i in table:
                word = ''
                for j in i:
                    word += j
                self.tables.append(word)
            if input_tables in self.tables:
                self.cursor.execute(f"select * from {input_tables};")
                date = self.cursor.fetchall()
                for i in date:
                    word = '';lst = []
                    if len(i) <= 1:
                        for j in i:
                            word += j
                        print(i)
                    else:
                        for k in list(i):
                            lst.append(k)
                        for h in lst:
                            print(h,end="   ")
                        print()
            else:
                print(f'{input_tables} nomli table mavjud emas.')
        else:
            print("Siz DataBase tanlamagansiz.")
    def addTableElement(self):
        if self.choise_databse != 'None':
            input_tables = input("Table nomini kiriting: ")
            self.cursor.execute('show tables;')
            table = self.cursor.fetchall()
            self.tables = list()
            for i in table:
                word = ''
                for j in i:
                    word += j
                self.tables.append(word)
            if input_tables in self.tables:
                self.cursor.execute(f'desc {input_tables};')
                columns = self.cursor.fetchall()
                lst = []
                for i in columns:
                    word = ''.join(tuple(i[0]))
                    word += '-'
                    word += ''.join(tuple(i[1]))
                    lst.append(word)
                for i in lst:
                    print(f"{i.split('-')[0]}-ga ",end="")
                    print(f"{i.split('-')[1]} tipida ",end='')
                print('qiymat beriladi.')
                
                query = ''
                for j in range(len(lst)):
                        query += input(f"{lst[j].split('-')[0]}ga {lst[j].split('-')[1]} tipida qiymat kiriting: ")
                        query += ','
                new_query = '';text_true = 0
                for i in range(len(lst)):
                    if lst[i].split('-')[1] == 'int' or lst[i].split("-")[1] == 'serial':
                        for j in query.split(',')[i]:
                            if not j.isdigit():
                               return f"{query.split(',')[i]}ga int tipida qiymat bermagansiz."
                    elif lst[i].split('-')[1] == 'text' or 'varchar' in lst[i].split("-")[1]:
                        for h in query.split(",")[i]:
                            if  h.isdigit():
                                text_true += 0
                            else:
                                text_true += 1
                        if text_true == 0:
                            return f"{query.split(',')[i]}ga text tipida qiymat bermagansiz."   
                count = 0           
                if len(lst) != 0:
                    for i in query.split(","):
                        if lst[count].split("-")[1] == 'int' or lst[count].split("-")[1] == 'serial':
                            new_query += i
                            if count + 1 != len(lst):
                                new_query += ','
                        elif lst[count].split("-")[1] == 'text' or 'varchar' in lst[count]:
                            new_query += "'";new_query += i;new_query += "'"
                            if count + 1 != len(lst):
                                new_query += ','
                        count += 1
                        if count == len(lst):
                            break
                print(new_query)
                self.cursor.execute(f"insert into {input_tables} values({new_query});")
                self.db.commit()
                return f"Siz {input_tables}ga qiymat kiritdingiz."
            else:   
                return f"{input_tables} nomli table mavjud emas."
        else:
            return "Siz DateBase tanlamagansiz."

    def CreateDataBase(self):
        self.cursor.execute('show databases;')
        dbs = self.cursor.fetchall()
        dbs_lst = []
        for i in dbs:
            for j in tuple(i):
                dbs_lst.append(i[0])
        input_databases = input("Yaratmoqchi bolgan DataBase nomini kiriting: ")
        if input_databases not in dbs_lst:
            self.cursor.execute(f"create database {input_databases};")
            return f"{input_databases} nomli DataBase yaratildi."
        else:
            return f"{input_databases} nomli DataBase mavjud."

    def DropDateBase(self):
        self.cursor.execute('show databases;')
        dbs = self.cursor.fetchall()
        dbs_lst = []
        for i in dbs:
            for j in tuple(i):
                dbs_lst.append(i[0])
        input_databases = input("Ochirmoqchi bolgan DataBaseni kiriting: ")
        if input_databases in dbs_lst:
            self.cursor.execute(f"drop database {input_databases};")
            return f"{input_databases} nomli DateBase yaratildi."
        else:
            return f"{input_databases} nomli DateBase mavjud emas."

    def CreateTable(self):
        if self.choise_databse != 'None':
            self.cursor.execute('show tables;')
            tbs = self.cursor.fetchall()
            tbs_lst = []
            for i in tbs:
                for j in tuple(i):
                    tbs_lst.append(i[0])
            input_tables = input("Yaratmoqchi bolgan Table nomini kiriting: ")
            if input_tables not in tbs_lst:
                while True:
                    print(f"{input_tables} nomli table yaratilmoqda.")
                    print("1.Oddiy Table     2.Primary key    3.Exit")
                    choise = int(input(">>> "));create_columns = [];column = ''
                    if choise == 1:
                        for i in range(int(input('Nechta column yaratmoqchisiz: '))):
                            while True:
                                new_col = input("Yaratmoqchi bolgan column nomini kiriting: ")
                                if new_col not in create_columns:
                                    create_columns.append(new_col);column += new_col;column += ' '
                                    break
                                else:
                                    print("Bunaqa column mavjud.")

                            while True:
                                col_type = input("Column uchun biror bir type tanlang: Masalan: int,text,varchar,boolean: ")
                                if col_type.lower() == 'varchar':
                                    while True:
                                        varchar_choise = input("Bu columnda maximum nechta element bolishi kerak: ")
                                        if varchar_choise.isdigit():
                                            column += f'varchar({varchar_choise})'
                                            column += ','
                                            break
                                        else:
                                            print("Bu yerga faqat son kiritishingiz zarur.")
                                    break
                                elif col_type.lower() == 'text' or col_type.lower() == 'int' or col_type.lower() == 'boolean':
                                    column += col_type.lower();column += ','
                                    break
                                elif col_type.lower() == 'exit':
                                    return "Table yaratilmadi."
                                else:
                                    print("Siz no togri malumot kiritdingiz.Tugatish uchun Exit kiriting: ")
                        column = column[:-1:]
                        self.cursor.execute(f"create table {input_tables}({column});")
                        self.db.commit()
                        return f"{input_tables} nomli table yaratildi."
                    elif choise == 2:
                        column = '';col_lst = [];end_col = '';fore_col = ''
                        for i in range(int(input("Nechta column yaratmoqchisiz: "))):
                            while True:
                                col_name = input("Column nomini kiriting: ")
                                if col_name not in col_lst and col_name.isalpha():
                                    column += col_name;column += ' ';end_col == col_name
                                    break
                                else:
                                    print("Bunaqa column mavjud.")
                            end = 0
                            while True:
                                if end > 0:
                                    break
                                col_type = input("Columnga biror bir type tanlang: M.n  int,text,varchar,boolean,serial,primary key,foreign key: ")
                                if col_type.lower() == 'varchar':
                                    while True:
                                        varchar_numb = input("Varcharda maximum nechta qiymat bolishi kerak: ")
                                        if varchar_numb.isdigit():
                                            column += f'varchar({varchar_numb})'
                                            column += ',';break
                                        else:
                                            print("Varchar faqat raqam qabul qiladi.")
                                    break
                                elif col_type.lower() == 'text' or col_type.lower() == 'int' or col_type.lower() == 'boolean' or col_type.lower() == 'serial':
                                    column += col_type.lower()
                                    column += ',';break
                                elif col_type.lower() == 'primary key':
                                    while True:
                                        pri_type = input("Primary key uchun type tanlang: M.n int,varchar,serial: ")
                                        if pri_type.lower() == 'int' or pri_type.lower() == 'serial':
                                            column += f"{pri_type.lower()} primary key,";end += 1
                                            break
                                        elif pri_type.lower() == 'varchar':
                                            while True:
                                                var_numb = input("Varcharga maximum nechta element kiritish kerak: ")
                                                if var_numb.isdigit():
                                                    column += f"{pri_type.lower()}({var_numb}),"
                                                    end += 1
                                                    break
                                                else:
                                                    print("Varchar faqat raqam qabul qiladi.")
                                            break
                                        else:
                                            print("Bunaqa type mavjud emas.")
                                elif col_type.lower() == 'foreign key':
                                    while True:
                                        pri_type = input("Foreign key uchun type tanlang: M.n int,serial: ")
                                        if pri_type.lower() == 'int' or pri_type.lower() == 'serial':
                                            search_table = input('Qaysi tablega ulamoqchisiz: ')
                                            self.cursor.execute('show tables;')
                                            tbs = self.cursor.fetchall()
                                            tbs_lst = []
                                            for i in tbs:
                                                for j in tuple(i):
                                                    tbs_lst.append(i[0])
                                            if search_table in tbs_lst:
                                                self.cursor.execute(f"desc {search_table};")
                                                search_table_col = self.cursor.fetchall();pri_lst = []
                                                for i in search_table_col:
                                                    if 'PRI' in  i and (tuple(i)[1] == 'int' or tuple(i)[1] == 'serial') :
                                                        pri_lst.append(tuple(i)[0])
                                                if len(pri_lst) == 0:
                                                    return f"Kechirasiz, ammo {search_table} tableda primary key mavjud emas ekan."
                                                elif len(pri_lst) == 1:
                                                    print(f"Siz faqatgina {pri_lst[0]} nomli columnga ulay olasiz.")
                                                    sorov = input(f"Siz {search_table}ning {pri_lst[0]} columniga ulashni hohlaysizmi: ha yoki yuq: ")
                                                    if sorov.lower() == 'ha':
                                                        column += f"{pri_type.lower()},"
                                                        fore_col += f"foreign key({col_name.lower()}) references {search_table}({pri_lst[0]}),"
                                                        end += 1
                                                        break
                                                    else:
                                                        return f"Table yaratilmadi."
                                                elif len(pri_lst) > 1:
                                                    print(f"Siz {search_table} tablening ",end="")
                                                    for x in pri_lst:
                                                        print(x,end="")
                                                    print(" nomli columnlariga ulay olasiz.")
                                                    sorov = input("Qaysi columnga ulamoqchisiz: ")
                                                    if sorov.lower() in pri_lst:
                                                        column += f"{col_type.lower()},"
                                                        fore_col += f"foreign key({pri_type.lower()}) references {search_table}({sorov.lower()}),"
                                                        end += 1
                                                        break
                                                    else:
                                                        return f"{sorov} bunaqa column topilmadi."
                                            else:
                                                return f"{search_table} nomli table mavjud emas.Table yaratilmadi."
                                        else:
                                            print("Bunaqa type mavjud emas.")
                                elif col_type.lower() == 'exit':
                                    return f"Table yaratilish toxtatildi."
                                else:
                                    print("Bunaqa type mavjud emas.Chiqish uchun exit.")
                        column += fore_col
                        column = column[:-1:]
                        self.cursor.execute(f"create table {input_tables}({column});")
                        self.db.commit()
                        return f"{input_tables} nomli table yaratildi."
                    elif choise == 3:
                        return 'Table yaratilmadi.'
                    else:
                        print("Siz no togri tanlov qildingiz.")
            else:
                return f"Bunaqa Table mavjud."    
        else:
            return f"Siz oldin DateBase tanlamagansiz."


user = Books()
while True:
    print("""1. DataBaselarni ko'rish     2.DataBase tanlash.
3.DataBase yaratish     4.DataBaseni ochirish
5.Tanlangan Databse     6.Tablelarni kurish.
7.Tabledagi malumotlar.  8.Tablega malumot qoshish.
9.Table yaratish        10.Tableni ochirish""")
    a = int(input(">>> "))
    # if a == 1:
    #     user.ShowDB()
    # elif a == 2:
    #     user.useDataBase(input('DataBase nomini kiriting: '))
    # elif a == 3:
    #     print(user.ChoiseDatabase())
    # elif a == 4:
    #     user.ShowTables()
    # elif a == 5:
    #     user.ShowTableElements()
    # elif a == 6:
    #     print(user.addTableElement())
    # elif a == 7:
    #     print(user.CreateDataBase())
    if a == 1:
        user.ShowDB()
    elif a == 2:
        user.useDataBase(input('DataBase nomini kiriting: '))
    elif a == 3:
        print(user.CreateDataBase())
    elif a == 4:
        print(user.DropDateBase())
    elif a == 5:
        print(user.ChoiseDatabase())
    elif a == 6:
        user.ShowTables()
    elif a == 7:
        user.ShowTableElements()
    elif a == 8:
        print(user.addTableElement())
    elif a == 9:
        print(user.CreateTable())
