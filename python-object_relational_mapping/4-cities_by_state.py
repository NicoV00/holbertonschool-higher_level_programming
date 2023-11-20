#!/usr/bin/python3
''' script that lists all cities from the database hbtn_0e_4_usaimport MySQLdb.'''
import sys
if __name__ == "__main__":
    """main function"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()

    cur.execute('''SELECT cities.id, cities.name, states.name
                FROM cities JOIN states
                ON state_id = states.id ORDER BY cities.id''')
    fetchs = cur.fetchall()
    for x in range(len(fetchs)):
        if fetchs[x][1] == sys.argv[4]:
            print("{}".format(fetchs[x]))

    db.close()
