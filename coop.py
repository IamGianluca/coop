import os
import requests
import sys


class Farmer(object):
    '''A hard-working farmer.'''

    CLIENT_ID = os.environ['COOP_CLIENT_ID']
    CLIENT_SECRET = os.environ['COOP_CLIENT_SECRET']
    TOKEN = os.environ['COOP_TOKEN']
    URL = 'http://coop.apps.knpuniversity.com'

    def __init__(self):
        pass

    def feed_chicken(self):
        suffix = '/api/{USER_ID}/chickens-feed'.format(USER_ID=1133)
        url = ''.join([self.URL, suffix])
        headers = {
            'Host': 'coop.apps.knpuniversity.com',
            'Authorization': 'Bearer {token}'.format(token=self.TOKEN)
        }
        response = requests.post(url, headers=headers)
        print(response.text)

    def collect_eggs(self):
        pass

    def count_eggs(self):
        pass

def main():
    luca = Farmer()
    luca.feed_chicken()

if __name__ == "__main__":
    sys.exit(main())
