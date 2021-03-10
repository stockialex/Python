import requests
import json

class User:
    def __init__(self, t = 0, tr = 0):
        self.token = t
        self.token_refresh = tr
        self.token_url = 'https://api.invertironline.com/token'

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token):
        self.__token = token

    @property
    def token_refresh(self):
        return self.__token
    
    @token_refresh.setter
    def token_refresh(self, token_refresh):
        self.__token_refresh = token_refresh
    
usuario = User(10)
usuario.token = 15
print(usuario.token)

