import mysql.connector


def get_db():
    """Kobler til MariaDB-databasen og returnerer tilkoblingen."""
    connection = mysql.connector.connect(
        host="localhost",
        user="flask",
        password="flask",  # Bytt til ditt MariaDB-passord
        database="flask_spilldb"
    )
    return connection
