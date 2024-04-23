from atf.ui import *


class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] input', 'Логин')
    password = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__password"] input', 'Пароль')

    def auth(self, login: str, password: str):
        """Авторизация"""

        self.browser.open(self.config.get('SITE_TASK'))
        self.login.type_in(login + Keys.ENTER)
        self.login.should_be(ExactText(login))
        self.password.type_in(password + Keys.ENTER)
