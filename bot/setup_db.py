import psycopg2

# establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='password', host='database', port='5432'
)
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to create a database
sql = '''CREATE DATABASE ytb; GRANT ALL PRIVILEGES ON DATABASE ytb TO postgres;'''

# Creating a database
cursor.execute(sql)

print("Database ytb created successfully...")

# Closing the connection
conn.close()
