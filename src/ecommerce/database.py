from typing import Optional


class Database:
    """The Database Implementation"""

    def __init__(self, connection: Optional[str] = None) -> None:
        """Create a connection to a database"""
        pass

db: Optional[str] = None

def initialise_database(connection: Optional[str] = None) -> None:
    global db
    db = Database(connection)

# Alternaive implementation
def get_database(connection: Optional[str] = None) -> Database:
    global db
    if not db:
        db = Database(connection)
    return db