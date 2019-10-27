import pathlib

from aiohttp import web

from news_aggregator.views.home import get_home
from news_aggregator.views.auth import post_login, get_registration, post_registration

PROJECT_PATH = pathlib.Path(__file__).parent


def init_routes(app: web.Application) -> None:
    add_route = app.router.add_route

    add_route('GET', '/', get_home, name='home')

    add_route('POST', '/login', post_login, name='login_post')
    add_route('POST', '/invalid_login', post_login, name='invalid_login')

    add_route('GET', '/registration', get_registration, name='registration_get')
    add_route('POST', '/registration', post_registration, name='registration_post')

    add_route('POST', '/forgot_pass', get_home, name='forgot_pass_get')
    add_route('POST', '/forgot_pass', get_home, name='forgot_pass_post')

    add_route('GET', '/sources', get_home, name='sources')
    add_route('GET', '/about_us', get_home, name='about_us')
    add_route('POST', '/search', get_home, name='search')

    add_route('GET', '/news/travel', get_home, name='travel')
    add_route('GET', '/news/world', get_home, name='world')
    add_route('GET', '/news/politics', get_home, name='politics')
    add_route('GET', '/news/sport', get_home, name='sport')
    add_route('GET', '/news/literature', get_home, name='literature')

    # added static dir
    app.router.add_static('/static/', path=(PROJECT_PATH / 'static'), name='static')
