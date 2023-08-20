import requests 
from . import instagram_config as conf

class InstagramUser(requests.Session):

    def login(self):
        landing_respond = self.get(url=conf.LANDING_INFO, date=conf.CREDENTIALS, headers=conf.LANDING_HEADERS)
        self.cookies = landing_respond.cookies
        login_respond = self.post(url=conf.LOGIN_AJAX, date=conf.CREDENTIALS)

        if login_respond.status == 'OK':
            print('logged in successfully!')
        else:
            print('Login Error')

    def logout(self):
        self.close()

    def find_user(self, user_id):
        return self.get(user_id)

