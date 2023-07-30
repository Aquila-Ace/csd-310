# pysports_update_and_delete.py
# By: Alex Bailey
# July 29, 2023
# Code for Updating, Deleting, and Displaying Inner Joining Table Information

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



# Creating recurring function for displaying records
# Multi-Parameter Function format from Jenny Palomino and Leah Wasser
# at URL: https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/functions-modular-code/write-functions-with-multiple-and-optional-parameters-in-python/
def main(cursor, display):

# Inner Join Query format as provided by Professor Haas
# at URL: https://cyberactive.bellevue.edu/ultra/courses/_518940_1/cl/outline
# Multi-Line string format from AlixaProDev
# at URL:  https://sparkbyexamples.com/python/python-create-a-long-multi-line-string/
    cursor = db.cursor()
    cursor.execute("""
                   SELECT player_id, first_name, last_name, team_name
                   FROM player
                   INNER JOIN team
                   ON player.team_id = team.team_id""")

# Pull and begin to print results
    players = cursor.fetchall()

# Format() function formatting from W3 Schools
# at URL: https://www.w3schools.com/python/ref_string_format.asp
    print("\n  -- {} --".format(display))
    
# Multi-line printing format from BowlOfRed
# at URL: https://discuss.python.org/t/pythonic-way-of-printing-multi-line-strings/19681
    for player in players: 
        print("Player ID {}"
              "\nFirst Name: {}"
              "\nLast Name: {}"
              "\nTeam Name: {}\n"
              .format(player[0],player[1],player[2],player[3]))
        


# Attempting to connect with MySQL using Try-Block.
try:
    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

# INSERT player(s) INTO player, UPDATE player, and DELETE player with formats provided by Professor Haas
# at URL: https://cyberactive.bellevue.edu/ultra/courses/_518940_1/cl/outline
    add_player = ("""INSERT INTO player(first_name, last_name, team_id)
                 VALUES('Smeagol', 'Shire Folk', 1)""")
    cursor.execute(add_player)
    db.commit()

# Display records after INSERT INTO using main()
    main(cursor, "DISPLAYING PLAYERS AFTER INSERT")

# UPDATE player
    update_player = ("""UPDATE player
                     SET team_id = 2,
                     first_name = 'Gollum',
                     last_name = 'Ring Stealer'
                     WHERE first_name = 'Smeagol'""")
    cursor.execute(update_player)
    db.commit()

# Display records after UPDATE using main() 
    main(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

# DELETE player(s) to ensure removal
    delete_player2= ("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute(delete_player2)
    db.commit()

# Display records after DELETE using main()
    main(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n Press any key to continue...")

# Same error notations if code fails as previous files
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist") 

    else:
        print(err)
        
finally:
    db.close()
