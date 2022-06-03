setup:
	cd .setup && docker compose up
start:
	docker compose up -d
stop:
	docker compose down
