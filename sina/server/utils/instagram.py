import requests
from bs4 import BeautifulSoup as BS
import json
import re
from Kanashi.utility import String


def generate_password(password):
    p = "hex[b64]\"{}\"".format(String.encode(password))
    return p


def get_login_data(username='922tech@gmail.com', password='52075207#'):
    data = {
        "username": username,
        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(int(datetime.now().timestamp()), generate_password(password)),
        "queryParams": {},
        "optIntoOneTap": "false"
    }
    return data


class InstagramUser(requests.Session):

    def get_tokens(self):
        jar = self.get("https://www.instagram.com/accounts/login/", headers={"dpr": "1", "sec-ch-prefers-color-scheme": "light", "sec-ch-ua-full-version-list":
                       "\"Not_A Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"109.0.5414.149\", \"Chromium\";v=\"109.0.5414.149\"", "sec-ch-ua-platform-version": "\"6.0\"", "viewport-width": "636"}, cookies={"dpr": "2"})
        doc = BS(jar.text)
        tags = doc.find_all('script')
        tokens = json.loads(tags[28].text)
        s = str(tokens['require'][0][3])
        # s2 = str(tokens['require'][0])
        csrf_search = re.search(r'"csrf_token":"([A-Za-z0-9]+)"', s)
        xig_search = re.search(r'"X-IG-App-ID":"([A-Za-z0-9]+)"', str(tags))
        return {'X-IG-App-ID': xig_search.groups(1)[0], 'csrftoken': csrf_search.groups(1)[0]}

    def get_cookies(self):
        tokens = self.get_tokens()
        res = self.get("https://www.instagram.com/api/v1/web/data/shared_data/",
                       headers={
                           "dpr": "2", "sec-ch-prefers-color-scheme": "light",
                           "sec-ch-ua-full-version-list": "\"Not_A Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"109.0.5414.149\", \"Chromium\";v=\"109.0.5414.149\"",
                           "sec-ch-ua-platform-version": "\"6.0\"", "viewport-width": "636", "x-asbd-id": "129477",
                           "x-csrftoken": tokens['csrftoken'],
                           "x-ig-app-id": tokens['X-IG-App-ID'],
                           "x-ig-www-claim": "0",
                           "x-requested-with": "XMLHttpRequest",
                           "x-web-device-id": "19094CAA-9A4E-4AC2-957B-61753B59151D"
                       }
                       )
        # print(dict(self.cookies))
        return dict(res.cookies)

    def login(self, username, password):
        # tokens = get_tokens(self)
        cookies = self.get_cookies()
        login_result = self.post("https://www.instagram.com/api/v1/web/accounts/login/ajax/",
                                 data=get_login_data(username, password),
                                 headers={
                                     "dpr": "2", "sec-ch-prefers-color-scheme": "light",
                                     "sec-ch-ua-full-version-list": "\"Not_A Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"109.0.5414.149\", \"Chromium\";v=\"109.0.5414.149\"", "sec-ch-ua-platform-version": "\"6.0\"",
                                     "viewport-width": "495", "x-asbd-id": "129477",
                                     "x-csrftoken": cookies['csrftoken'], "x-ig-app-id": cookies['X-IG-App-ID'],
                                     "x-ig-www-claim": "0", "x-instagram-ajax": "1008155130",
                                     "x-requested-with": "XMLHttpRequest"}, cookies=cookies)
        return login_result

    def get_cookies(self):
        tokens = self.get_tokens()
        g = self.get("https://www.instagram.com/api/v1/web/data/shared_data/",
                     headers={"dpr": "2", "sec-ch-prefers-color-scheme": "light",
                              "sec-ch-ua-full-version-list": "\"Not_A Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"109.0.5414.149\", \"Chromium\";v=\"109.0.5414.149\"", "sec-ch-ua-platform-version": "\"6.0\"",
                              "viewport-width": "636", "x-asbd-id": "129477",
                              "x-csrftoken": tokens['csrftoken'],
                              "x-ig-app-id": tokens['X-IG-App-ID'],
                              "x-ig-www-claim": "0", "x-requested-with": "XMLHttpRequest",
                              "x-web-device-id": "19094CAA-9A4E-4AC2-957B-61753B59151D"})

        return {**dict(g.cookies), **tokens}

    def logout(self):
        self.close()

    def find_user(self, user_id):
        return self.get(user_id)
