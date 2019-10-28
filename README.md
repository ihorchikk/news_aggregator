# news_aggregator

___

## Requirements
- docker-compose

___

## Features

- aiohttp
- pytest
- flake8
- trafaret
- docker-compose
- aio devtools
- aiohttp debug toolbar
- postgres
- alembic
- aiopg
- sqlAlchemy


## Local development
All develop settings for application are in the `/config/api.dev.yml`.

### Run
To start the project in develop mode, run the following command:

```
make run
```

or just

```
make
```

For stop work of docker containers use:

```
make stop
```

For clean up work of docker containers use:

```
make clean
```

Interactive work inside container

```
make bash # the command must be running after `make run` 
```

### Upgrade
To upgrade dependencies:

```
make upgrade
```

### Docs

For generate sphinx docs
```
make doc
```

### Linters
To run flake8, run the following command:

```
make lint
```

The all settings connected with a `flake8` you can customize in `.flake8`.

___


### Database
Management of database (postgres) migrations takes place with the help of [alembic](http://alembic.zzzcomputing.com/en/latest/).

Create new migration (new file in `news_aggregator/migrations/versions/`):

```
make migrations # the command must be running after `make run` 
```

Apply migrations:

```
make migrate # the command must be running after `make run` 
```

To connect to postgres, use the command below

```
make psql # the command must be running after `make run` 
```

## Software

- python3.7
