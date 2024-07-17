# Diplom_2
# Тестирование API сервиса Stellar Burgers
### Структура проекта:

- Файл data.py, в котором содержится инфомация о запросах
- Файл generator.py, в котором содержится метод генерации данных
- Файл api_method, в котором содержатся методы запросов
- Директория tests, в которой содержатся файлы с тестами: 
  - test_create_user.py — тест создания пользователя
    - ручка `api/auth/register`
  - test_login_courier.py — тест логина пользователя
    - ручка `api/auth/login`
  - test_create_order.py — тест создания заказа
    - ручка `api/orders`
  - tests_user_data — тест изменения данных пользователя
    - ручка `api/auth/user`