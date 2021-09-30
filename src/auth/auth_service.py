import os
from flask import Flask
from flask_restful import Api
from pymitter import EventEmitter
import requests
from auth.token_resource import TokenResource


class AuthService:
    port = 5012
    scope = 'https://www.googleapis.com/auth/youtube.readonly'

    def __init__(self):
        self._events = EventEmitter()

    @property
    def events(self): return self._events

    def start(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(TokenResource, '/token')
        self.app.run(port=AuthService.port, threaded=True)

        res = requests.post('https://accounts.google.com/o/oauth2/v2/auth', {
            'client_id': os.environ['YT_CLIENT_ID'],
            'redirect_uri': f'http://localhost:{AuthService.port}/token',
            'response_type': 'code',
            'scope': AuthService.scope,
        })

        print(res)
