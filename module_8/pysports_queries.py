# Lanedra Moore
# July 20, 2023
# CYBR410 Data/Database Security
# Pysports Query: Creating a program that queries a mysql database

import mysql.connector
from mysql.connector import errorcode

#The information needed to access the database
config = {
    "user": "pysports_user1",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#attempting to access the database
try:
    db = mysql.connector.connect(**config)

    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    #SQL Statement and adding it to the cursor
    sqlQuery = """SELECT * FROM team;"""
    cursor = db.cursor()
    cursor.execute(sqlQuery)

    #make a list of teams
    teams = cursor.fetchall()

    #Display teams
    print("\n--  DISPLAYING TEAM RECORDS --")
    for team in teams:
        print("Team ID: {}".format(team[0]))
        print("Team Name: {}".format(team[1]))
        print("Mascot: {}".format(team[2]))
        print()

    
    sqlQuery = """SELECT * FROM player;"""
    cursor.execute(sqlQuery)

    #make a list of players
    players = cursor.fetchall()

    #Display players
    print("\n -- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team ID: {}".format(player[3]))
        print()


    input("\n\n   Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")
    
    else:
        print(err)

finally:
    db.close()