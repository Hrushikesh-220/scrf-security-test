from sqlalchemy import text

# INTENTIONALLY VULNERABLE - FOR STATIC SECURITY SCANNING ONLY
# Do not execute or deploy this module.

def find_user(connection, username):
    query = text(
        "SELECT * FROM users WHERE name = '" + username + "'"
    )
    return connection.execute(query)

def calculate(expression):
    return eval(expression)
