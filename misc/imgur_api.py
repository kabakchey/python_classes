import os

from pprint import pprint as pp
from imgurpython import ImgurClient


# ----------------------------------------------------------------------------------------------------------------
IMGUR_CLIENT_ID = os.environ.get('IMGUR_CLIENT_ID')
IMGUR_CLIENT_SECRET = os.environ.get('IMGUR_CLIENT_SECRET')


# ----------------------------------------------------------------------------------------------------------------
def demo_imgur():
    client = ImgurClient(IMGUR_CLIENT_ID,
                         IMGUR_CLIENT_SECRET)

    response = client.upload_from_path('/home/dbhost/Desktop/Screenshot_2018-02-11_05-52-08.png')

    pp(response)


# ----------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    demo_imgur()
