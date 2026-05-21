import sqlite3

# 1. Connect to an in-memory database and create a cursor
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# 2. Create a sample table
cursor.execute(
    """
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    grade TEXT
)
"""
)

# 3. Insert sample data (including duplicate departments for DISTINCT)
sample_data = [
    (1, "Alice Smith", "Computer Science", "A"),
    (2, "Bob Jones", "Data Science", "B"),
    (3, "Charlie Brown", "Computer Science", "A"),
    (4, "David Miller", "Mathematics", "A"),
    (5, "Eva Green", "Data Science", "C"),
    (6, "Frank Smith", "Physics", "B"),
]
cursor.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?)", sample_data
)
conn.commit()

# 4. Query: Combine DISTINCT, LIKE, filtering, and sorting
# Goal: Find unique departments where a student's last name or first name starts with 'A' or contains 'Science', sorted alphabetically.
query = """
SELECT DISTINCT department 
FROM students 
WHERE department LIKE '%Science%' 
ORDER BY department ASC;
"""

# Execute and fetch results
cursor.execute(query)
results = cursor.fetchall()

# 5. Print the results
print("Filtered, Distinct, and Sorted Departments:")
for row in results:
    print(f"- {row[0]}")

# Close connection
conn.close()
