
from data import Data
from generator import generate_data
from api_method import create_user
from api_method import delete_user
import pytest
import allure


class TestCreateUser:
    @allure.title('Тест создания уникального пользователя')
    def test_create_user_successful(self):
        payload = generate_data()
        response = create_user(payload)
        delete_user()

        assert (response.status_code == Data.OK and response.json()["success"] == True)

    @allure.title('Тест создания пользователя с некорректной почтой')
    @pytest.mark.parametrize('email', ['', '123'])
    def test_create_user_with_incorrect_email(self, email):
        payload = generate_data()
        response = create_user(payload={
            'email': email,
            'password': payload['password'],
            'name': payload['name']
        })
        delete_user()

        assert (response.status_code == Data.FORBIDDEN and response.json()["success"] == False)

    @allure.title('Тест создания пользователя без пароля')
    def test_create_user_without_password(self):
        payload = generate_data()
        response = create_user(payload={
            'email': payload['email'],
            'password': '',
            'name': payload['name']
        })
        delete_user()

        assert (response.status_code == Data.FORBIDDEN and response.json()["success"] == False)



    @allure.title('Тест создания уже зарегистрированного пользователя')
    def test_create_duplicate_user(self):
        payload = generate_data()
        create_user(payload)
        response = create_user(payload)

        assert (response.status_code == Data.FORBIDDEN and response.json()["success"] == False)
