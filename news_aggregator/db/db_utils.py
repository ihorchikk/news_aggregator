from aiopg.sa import SAConnection
from aiopg.sa.result import RowProxy

from news_aggregator.db.tables import users


__all__ = ['select_user_by_id', ]


async def select_user_by_id(conn: SAConnection, key: int) -> RowProxy:
    query = users.select().where(users.c.id == key).order_by(users.c.id)
    print(query)
    print(type(conn))
    cursor = await conn.execute(query)

    return await cursor.fetchone()
