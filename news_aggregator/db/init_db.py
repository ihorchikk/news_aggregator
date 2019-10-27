from sqlalchemy import create_engine, MetaData
from werkzeug.security import generate_password_hash

from news_aggregator.db.enums import UserGender
from news_aggregator.db.tables import users
from news_aggregator.utils.common import get_config

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[users])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(users.insert(), [
        {'username': 'test',
         'email': 'test@test.com',
         'password':generate_password_hash('q1w2e3r4'),
         'avatar_url': 'http://example.com',
         'gender': UserGender.none}
    ])
    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**get_config()['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
