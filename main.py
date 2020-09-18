# Ken Holm
# Purpose: This is my CRUD test program
# Create
# Read
# Update
# Delete
#
# See https://pymysql.readthedocs.io/en/latest/index.html
#  We need to install the mypysql library
#  In the Terminal window (bottom of PyCharm), run
#  pip3 install pymysql

import pymysql.cursors
from creds import *

def showData():
    # Our sql statement, easy to read
    sqlSelect = """
      select
        *
      from
        employees;
      """

    # Execute select
    cursor.execute(sqlSelect)

    # Loop through all the results
    #  Print the data, nicely
    for row in cursor:
        print(row)

    input("Press [ENTER] to continue. ")


# Connect to the database
try:
    myConnection = pymysql.connect(host=hostname,
                                   user=username,
                                   password=password,
                                   db=database,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()
    exit()

# Now that we are connected, execute a query
#  and do something with the result set.
try:
    with myConnection.cursor() as cursor:
        # ==================
        # Show initial data
        print(f"Initial Data")
        showData()

        # NOTE: We are using placeholders in our SQL statement
        #  See https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
        sqlInsert = """
            insert into
              employees (id, first_name, last_name, username)
            values
              (%s, %s, %s, %s);
            """

        sqlUpdate = """
            update
              employees
            set
              first_name = %s
            where
              id = %s;
            """

        sqlDelete = """
            delete from
              employees
            where
              id = %s;
            """
        # ===============
        # Execute insert
        print(f"Inserting data")
        cursor.execute(sqlInsert, (9999, 'Ken', 'Holm', 'kholm'))

        print(f"We have executed the INSERT statement")
        print(f"Does the data exist outside of this program?")
        showData()

        # Now, we have to COMMIT our command
        myConnection.commit()

        print(f"We have now committed the data")
        print(f"What about now?")
        showData()

        # ===============
        # Execute update
        print(f"Updating data")
        cursor.execute(sqlUpdate, ('Alex', 9999))

        # Now, we have to COMMIT our command
        myConnection.commit()

        showData()

        # ===============
        # Execute delete
        print(f"Delete data")
        cursor.execute(sqlDelete, (9999))

        # Now, we have to COMMIT our command
        myConnection.commit()

        showData()

# If there is an exception, show what that is
except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()

# Close connection
finally:
    myConnection.close()
    print("Connection closed.")
