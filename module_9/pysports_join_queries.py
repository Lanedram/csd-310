# Lanedra Moore
# July 30, 2023
# CYBR410
# Program to make a inner join query connecting player and team

#Link to Github Repository: https://github.com/Lanedram/csd-310.git

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
    sqlQuery = """SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;"""
    cursor = db.cursor()
    cursor.execute(sqlQuery)

    #make a list of teams
    players = cursor.fetchall()

    #Display players
    print("\n-- DISPLAYING PLAYER RECORDS --")
  
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