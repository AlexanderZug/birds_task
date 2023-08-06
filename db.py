from pony.orm import Database, PrimaryKey, Required

db = Database(provider="sqlite", filename="bird_database.sqlite", create_db=True)


class Bird(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    color = Required(str)


db.generate_mapping(create_tables=True)
