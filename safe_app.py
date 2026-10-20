from sqlalchemy import text

def find_user(connection, username):
    query = text("SELECT * FROM users WHERE name = :name")
    return connection.execute(query, {"name": username})

def calculate_sum(a, b):
    return a + b
