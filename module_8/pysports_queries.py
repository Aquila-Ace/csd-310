# import, Config, and Try-Block as provided by Professor Haas
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

# Attempting to connect with MySQL.
try: 
    db = mysql.connector.connect(**config)

# Cursors and Formatting provided by Professor Haas
# at URL: https://cyberactive.bellevue.edu/ultra/courses/_518940_1/cl/outline
    cursor = db.cursor()
    print("--DISPLAYING TEAM RECORDS--")
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    teams = cursor.fetchall()

# Multi-line printing format from BowlOfRed
# at URL: https://discuss.python.org/t/pythonic-way-of-printing-multi-line-strings/19681
    for team in teams:
        print("Team ID: {}"
              "\nTeam Name: {}"
              "\nMascot: {}\n"
              .format(team[0],team[1],team[2]))
        
    cursor = db.cursor()
    print("\n--DISPLAYING PLAYER RECORDS--")
    cursor.execute("SELECT * FROM PLAYER")
    
    players = cursor.fetchall()
    
    for player in players: 
        print("Player ID {}"
              "\nFirst Name: {}"
              "\nLast Name: {}"
              "\nTeam ID: {}\n"
              .format(player[0],player[1],player[2],player[3]))
                   
    input("\n\n Press any key to continue...")

# Same error notations if code fails as previous file
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")    
    else:
        print(err)
        
finally:
    db.close()
