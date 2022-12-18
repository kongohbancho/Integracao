import mysql.connector
from mysql.connector import Error
import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = 100
pd.options.display.width = 500



def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
        )
        print("MySQL Server connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def read_query_index(connection, query,x):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchone()[x]
        return result
    except Error as err:
        print(f"Error: '{err}'")


def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

connection = create_server_connection("localhost", "root", "Matheus2000!")

connection = create_db_connection("localhost", "root", "Matheus2000!", "library")



#q1 = """SELECT * FROM book"""

#results = read_query(connection,q1)
#for result in results:
    #print(result)



while True:
    connection.reconnect()
    branch = 4
    q_check_borrow = """CALL check_borrow();"""
    q_block_user = """CALL block_user();"""
    execute_query(connection, q_check_borrow)
    execute_query(connection, q_block_user)



    try:
        option = int(input("""
        SELECT OPTION:
        
        1- Lists
        2- Search
        3- Loan Book
        4- Return Book
        5- Manage User Account
        6- Manage Books
        
        """))

        if option == 1:
            q1 = """SELECT loan.start_date, loan.due_date, loan.book, book.book_name, loan.user 
                    FROM loan 
                    JOIN book
                    ON loan.book = book.book_id"""
            q2 = """SELECT * FROM book"""
            q3 = """SELECT * FROM user"""
            q4 = """SELECT * FROM worker"""
            q5 = """SELECT * FROM branch"""
            q6 = """SELECT * FROM author """
            q7 = """SELECT * FROM publisher"""
            q8 = """SELECT * FROM job"""

            option_list = int(input("""
            SELECT OPTION: 
            
            1- Loan List
            2- Book List
            3- User List
            4- Worker List
            5- Branch List
            6- Author List
            7- Publisher List
            8- Job List
            
            """))

            if option_list == 1:
                from_db = []
                results = read_query(connection, q1)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Start Date", "Due Date", "Book ID", "Book Name", "User ID"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
                Press Any Key
                """)
            elif option_list == 2:
                from_db = []
                results = read_query(connection, q2)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Book ID", "Book Name", "Genre", "Branch ID", "Author", "Publisher ID"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
                Press Any Key
                """)
            elif option_list == 3:
                from_db = []
                results = read_query(connection, q3)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["User ID", "First Name", "Last Name", "Contact", "Books Borrowed", "Address", "Late"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
                Press Any Key
                """)
            elif option_list == 4:
                from_db = []
                results = read_query(connection, q4)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Worker ID", "First Name", "Last Name", "Contact", "job", "Weekly Hours", "Address"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
                Press Any Key
                """)
            elif option_list == 5:
                from_db = []
                results = read_query(connection, q5)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Branch ID", "Address", "Name"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
                Press Any Key
                """)
            elif option_list == 6:
                from_db = []
                results = read_query(connection, q6)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Author ID", "Name"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
                Press Any Key
                """)
            elif option_list == 7:
                from_db = []
                results = read_query(connection, q7)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Publisher ID", "Name", "Contact"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
                Press Any Key
                """)
            elif option_list == 8:
                from_db = []
                results = read_query(connection, q8)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Worker ID", "Branch ID"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
                Press Any Key
                """)
            else:
                print("Escolha Um Numero Valido")

        elif option == 2:
            option_2 = int(input(""" 
            SELECT OPTION: 
            
            1- Search Book
            2- Search User
            3- Search Worker
            4- Search Publisher
            5- Search Loans
            6- Search Author
            
            """))

            if option_2 == 1:
                search = input("""
                Search: """)
                q1 = f"""CALL search_book("{search}");"""
                from_db = []
                results = read_query(connection, q1)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Book Id", "Name", "Genre", "Author", "Branch", "Branch Address"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
    
                Press any key
    
                """)
            elif option_2 == 2:
                search = input("""
                Search: """)
                q1 = f"""CALL search_user("{search}");"""
                from_db = []
                results = read_query(connection, q1)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["User ID", "First Name", "Last Name", "Contact", "Books Borrowed", "Address", "Late"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
    
                Press any key
    
                """)
            elif option_2 == 3:
                search = input("""
                Search: """)
                q1 = f"""CALL search_worker("{search}");"""
                from_db = []
                results = read_query(connection, q1)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["First Name", "Last Name", "Workplace", "Job", "Contact", "Address", "ID"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
                
                Press any key
                
                """)
            elif option_2 == 4:
                search = input("""
                Search: """)
                q1 = f"""CALL search_publisher("{search}");"""
                from_db = []
                results = read_query(connection, q1)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Publisher ID", "Name", "Contact"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
    
                Press any key
    
                """)
            elif option_2 == 5:
                search = input("""
                Search: """)
                q1 = f"""CALL search_loan("{search}");"""
                from_db = []
                results = read_query(connection, q1)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Loan ID", "Start Date", "Due Date", "Book Name", "Book ID", "Last Name", "User ID"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
    
                Press any key
    
                """)
            elif option_2 == 6:
                search = input("""
                Search: """)
                q1 = f"""CALL search_author("{search}");"""
                from_db = []
                results = read_query(connection, q1)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Author ID", "Name"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input("""
    
                Press any key
    
                """)

            else:
                print("Escolha Um Numero Valido")

        elif option == 3:
            book_id = int(input("""Book ID: """))
            user_id = int(input("""User ID: """))
            q01 = f"""SELECT COUNT(book_id) from book WHERE book_id = {book_id};"""
            q02 = f"""SELECT late FROM user WHERE user_id = {user_id};"""
            q03 = f"""SELECT COUNT(user_id) from user WHERE user_id = {user_id};"""
            q1 = f"""CALL add_loan1({user_id},{book_id});"""
            q2 = """SELECT book.book_name, user, start_date, due_date  FROM loan
                     JOIN book
                     ON loan.book = book.book_id;"""

            results2 = read_query_index(connection, q01, 0)
            book_check = int(results2)
            results3 = read_query_index(connection, q03, 0)
            user_check = int(results3)
            if user_check == 0:
                print("No User With This ID")
                input("""Press Any Key""")

            elif book_check == 0:
                print("No Book With This ID")
                input("""Press Any Key""")

            else:
                results = read_query_index(connection, q02, 0)
                late_check = int(results)
                if late_check != 1:
                    execute_query(connection, q1)
                    from_db = []
                    results = read_query(connection, q2)
                    for result in results:
                        result = list(result)
                        from_db.append(result)
                    columns = ["Title", "User ID", "Borrow Date", "Due Date"]
                    df = pd.DataFrame(from_db, columns=columns)
                    print(df)
                    input(" Press Any Key ")
                else:
                    print("""Usuario em Situacao Irregular""")
                    input("""Press Any Key""")

        elif option == 4:
            book_id = int(input("""Book ID: """))
            q0 = f"""SELECT COUNT(book) from loan WHERE book = {book_id}"""
            q1 = f"""CALL return_book({book_id},{branch});"""
            q2 = """SELECT book.book_name, user, start_date, due_date  FROM loan
                    JOIN book
                    ON loan.book = book.book_id;"""
            results = read_query_index(connection, q0, 0)
            book_check = int(results)
            if book_check == 1:
                execute_query(connection, q1)
                from_db = []
                results = read_query(connection, q2)
                for result in results:
                    result = list(result)
                    from_db.append(result)
                columns = ["Title", "User Name", "Borrow Date", "Due Date"]
                df = pd.DataFrame(from_db, columns=columns)
                print(df)
                input(" Press Any Key ")
            else:
                print("Book Is Not Loaned")
                input(" Press Any Key ")

        elif option == 5:
            option_5 = int(input("""
            SELECT OPTION:
            
            1 - Add User
            2 - Remove User
            3 - Update User
            
            """))

            if option_5 == 1:
                user_borrow_number = 0
                user_late = 0
                user_user_id = 0
                user_firstname = input("First Name: ")
                user_lastname = input("Last Name: ")
                user_contact = input("Contact Information: ")
                user_address = input("Address: ")
                q1 = f"""INSERT INTO user VALUES 
                        ({user_user_id}, "{user_firstname}", "{user_lastname}", "{user_contact}", {user_borrow_number},
                        "{user_address}", {user_late});
                        """
                execute_query(connection, q1)
                input("Press Any Key")

            elif option_5 == 2:
                user_user_id = input("User ID to be Deleted:")
                q1 = f"""DELETE FROM user WHERE user_id = {user_user_id};"""
                execute_query(connection, q1)
                input("Press Any Key")

            elif option_5 == 3:
                user_user_id = int(input("User ID: "))
                option_5_1 = input("""
                What Column Should Change?
                * first_name
                * last_name
                * address
                * contact
                """)
                new_value = input("New Value: ")
                q1 = f"""UPDATE user SET {option_5_1} = "{new_value}" WHERE user_id = {user_user_id}"""
                execute_query(connection, q1)
                input("Press Any Key")

            else:
                print("Escolha Um Numero Valido")
                input("Press Any Key")

        elif option == 6:
            option_6_1 = int(input("""
                    SELECT OPTION:
    
                    1 - Add Book
                    2 - Remove Book
    
                    """))

            if option_6_1 == 1:
                book_book_id = 0
                book_name = input("Book Name: ")
                genre = input("Genre: ")
                author_id = int(input("Author ID: "))
                publisher_id = int(input("Publisher ID:"))
                q1 = f"""INSERT INTO book VALUES 
                                    ({book_book_id}, "{book_name}", "{genre}", {branch}, {author_id},
                                    {publisher_id});
                                    """
                execute_query(connection, q1)
                input("Press Any Key")

            elif option_6_1 == 2:
                book_book_id = input("Book ID to be Deleted:")
                q1 = f"""DELETE FROM book WHERE book_id = {book_book_id};"""
                execute_query(connection, q1)
                input("Press Any Key")

            else:
                print("Escolha Um Numero Valido")
                input("Press Any Key")

        else:
            print("Escolha Um Numero Valido")

    except ValueError:
        print("Choose A Valid Number")
