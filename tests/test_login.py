from api_method import create_user
from api_method import delete_user
from api_method import login_user
from data import Data
from generator import generate_data
import allure


class TestLogin:
    @allure.title('Тест логина под существующим пользователем')
    def test_log_in_successful(self):
        payload = generate_data()
        create_user(payload)
        response = login_user(payload)
        delete_user()

        assert (response.status_code == Data.OK and response.json()["success"] == True)

    @allure.title('Тест логина с неверным логином и паролем')
    def test_invalid_login(self):
        response = login_user(payload={
            'email': '123',
            'password': '123'
        })

        assert (response.status_code == Data.UNAUTHORIZED and response.json()["success"] == False)
