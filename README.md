# FastAPI

![](https://img.shields.io/badge/python-DCDCDC?style=for-the-badge&logo=python)
![](https://img.shields.io/badge/fastapi-DCDCDC?style=for-the-badge&logo=fastapi)
![](https://img.shields.io/badge/pytest-DCDCDC?style=for-the-badge&logo=pytest)
![](https://img.shields.io/badge/nginx-DCDCDC?style=for-the-badge&logo=nginx&logoColor=black)
![](https://img.shields.io/badge/docker-DCDCDC?style=for-the-badge&logo=docker)
![](https://img.shields.io/badge/postgresql-DCDCDC?style=for-the-badge&logo=postgresql)
![](https://img.shields.io/badge/sqlalchemy-DCDCDC?style=for-the-badge&logo=sqlalchemy&logoColor=black)
![](https://img.shields.io/badge/swagger-DCDCDC?style=for-the-badge&logo=swagger)
![](https://img.shields.io/badge/github-DCDCDC?style=for-the-badge&logo=github&logoColor=black)




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