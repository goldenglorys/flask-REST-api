from flask import Flask
from flask_restful import Api, Resource

# Initializing and wrapping our app into an API
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}


api.add_resource(HelloWorld, "/helloworld")

# DON'T run debug in "PRODUCTION"
if __name__ == "__main__":
    app.run(debug=True)
