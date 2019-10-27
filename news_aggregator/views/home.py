from typing import Dict, Optional

import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template('home.html')
async def get_home(request: web.Request) -> Optional[Dict[str, str]]:
    return None
