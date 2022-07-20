from playhouse.migrate import *
from app.dependencies import get_db

db = get_db()

migrator = PostgresqlMigrator(db)

if __name__ == "__main__":
    migrate(
        migrator.add_column('good', 'Fan')
    )