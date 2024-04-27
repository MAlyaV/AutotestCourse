from atf import *
from atf.ui import *


class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] input', 'Логин')
    password = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__password"] input', 'Пароль')

    def auth(self, login: str, password: str):
        """Авторизация
        :param login: Логин
        :param password: Пароль
        """

        info(f'Авторизуемся на онлайне под пользователем {login}')
        self.login.type_in(login + Keys.ENTER)
        self.login.should_be(ExactText(login))
        self.password.type_in(password + Keys.ENTER)
        self.password.should_not_be(Displayed, wait_time=True)
        self.check_page_load_wasaby()
