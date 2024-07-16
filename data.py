class Data:
    URL = 'https://stellarburgers.nomoreparties.site/'

    CREATE_USER = 'api/auth/register'
    LOGIN = 'api/auth/login'
    USER_DATA = 'api/auth/user'
    ORDERS = 'api/orders'

    MESSAGE_INCORRECT_LOGIN_OR_PASSWORD = "email or password are incorrect"
    MESSAGE_WITHOUT_AUTHORIZATION = "You should be authorised"
    MESSAGE_EMAIL_EXISTS = "User with such email already exists"

    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    SERVER_ERROR = 500

    INGREDIENTS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]
