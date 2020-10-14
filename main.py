from flask import Flask
from flask_restful import Api, Resource, reqparse

# Initializing and wrapping our app into an API
app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=str, help="Likes of the video is required", required=True)

videos = {}


class HelloWorld(Resource):
    def get(self):
        return {"data": "Posted"}

    def post(self, name, test):
        return  {"data": name, "test": test}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201


api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")
api.add_resource(Video, "/video/<int:video_id>")

# DON'T run debug in "PRODUCTION"
if __name__ == "__main__":
    app.run(debug=True)
