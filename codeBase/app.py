from flask import Flask, request
from flask_restful import Resource, Api
from connection import graph_db_driver
from flasgger import Swagger
import neo4j

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


class RelationShip(Resource):

    def get(self):
        """
        To get all  available realtionships
        It works when the database is on and connected!
        ---
        responses:
          200:
            description: to get all available relationships

        """
        try:
            with graph_db_driver.session() as session:
                results = session.run("MATCH ()-[r]->() RETURN DISTINCT type(r) AS RelationshipType")
                all_course = results.values()
                all_course = [i[0] for i in all_course]
                return {"realtionships":all_course}, 200
        except Exception as err:
            return {"Message" : f"the error is {str(err)}"}, 400

    def post(self):
        """
        This will post a new record if not available
        It works and doesnt work it depends
        ---
        parameters:
          - in: formData
            name: parent_node
            type: string
            required: true
          - in: formData
            name: child_node
            type: string
            required: true
          - in: formData
            name: realtionship_name
            type: string
            required: true
          - in: formData
            name: parent_filter_key
            type: string
            required: true
          - in: formData
            name: parent_filter_value
            type: string
            required: true
          - in: formData
            name: child_filter_key
            type: string
            required: true
          - in: formData
            name: child_filter_value
            type: string
            required: true
        responses:
          200:
            description: A single user item
        """
        node_1 = request.form.get("parent_node")
        node_2 = request.form.get("child_node")
        realtionship = request.form.get("realtionship_name")
        parent_node_filter_key = request.form.get("parent_filter_key")
        parent_node_filter_value = request.form.get("parent_filter_value")
        child_node_filter_key = request.form.get("child_filter_key")
        child_node_filter_value = request.form.get("child_filter_value")

        query = "MATCH (a:"+ node_1+" {" + parent_node_filter_key + " : $parent_node_filter_value}) - [x:"+  realtionship+"] -> (b:"+ node_2+" {" + child_node_filter_key + " : $child_node_filter_value}) return a,x,b"

        with graph_db_driver.session() as session:
            results = session.run(query, parent_node_filter_value = parent_node_filter_value, child_node_filter_value = child_node_filter_value)
            results = results.values()
            response = []
            for i in results:
                STRING = ""
                for j in i:
                    if isinstance(j, neo4j.graph.Node):
                        STRING += list(j.values())[0]
                    else:
                        STRING += "---- " + j.type + " ----"
                
                response.append(STRING)
            return {"Relationships" : response}, 200



class AddRelationShip(Resource):

    def post(self):
        """
        This will post a new record if not available
        It works and doesnt work it depends
        ---
        parameters:
          - in: formData
            name: parent_node
            type: string
            required: true
          - in: formData
            name: child_node
            type: string
            required: true
          - in: formData
            name: realtionship_name
            type: string
            required: true
          - in: formData
            name: parent_filter_key
            type: string
            required: true
          - in: formData
            name: parent_filter_value
            type: string
            required: true
          - in: formData
            name: child_filter_key
            type: string
            required: true
          - in: formData
            name: child_filter_value
            type: string
            required: true
        responses:
          200:
            description: A single user item
        """
        node_1 = request.form.get("parent_node")
        node_2 = request.form.get("child_node")
        realtionship = request.form.get("realtionship_name")
        parent_node_filter_key = request.form.get("parent_filter_key")
        parent_node_filter_value = request.form.get("parent_filter_value")
        child_node_filter_key = request.form.get("child_filter_key")
        child_node_filter_value = request.form.get("child_filter_value")

        query = "MATCH (a:"+ node_1+" {" + parent_node_filter_key + " : $parent_node_filter_value}) - [x:"+  realtionship+"] -> (b:"+ node_2+" {" + child_node_filter_key + " : $child_node_filter_value}) return a,x,b"
        with graph_db_driver.session() as session:
            results = session.run(query, parent_node_filter_value = parent_node_filter_value, child_node_filter_value = child_node_filter_value)
            results = results.values()
            if len(results)>0:
                # realtionship exists
                return {"Message" : "Realtionship exists we are not creating it"},403
            else:
                # relationship doesnt exists
                # create it
                query = "CREATE (a:"+ node_1+" {" + parent_node_filter_key + " : $parent_node_filter_value}) - [x:"+  realtionship+"] -> (b:"+ node_2+" {" + child_node_filter_key + " : $child_node_filter_value})"
                session.run(query,parent_node_filter_value = parent_node_filter_value, child_node_filter_value = child_node_filter_value)
                return {"Message" : "realtion ship created"}, 200

    

api.add_resource(Home, "/")
api.add_resource(Course, "/course")
api.add_resource(Student, "/student")
api.add_resource(Subject, "/subject")
api.add_resource(RelationShip, "/relationships")
api.add_resource(AddRelationShip, "/add_relationships")

if __name__ == '__main__':
    app.run(debug = True, port = 5001)
