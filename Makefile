up:  ## Run Docker Compose services
	docker-compose -f docker-compose.yml up

runserver:  ## Run Docker Compose services
	uvicorn src.main:app --reload

create-migration:
	alembic -c src/alembic.ini revision --autogenerate -m $(name)

migrate:
	alembic -c src/alembic.ini upgrade head
