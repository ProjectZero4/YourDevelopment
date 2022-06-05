uid := $(shell id -u)
gid := $(shell id -g)
setup:
	cd .setup && docker compose up
	sudo chown $(uid):$(gid) -R .
start:
	docker compose up -d
stop:
	docker compose down
reset:
	make forget
	make setup
	make start

forget:
	make stop
	-@docker rm -f $(shell docker ps -a -q -f name=yd.)
	-@docker volume rm $(shell docker volume ls -q -f name=your_development_yd-)
	-@docker image rm $(shell docker image ls -q -f reference="your_development_yd*")
