from flask import Flask
from flask_restful import Api, Resource

# Initializing and wrapping our app into an API
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Posted"}

    def post(self, name, test):
        return  {"data": name, "test": test}


api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

# DON'T run debug in "PRODUCTION"
if __name__ == "__main__":
    app.run(debug=True)
