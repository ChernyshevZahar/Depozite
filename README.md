# Depozite

Приложение для работы с дипозитом клиента через апи

Для запуска проекта нужно:

docker-compose up --build

открываем новый терминал

docker-compose exec web bash
python manage.py migrate


Запросы апи
Для добавления 
POST "http://localhost:8000/api/v1/wallets/<WALLET_UUID>/operation"
{
operation_type: “DEPOSIT”
amount: 1000
}


Для вычетания
POST "http://localhost:8000/api/v1/wallets/<WALLET_UUID>/operation"
{
operation_type: “WITHDRAW” 
amount: 1000
}


Да вывода баланса

GET "http://localhost:8000/api/v1/wallets/{WALLET_UUID}"
