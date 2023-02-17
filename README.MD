# Приложение: сеть по продаже электроники

Приложение реализовано на Django с использованием PostgreSQL. Реализовано API для создания поставщиков и пользователей.
Панель администратора, где можно просмотреть поставщиков с их задолженностью. Настроен action для очистки задолеженности.
В списке поставщиков каждый элемент имеет ссылку на ссылающийся узел сети поставок.

## Сущности:
- Поставщик
- Пользователь
- Продукт

## Стек:
- Python 3.10
- Django 4.1.3
- REST Framework 3.14.0
- PosrgeSQL 13.0
- PyTest 7.2.0
- Djoser 2.1.0
- Docker 20.10

## Тесты:
1. Для поставщиков
2. Для пользователей
3. Для продуктов

## Запуск:
- git clone https://github.com/zamotaeff/nfse
- cd nfse
- python3 -m venv venv
- source venv/bin/activate
- pip3 install -r requirements.txt
- cd backend
- python3 manage.py migrate
- python3 manage.py runserver
- python3 manage.py createsuperuser

## Docker:
- git clone https://github.com/zamotaeff/nfse
- cd nfse
- docker-compose up

## Документация API:

Доступна по следующим адресам.

- http://127.0.0.1:8000/swagger/
- http://127.0.0.1:8000/redoc/