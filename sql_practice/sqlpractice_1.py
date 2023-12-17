import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successfully connected...")
    print("#" * 30)

    try:

        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users` (`id` int(11) NOT NULL AUTO_INCREMENT," \
        #                           "`email` varchar(255) COLLATE utf8_bin NOT NULL," \
        #                           "`password` varchar(255) COLLATE utf8_bin NOT NULL," \
        #                           "PRIMARY KEY (`id`));"
        #     cursor.execute(create_table_query)
        #     print("It's okayy")

        # добавление нового поля
        # with connection.cursor() as cursor:
        #     create_new_column = "ALTER TABLE users ADD COLUMN name varchar(32);"
        #     cursor.execute(create_new_column)
        #     print("Success")

        # добавление данных
        # with connection.cursor() as cursor:
        #     insert_query = ("INSERT INTO `users` (name, password, email) VALUES ('Ari',"\
        #                     "  'iqueen', 'arikim@gmail.com');")
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print("Data was successfully added")
        #
        # with connection.cursor() as cursor:
        #     insert_query = ("INSERT INTO `users` (name, password, email) VALUES ('Victor',"\
        #                     "  'imglad', 'vicki@gmail.com');")
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print("Data was successfully added")
        #
        # with connection.cursor() as cursor:
        #     insert_query = ("INSERT INTO `users` (name, password, email) VALUES ('God',"\
        #                     "  'powerfull', 'godreallycool@gmail.com');")
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print("Data was successfully added")

        # обновление данных
        # with connection.cursor() as cursor:
        #     new_data = "UPDATE `users` SET password = 'trickyqueen' WHERE id=1;"
        #     cursor.execute(new_data)
        #     connection.commit()

        # удаление данных
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `users` WHERE id IN (5, 6, 7, 8, 9);"
        #     # для удаления одной строки надо  использовать id = int;
        #     cursor.execute(delete_query)
        #     connection.commit()

        # сбор данных
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `users`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("#" * 30)

        # удаление таблицы
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `users`;"
        #     cursor.execute(drop_table_query)

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)
