#!/usr/bin/python3
"""Script that retrieves data from the 'states' table."""


if __name__ == "__main__":
    """Main function."""
    import sys
    import MySQLdb
    # Trying to connect
    try:
        db_connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    # If not succesfull
    except MySQLdb.OperationalError:
        print("Can't connect to the database")
        sys.exit(1)

    # Cursor Object For Query Execution
    cursor = db_connection.cursor()

    # Execute Query
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id"
    )

    # Fetch Data
    states = cursor.fetchall()

    # Prints result
    for state in states:
        print(state)

    # Close Database Connection
    db_connection.close()
