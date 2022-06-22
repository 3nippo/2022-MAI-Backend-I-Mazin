COMPOSE_SPEC = -f lab06/compose.yaml

up:
	docker-compose $(COMPOSE_SPEC) up -d

down:
	docker-compose $(COMPOSE_SPEC) down

migrate: up
	docker-compose $(COMPOSE_SPEC) exec ascapp python3.10 ./manage.py migrate

createsuperuser: up
	@echo "Create superuser for db"
	docker-compose $(COMPOSE_SPEC) exec ascapp python3.10 ./manage.py createsuperuser

create_secrets:
	@echo "Create secrets for db"
	/bin/bash -c "cd ./lab06 && /bin/bash ./setup_secrets.sh"

init: create_secrets migrate createsuperuser

all: up
