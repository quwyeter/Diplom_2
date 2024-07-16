import requests
from data import Data
import allure


@allure.step('Создание пользователя')
def create_user(payload):
    return requests.post(Data.URL + Data.CREATE_USER, json=payload)


@allure.step('Логин пользователя')
def login_user(payload):
    return requests.post(Data.URL + Data.LOGIN, json=payload)


@allure.step('Изменение данных пользователя')
def change_user_data(payload, token):
    header = {"Authorization": token}
    return requests.patch(Data.URL + Data.USER_DATA, json=payload, headers=header)


@allure.step('Создание заказа')
def create_order(ingredients, token):
    ingredients = {"ingredients": ingredients}
    header = {"Authorization": token}
    return requests.post(Data.URL + Data.ORDERS, data=ingredients, headers=header)


@allure.step('Получение списка заказов пользователя')
def get_orders(token):
    header = {"Authorization": token}
    return requests.get(Data.URL + Data.ORDERS, headers=header)


@allure.step('Удаление пользователя')
def delete_user():
    requests.delete(Data.URL + Data.USER_DATA)
