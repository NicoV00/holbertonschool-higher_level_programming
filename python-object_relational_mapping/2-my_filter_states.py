#!/usr/bin/python3
"""script that displays all values in the states table of hbtn_0e_0_usa where name matches the argument."""


if __name__ == "__main__":
    """Main function."""
    import sys
    import MySQLdb
    # Trying to connect
    try:
        db_connection = MySQLdb.connect(
            "localhost",
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
    # If not succesfull
    except MySQLdb.OperationalError:
        print("Can't connect to the database")

    # Cursor Object For Query Execution
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    fetchs = cursor.fetchall()
    for x in range(len(fetchs)):
        if fetchs[x][1] == sys.argv[4]:
            print("{}".format(fetchs[x]))

    db_connection.close()