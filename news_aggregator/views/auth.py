from typing import Dict, Optional

import aiohttp_jinja2
from aiohttp import web

from news_aggregator.db.auth import check_credentials, register_user
from news_aggregator.db.enums import UserGender


@aiohttp_jinja2.template('home.html')
async def post_login(request: web.Request) -> Optional[Dict[str, str]]:
    data = await request.post()
    result = await check_credentials(db_engine=request.app['postgres'],
                                     email=data.get('email'),
                                     password=data.get('password'))

    return None


@aiohttp_jinja2.template('registration.html')
async def get_registration(request: web.Request):
    pass


async def post_registration(request: web.Request):
    data = await request.post()
    gender = UserGender.none
    gender_data = data.get('gender')
    if gender_data and gender_data != 'None':
        gender = UserGender.male if gender_data == 'Male' else UserGender.women
    res = await register_user(db_engine=request.app['postgres'],
                              username=data.get('username'),
                              password=data.get('password'),
                              email=data.get('email'),
                              gender=gender,
                              avatar_url=data.get('avatar_url'))
    if res:
        response = aiohttp_jinja2.render_template('home.html', request, context={'success_registration': True})
    else:
        response = aiohttp_jinja2.render_template('registration.html', request, context={'invalid_registration': True})
    return response
