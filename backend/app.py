import datetime
import os

from flask import Flask, Response, request
from flask_mongoengine import MongoEngine

from database.db import initialize_db
from database.models import Student

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': os.environ['MONGODB_DBNAME'],
    'authentication_source': os.environ['MONGODB_AUTH_SOURCE'],
}

# app.config['MONGODB_SETTINGS'] = {
#         'DB': 'student-db',
#         'USERNAME': 'apiuser',
#         'PASSWORD': 'apipassword',
#         'HOST': 'localhost',
#         'PORT': 27017,
#         'authentication_source': 'student-db',
#     }

initialize_db(app)

@app.route("/api")
def index():
    Student.objects().delete()
    Student(
        sid = 1,
        full_name="Nguyen Duc Duong", 
        year_of_birth= 2000,
        university = "UET",
        major = "Computer science"
        ).save()
    students = Student.objects().to_json()
    return Response(students, mimetype="application/json", status=200)

if __name__ == "__main__":
    app.run(debug=True, port=5000)