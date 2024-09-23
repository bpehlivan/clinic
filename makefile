db:
	docker-compose run --rm --service-ports -d database

up:
	docker-compose up

bash:
	docker-compose run --rm app bash

build:
	docker-compose build

down:
	docker-compose down --remove-orphans
