# РЕПОЗИТОРИЯ НАХОДИТЬСЯ НА ВЕТКЕ MASTER

### Установка
1. Clone the repo
```sh
git clone git_url
docker-compose build
docker-compose up -d
docker-compose exec -it djk-backend python manage.py migrate
docker-compose exec -it djk-backend python manage.py createsuperuser
```


### Если таблица базы-данных не поднимается? тогда вам чит-код (вниз).
```sh
docker exec -t djk-postgres pg_dump -U postgres parser_k > dump.sql
## clean db
docker exec -it djk-postgres psql -U postgres -c "DROP DATABASE IF EXISTS parser_k;"
docker exec -it djk-postgres psql -U postgres -c "CREATE DATABASE parser_k;"
## import db
docker cp /Users/max/Documents/1company/home/dev/dump.sql djk-postgres:/dump.sql
docker exec -i djk-postgres psql -U postgres -d parser_k < /home/max/Documents/2025/1company/dump.sql
```
