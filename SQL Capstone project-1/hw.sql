import sqlite3

# 1. Connect to an in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# 2. CREATE TABLE
cursor.execute(
    """
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER,
        subject TEXT
    )
"""
)

# 3. DATA MANIPULATION (Insert, Update, Delete)
# Insert data
students_data = [
    (1, "Alice", 85, "Math"),
    (2, "Bob", 92, "Science"),
    (3, "Charlie", 78, "Math"),
    (4, "Diana", 95, "Science"),
]
cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students_data)

# Update data
cursor.execute("UPDATE students SET grade = 80 WHERE name = 'Charlie'")

# Delete data
cursor.execute("DELETE FROM students WHERE id = 1")


# 4. FILTERING AND SORTING
# Filter for Science students and sort by grade in descending order
cursor.execute(
    """
    SELECT name, grade 
    FROM students 
    WHERE subject = 'Science' 
    ORDER BY grade DESC
"""
)

# Fetch and print results
results = cursor.fetchall()
print("Filtered & Sorted Results (Science Students):")
for row in results:
    print(f"Name: {row[0]}, Grade: {row[1]}")

# Close the connection
conn.close()
