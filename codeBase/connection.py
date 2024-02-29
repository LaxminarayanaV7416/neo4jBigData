from neo4j import GraphDatabase


DB_URI = "neo4j://db:7687"
graph_db_driver = GraphDatabase.driver(DB_URI, auth=("neo4j", "SLU@2024"))
