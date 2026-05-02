import sqlite3

# Connect to an in-memory database
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

# 1. Create a table (DDL)
cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        price REAL,
        stock_count INTEGER
    )
""")

# 2. Insert data (DML)
data = [
    (1, 'Laptop', 'Electronics', 1200.00, 10),
    (2, 'Phone', 'Electronics', 800.00, 0),
    (3, 'Desk', 'Furniture', 150.00, 5),
    (4, 'Chair', 'Furniture', 85.00, 20),
    (5, 'Tablet', 'Electronics', 400.00, 15)
]
cursor.executemany("INSERT INTO products VALUES (?,?,?,?,?)", data)

# 3. Query using all major SQL operators
# Combined query demonstrating: LIKE, IN, BETWEEN, IS NOT, AND, OR, and Comparison
query = """
SELECT name, price 
FROM products 
WHERE (category IN ('Electronics', 'Furniture')   -- IN: Membership
    AND price BETWEEN 100 AND 1000)               -- BETWEEN: Range
    OR (name LIKE 'Lap%'                          -- LIKE: Pattern matching
    AND stock_count > 0                           -- >: Comparison
    AND stock_count != 0)                         -- !=: Comparison
    AND category IS NOT NULL                      -- IS NOT: Null check
ORDER BY price DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

# Display results
print("Matching Products:")
for row in results:
    print(f"Product: {row[0]}, Price: ${row[1]}")

connection.close()
