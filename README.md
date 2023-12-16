# FastAPI


### env setting
```shell
cp .env.sample .env
```

### docker build & run
```shell
docker compose build fastapi-server

docker compose up -d fastapi-db fastapi-server fastapi-nginx
```

### alembic migration
```shell
alembic upgrade head
```

### swagger
> http://localhost/docs  
> http://localhost/redoc