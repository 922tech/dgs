

CREDENTIALS = {
  "enc_password":"#PWD_INSTAGRAM_BROWSER:10:1692298165:ATRQAFT41Btkzo1y2O2HYIG0nmBmjmCYXEolHNIMpooDy85vHdA4sDqHaWQJm+ZJi0Qv2EZky4sPQuVnQ/SVnL1oOfltjBFbsluByNVasL55yHcgYyIzTF9Y0t+JLo9tIIf2UOUNr6+PDNotoA==",
  "optIntoOneTap":"false",
  "queryParams":"{}",
  "trustedDeviceRecords":"{}",
  "username":"martin_the_musican"
}


ACCOUNTS_LOGIN = 'https://www.instagram.com/accounts/login/'
LOGIN_PAGE = 'https://www.instagram.com/api/v1/web/login_page/'
LOGIN_AJAX = 'https://www.instagram.com/accounts/login/ajax/'
LANDING_INFO= 'https://www.instagram.com/api/v1/public/landing_info/'
land = 'https://www.instagram.com/ajax/qm/?__a=1&__user=0&__comet_req=7&jazoest=2970'
user = 'https://www.instagram.com/ajax/qm/?__a=1&__user=0&__comet_req=7&jazoest=2888'

USER_PAYLOAD = { #for user url payload
    '__a': '1',
    '__ccg': 'EXCELLENT',
    '__comet_req': '7',
    '__d': 'www',
    '__hs': '19587.HYP%3Ainstagram_web_pkg.2.1..0.0',
    '__hsi': '7268499759825335963',
    '__req': 'h',
    '__rev': '1008118991',
    '__s': '%3Aun2k1l%3Alhp3kc',
    '__spin_b': 'trunk',
    '__spin_r': '1008118991',
    '__spin_t': '1692329477',
    '__user': '0',
    'dpr': '1',
    'jazoest': '2990',
    'lsd': 'AVq6BXqBfzs',
    'ph': 'C3'
}


USER_HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,nl-BE;q=0.8,nl;q=0.7,fa-IR;q=0.6,fa;q=0.5",
    "content-length": "1071",
    "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryZc5fH3vHiR4cFm1P",
    "cookie": "mid=ZN5MHAALAAFY14wyAcs0sux7N4Xu; ig_did=DC34BAF1-180B-45D4-9497-86ACD711D00C; dpr=2; datr=AE_eZKy2aqiWCCr7UQ903hLv; shbid=\"4129\\05427025445571\\0541723828156:01f715689c3c50bd951393deb964aff53d41d7d5c816d9fc41ecf86179632d6150af501c\"; shbts=\"1692292156\\05427025445571\\0541723828156:01f7163ce5358cd4cca2c15b68ebc48634034786f820399c740630b7bd8c7a11bc670816\"; csrftoken=i21HH8bPft4IsdelDlJ2AXn8DbeDriVx",
    "dpr": "2",
    "origin": "https://www.instagram.com",
    "referer": "https://www.instagram.com/accounts/login/",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-full-version-list": "\"Not_A Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"109.0.5414.149\", \"Chromium\";v=\"109.0.5414.149\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-ch-ua-platform-version": "\"6.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
    "viewport-width": "513"
}
LOGIN_HEADERS = {
    # ":authority": "www.instagram.com",
    # ":method": "GET",
    # ":path": "/api/v1/web/login_page/",
    # ":scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,nl-BE;q=0.8,nl;q=0.7,fa-IR;q=0.6,fa;q=0.5",
    "dpr": "2",
    "referer": "https://www.instagram.com/accounts/login/",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-full-version-list": "\"Not_A Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"109.0.5414.149\", \"Chromium\";v=\"109.0.5414.149\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-ch-ua-platform-version": "\"6.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
    "viewport-width": "513",
    "x-asbd-id": "129477",
    "x-csrftoken": "QcWp0gBDpkgnyExSK5fzd0N4jDQXk9t3",
    "x-ig-app-id": "1217981644879628",
    "x-ig-www-claim": "0",
    "x-requested-with": "XMLHttpRequest",
    "x-web-device-id": "AF31860B-A56C-42ED-A668-445B1C29F171"
}

LANDING_HEADERS =  {
    "authority": "www.instagram.com",
    "method": "POST",
    "path": "/ajax/qm/?__a=1&__user=0&__comet_req=7&jazoest=2970",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,nl-BE;q=0.8,nl;q=0.7,fa-IR;q=0.6,fa;q=0.5",
    "content-length": "126",
    "content-type": "application/x-www-form-urlencoded",
    "dpr": "2",
    "origin": "https://www.instagram.com",
    "referer": "https://www.instagram.com/accounts/login/",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-full-version-list": "\"Not_A Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"109.0.5414.149\", \"Chromium\";v=\"109.0.5414.149\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-ch-ua-platform-version": "\"6.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
    "viewport-width": "513"
}


USER_AGENT = {
            'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
        }