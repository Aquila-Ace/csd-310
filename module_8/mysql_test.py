#As provided by Professor Haas at URL: https://cyberactive.bellevue.edu/ultra/courses/_518940_1/cl/outline
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "Aquila001!",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MysSQL host {} with database {}".format(config["host"], config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username are invalid")

    elif err.errno == errorcode.ER_BAD_DB_Error:
        print(' The specified database does not exist')

    else:
        print(err)
    
    #finally:
        db.close()
