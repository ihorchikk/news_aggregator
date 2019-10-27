from pathlib import Path
from typing import Optional, List
from functools import partial

import aiohttp_jinja2
import aiopg.sa
from aiohttp import web
import aioredis
import jinja2
from aiohttp_security import setup as setup_security, SessionIdentityPolicy
from aiohttp_session import setup as setup_session
from aiohttp_session.redis_storage import RedisStorage
from aiopg.sa import create_engine
from aioredis import create_pool

from news_aggregator.routes import init_routes
from news_aggregator.utils.common import init_config


path = Path(__file__).parent


def init_jinja2(app: web.Application) -> None:
    """ Initialize jinja2 template for application.

    :param app:
    :return:
    """
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(str(path / 'templates'))
    )

async def database(app: web.Application) -> None:
    """ A function that, when the server is started, connects to postgresql,
    and after stopping it breaks the connection (after yield)

    :param app:
    :return:
    """
    config = app['config']['postgres']

    engine = await aiopg.sa.create_engine(**config)
    app['postgres'] = engine

    yield

    app['postgres'].close()
    await app['postgres'].wait_closed()


async def redis(app: web.Application) -> None:
    """A function that, when the server is started, connects to redis,
    and after stopping it breaks the connection (after yield)

    :param app:
    :return:
    """
    config = app['config']['redis']

    create_redis = partial(
        aioredis.create_redis,
        f'redis://{config["host"]}:{config["port"]}'
    )
    app['create_redis'] = await create_redis()

    yield

    app['create_redis'].close()
    await app['create_redis'].wait_closed()


def init_app(config: Optional[List[str]] = None) -> web.Application:
    app = web.Application()

    init_jinja2(app)
    init_config(app, config=config)
    init_routes(app)

    app.cleanup_ctx.extend([
        redis,
        database,
    ])

    return app


app = init_app()
