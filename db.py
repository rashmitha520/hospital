import sqlite3
# Retrieving data from the database
def get_patient():
    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `Patient`")
    results = cursor.fetchall()
    conn.close()
    return results
data = get_patient()

print(data)