import sqlite3
import re


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as error:
        print(error)

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def create_product(conn, product: tuple):
    try:
        sql = '''insert into products (product_title, price, quantity)
        values (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def update_quantity(conn, product: tuple):
    try:
        sql = '''update products set quantity = ? where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def update_price(conn, product: tuple):
    try:
        sql = '''update products set price = ? where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def delete_product(conn, id):
    try:
        sql = '''delete from products where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def all_products(conn):
    try:
        sql = '''select * from products
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def select_by_price_and_quantity(conn, limit):
    try:
        sql = '''select * from products where price < ? and quantity > ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def seek_by_word(conn, word):
    try:
        sql = '''select * from products where product_title like ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


database = r'hw.db'

sql_create_products_table = '''
create table products (
id integer primary key autoincrement,
product_title varchar(200) not null,
price  double(10, 2) not null default 0.0,
quantity integer(5) not null default 0
)
'''

connection = create_connection(database)
create_table(connection, sql_create_products_table)
create_product(connection, ('Кола', 76.5, 12))
create_product(connection, ('Хотдог', 95.89, 8))
create_product(connection, ('Щампунь детское', 99.25, 9))
create_product(connection, ('Вода негазированная', 22.15, 3))
create_product(connection, ('Вода со вкусом киви', 65.67, 12))
create_product(connection, ('Вода со вкусом ананаса', 76.99, 9))
create_product(connection, ('Шоколад', 110.34, 15))
create_product(connection, ('Шоколадное молоко', 109.58, 7))
create_product(connection, ('Печенье овсяные', 129.12, 15))
create_product(connection, ('Чипсы', 121.19, 11))
create_product(connection, ('Чипсы сырные', 123.79, 8))
create_product(connection, ('Конфета', 34.45, 17))
create_product(connection, ('Жвачка', 35.23, 10))
create_product(connection, ('Ручка синяя', 96.5, 6))
create_product(connection, ('Молоко', 97.1, 12))
update_quantity(connection, (13, 7))
update_price(connection, (33.33, 12))
delete_product(connection, 2)
all_products(connection)
select_by_price_and_quantity(connection, (100, 5))
seek_by_word(connection, 'Кола')

connection.close()