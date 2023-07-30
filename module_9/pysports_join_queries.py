# pysports_join_queries.py
# Alex Bailey
# July 29, 2023
# Code for Inner Joining Tables

# Import, Config, and Full Try-Block as provided by Professor Haas
# at URL: https://cyberactive.bellevue.edu/ultra/courses/_518940_1/cl/outline
import mysql.connector
from mysql.connector import errorcode
# Configuring based on my system and my MySQL root access
config = {
    "user": "root",
    "password": "DarkHorse001!",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

# Attempting to connect with MySQL using Try-Block.
try: 
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

# Inner Join Query format as provided by Professor Haas
# at URL: https://cyberactive.bellevue.edu/ultra/courses/_518940_1/cl/outline
# Multi-Line string format from AlixaProDev
# at URL:  https://sparkbyexamples.com/python/python-create-a-long-multi-line-string/
    cursor.execute("""
                   SELECT player_id, first_name, last_name, team_name
                   FROM player
                   INNER JOIN team
                   ON player.team_id = team.team_id""")

# Pull and begin to print results
    players = cursor.fetchall()

    print("\n-- DISPLAYING PLAYER RECORDS --")

# Multi-line printing format from BowlOfRed
# at URL: https://discuss.python.org/t/pythonic-way-of-printing-multi-line-strings/19681
    for player in players: 
        print("Player ID {}"
              "\nFirst Name: {}"
              "\nLast Name: {}"
              "\nTeam ID: {}\n"
              .format(player[0],player[1],player[2],player[3]))

    input("\n\n Press any key to continue...")

# Same error notations if code fails as previous files
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist") 

    else:
        print(err)
        
finally:
    db.close()
