import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from news_aggregator.migration import metadata
from news_aggregator.db.enums import UserGender


__all__ = ['users', 'gender_enum', ]


gender_enum = postgresql.ENUM(UserGender)


users = sa.Table(
    'users', metadata,
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column('username', sa.String(200), unique=True, nullable=False),
    sa.Column('email', sa.String(200), unique=True, nullable=False),
    sa.Column('password', sa.Text, nullable=False),
    sa.Column('avatar_url', sa.Text),
    sa.Column(
        'gender',
        gender_enum,
        server_default=UserGender.none.value,
    ),
)

