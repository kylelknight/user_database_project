import sqlite3

# Step 1: Connect to SQLite (or create a new database if it doesn't exist)
conn = sqlite3.connect("user_info.db")
cursor = conn.cursor()

# Step 2: Load and execute the SQL schema from the external file
with open("schema.sql", "r") as sql_file:
    cursor.executescript(sql_file.read())
print("Table created successfully using schema.sql.")

# Step 3: Insert some records
cursor.executemany("""
INSERT INTO users (name, email, age) VALUES (?, ?, ?)
""", [
    ("Alice", "alice@example.com", 25),
    ("Bob", "bob@example.com", 30),
    ("Charlie", "charlie@example.com", 22)
])
conn.commit()
print("Records inserted successfully.")

# Step 4: Query the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("User Data:")
for row in rows:
    print(row)

# Step 5: Close the connection
conn.close()
print("Database connection closed.")
