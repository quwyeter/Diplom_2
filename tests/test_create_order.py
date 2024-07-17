from api_method import create_order
from api_method import create_user
from api_method import get_orders
from data import Data
from generator import generate_data
import allure


class TestCreateOrder:
    @allure.title('Тест создания заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth_and_ingredients(self):
        payload = generate_data()
        user = create_user(payload)
        token = user.json()["accessToken"]
        ingredients = Data.INGREDIENTS
        order = create_order(ingredients, token)

        assert order.status_code == Data.OK and order.json()['success'] == True

    @allure.title('Тест создания заказа без авторизации с ингредиентами')
    def test_order_without_auth_and_with_ingredients(self):
        ingredients = Data.INGREDIENTS
        order = create_order(ingredients, token=None)

        assert order.status_code == Data.OK and order.json()['success'] == True

    @allure.title('Тест создания заказа с авторизацией без ингредиентов')
    def test_order_with_auth_and_without_ingredients(self):
        payload = generate_data()
        user = create_user(payload)
        token = user.json()["accessToken"]
        order = create_order(ingredients=None, token=token)

        assert order.status_code == Data.BAD_REQUEST

    @allure.title('Тест создания заказа с неверным хешем ингредиентов')
    def test_order_with_invalid_hash_ingredients(self):
        ingredients = ["123", "321"]
        order = create_order(ingredients, token=None)

        assert order.status_code == Data.SERVER_ERROR

    @allure.title('Тест получения списка заказов с авторизацией')
    def test_get_orders_with_auth(self):
        payload = generate_data()
        user = create_user(payload)
        token = user.json()["accessToken"]
        ingredients = Data.INGREDIENTS
        create_order(ingredients, token)
        order = get_orders(token)

        assert order.status_code == Data.OK and order.json()['success'] == True

    @allure.title('Тест получения списка заказов без авторизации')
    def test_get_orders_without_auth(self):
        order = get_orders(token=None)

        assert order.status_code == Data.UNAUTHORIZED
