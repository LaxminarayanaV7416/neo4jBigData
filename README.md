# Basic Usage of Neo4j Graph based Data base and sample flask application as backend



> This project shows the usage of Neo4j Database which is a Graph based Database, this data base uses a special querying language called Cypher Querying Language. there is a learning curve for this Cypher Querying Language but trust me its damn easy if we are aware of the concepts related to SQL.


### Description about the project

This project is build using technologies Docker, Flask (Web Framework in python), Swagger UI and Neo4j. These all components are we sorted and conencted to each other, using docker internal network, to start the application we just need to do following.

1. Clone this repository
2. navigate to the below directory you cloned the git repo to using the terminal or Command Prompt and run below command
```{python}
$ docker-compose up
```
NOTE: Before running the above command please make sure that the docker daemon is running.

3. Once you see the bunch command called started, you can access the [neo4j application url](http://localhost:7474) which shows you the screen for login to the neo4j website.
4. we can use the defauly username "neo4j" and default password "neo4j" initally and you end up with password change form please change the password to "SLU@2024".
5. Now as we set up our database we can access the [Swagger UI](http://localhost:5001/apidocs/) from here.
6. from Swagger we can hit the requests and get responses for the course and student and subject nodes or tables.

NOTE: This application is showing very limited basic features of the neo4j like creating, reading , update and delete (CRUD) operations.


