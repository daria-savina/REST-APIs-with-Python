from flask import Flask,jsonify
from flask_restful import Api,Resource,reqparse


app = Flask(__name__)
api = Api()

tasks = {
    1: {"title": "Buy groceries"},
    2: {"title": "Learn Python"}
}

parser = reqparse.RequestParser()
parser.add_argument("title", location='form')

class Main(Resource):
    def get(self,task_id):
        if task_id == 0:
           return tasks
        else:
            return tasks[task_id]

    def delete(self, task_id):
        del tasks[task_id]
        return tasks

    def post(self,task_id):
        tasks[task_id]  = parser.parse_args()
        return tasks

    def put(self,course_id):
        tasks[task_id] = parser.parse_args()
        return tasks

api.add_resource(Main, "/api/tasks/<int:task_id>")
api.init_app((app))

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')

