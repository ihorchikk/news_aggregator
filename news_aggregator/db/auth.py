from aiohttp_security import AbstractAuthorizationPolicy
from sqlalchemy import select, insert
from werkzeug.security import check_password_hash, generate_password_hash

from news_aggregator.db.tables import users


async def check_credentials(db_engine, email, password):
    async with db_engine.acquire() as conn:
        query = select([users.c.email, users.c.password]).where(users.c.email == email)
        ret = await conn.execute(query)
        data = await ret.fetchone()
        if data:
            email_from_db, password_from_db = data['email'], data['password']
            if email_from_db is not None:
                return check_password_hash(password_from_db, password)
    return False


async def register_user(db_engine, email, username, password, avatar_url, gender):
    async with db_engine.acquire() as conn:
        query = users.insert().values(email=email,
                                      username=username,
                                      password=generate_password_hash(password),
                                      avatar_url=avatar_url,
                                      gender=gender)
        await conn.execute(query)
    return True
