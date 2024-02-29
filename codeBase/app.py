from flask import Flask, request
from flask_restful import Resource, Api
from connection import graph_db_driver
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class Home(Resource):
    
    def get(self):
        with graph_db_driver.session() as session:
            result = session.run("MATCH (n) RETURN n")
            print(result)
        return "Hello World"


class Course(Resource):

    def get(self):
        """
        To get all Course available
        It works when the database is on and connected!
        ---
        responses:
          200:
            description: A Course List of all available courses.

        """
        try:
            with graph_db_driver.session() as session:
                results = session.run("MATCH (course:COURSE) return course.name")
                all_course = results.values()
                all_course = [i[0] for i in all_course]
                return {"courses":all_course}, 200
        except Exception as err:
            return {"Message" : f"the error is {str(err)}"}, 400

    def post(self):

        """
        This will post a new record if not available
        It works and doesnt work it depends
        ---
        parameters:
          - in: formData
            name: course
            type: string
            required: true
        responses:
          200:
            description: A single user item
        """
        try:
            course = request.form.get("course")
            all_course = []
            with graph_db_driver.session() as session:
                results = session.run("MATCH (course:COURSE) return course.name")
                all_course = results.values()
                all_course = [i[0] for i in all_course]
                if course in all_course:
                    return {"Message" : f"{course} already exists"}, 403
                else:
                    query = "CREATE (:COURSE {name : $course, max_grade : 4})"
                    session.run(query, course = course)
                    return {"Message": f"{course} added succesfully"}, 200

        except Exception as err:
            return {"Message" : f"the error is {str(err)}"}, 400


class Student(Resource):

    def get(self):
        """
        To get all Students available
        It works when the database is on and connected!
        ---
        responses:
          200:
            description: A Course List of all available courses.

        """
        try:
            with graph_db_driver.session() as session:
                results = session.run("MATCH (student:STUDENT) return student.name")
                all_course = results.values()
                all_course = [i[0] for i in all_course]
                return {"students":all_course}, 200
        except Exception as err:
            return {"Message" : f"the error is {str(err)}"}, 400

    def post(self):
        """
        This will post a new record if not available
        It works and doesnt work it depends
        ---
        parameters:
          - in: formData
            name: student
            type: string
            required: true
        responses:
          200:
            description: A single user item
        """
        try:
            student = request.form.get("student")
            all_course = []
            with graph_db_driver.session() as session:
                results = session.run("MATCH (student:STUDENT) return student.name")
                all_course = results.values()
                all_course = [i[0] for i in all_course]
                if student in all_course:
                    return {"Message" : f"{student} already exists"}, 403
                else:
                    query = "CREATE (:STUDENT {name : $student, max_grade : 4})"
                    session.run(query, student = student)
                    return {"Message": f"{student} added succesfully"}, 200

        except Exception as err:
            return {"Message" : f"the error is {str(err)}"}, 400


class Subject(Resource):

    def get(self):
        """
        To get all subjects available
        It works when the database is on and connected!
        ---
        responses:
          200:
            description: A Course List of all available courses.

        """
        try:
            with graph_db_driver.session() as session:
                results = session.run("MATCH (subject:SUBJECT) return subject.name")
                all_course = results.values()
                all_course = [i[0] for i in all_course]
                return {"subjects":all_course}, 200
        except Exception as err:
            return {"Message" : f"the error is {str(err)}"}, 400

    def post(self):
        """
        This will post a new record if not available
        It works and doesnt work it depends
        ---
        parameters:
          - in: formData
            name: subject
            type: string
            required: true
        responses:
          200:
            description: A single user item
        """
        try:
            subject = request.form.get("subject")
            all_course = []
            with graph_db_driver.session() as session:
                results = session.run("MATCH (subject:SUBJECT) return subject.name")
                all_course = results.values()
                all_course = [i[0] for i in all_course]
                if subject in all_course:
                    return {"Message" : f"{subject} already exists"}, 403
                else:
                    query = "CREATE (:SUBJECT {name : $subject, max_grade : 4})"
                    session.run(query, subject = subject)
                    return {"Message": f"{subject} added succesfully"}, 200

        except Exception as err:
            return {"Message" : f"the error is {str(err)}"}, 400


api.add_resource(Home, "/")
api.add_resource(Course, "/course")
api.add_resource(Student, "/student")
api.add_resource(Subject, "/subject")

if __name__ == '__main__':
    app.run(debug = True, port = 5001)