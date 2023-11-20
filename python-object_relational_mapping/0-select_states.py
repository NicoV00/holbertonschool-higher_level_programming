#!/usr/bin/python3
# gets all states


if __name__ == '__main__':
    import sys
    import MySQLdb
    try:
        # Database connection
        db_connection = MySQLdb.connect(
            "localhost",
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
    except MySQLdb.OperationalError:
        print("Can't connect to database")
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    db_connection.close()
