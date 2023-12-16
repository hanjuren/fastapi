# FastAPI

![](https://img.shields.io/badge/python-ffffff?style=for-the-badge&logo=python)
![](https://img.shields.io/badge/fastapi-ffffff?style=for-the-badge&logo=fastapi)
![](https://img.shields.io/badge/pytest-ffffff?style=for-the-badge&logo=pytest)
![](https://img.shields.io/badge/nginx-ffffff?style=for-the-badge&logo=nginx&logoColor=black)
![](https://img.shields.io/badge/docker-ffffff?style=for-the-badge&logo=docker)
![](https://img.shields.io/badge/postgresql-ffffff?style=for-the-badge&logo=postgresql)
![](https://img.shields.io/badge/sqlalchemy-ffffff?style=for-the-badge&logo=sqlalchemy&logoColor=black)
![](https://img.shields.io/badge/swagger-ffffff?style=for-the-badge&logo=swagger)
![](https://img.shields.io/badge/github-ffffff?style=for-the-badge&logo=github&logoColor=black)




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