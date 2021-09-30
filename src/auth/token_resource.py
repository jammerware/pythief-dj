from flask_restful import Resource, reqparse


class TokenResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        print('things', self.parser.parse_args())
