#!/usr/bin/python3
"""Script that retrieves data from the 'states' table."""

if __name__ == "__main__":
    """Main function."""
    import MySQLdb
    import sys

    # MySQL connection parameters
    user_name = sys.argv[1]
    user_passw = sys.argv[2]
    db_name = sys.argv[3]

    # Connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=user_passw,
        db=db_name
    )

    # Cursor to execute SQL queries
    cur = db.cursor()

    # Execute query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Results
    states = cur.fetchall()

    # Print data
    for state in states:
        print(state)

    # Close the database connection
    db.close()
