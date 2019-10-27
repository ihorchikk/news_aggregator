PROJECT_NAME=news_aggregator

all: run

run:
	@docker-compose up $(PROJECT_NAME)_app

build:
	@docker-compose build $(PROJECT_NAME)_app

stop:
	@docker-compose stop

clean:
	@docker-compose down

bash:
	@docker exec -it $(PROJECT_NAME) bash

doc:
	@docker-compose run --rm $(PROJECT_NAME)_app make _doc

_doc:
	@doc8 docs
	@cd docs && make html

lint:
	@docker-compose run --rm $(PROJECT_NAME)_app flake8 $(PROJECT_NAME)

psql:
	@docker exec -it $(PROJECT_NAME)_postgres psql -U postgres

migrations:
	@docker exec -it $(PROJECT_NAME) alembic revision;
