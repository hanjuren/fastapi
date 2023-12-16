docker compose build fastapi

docker compose up -d database
docker compose up fastapi

docker exec -it fastapi bash
alembic revision --autogenerate -m ""
alembic upgrade head
alembic downgrade -1
