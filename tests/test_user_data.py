from api_method import change_user_data
from api_method import create_user
from data import Data
from generator import generate_data
import allure


class TestUserData:
    @allure.title('Тест изменения данных пользователя с авторизацией')
    def test_change_user_data_with_authorization(self):
        payload = generate_data()
        user = create_user(payload)
        token = user.json()['accessToken']
        payload['email'] = f'new{payload["email"]}'
        response = change_user_data(payload, token)

        assert response.status_code == Data.OK and response.json()['success'] == True

    @allure.title('Тест изменения данных пользователя без авторизации')
    def test_change_user_data_without_authorization(self):
        payload = generate_data()
        payload['email'] = f'new{payload["email"]}'
        response = change_user_data(payload, token=None)

        assert response.status_code == Data.UNAUTHORIZED and response.json()['success'] == False
