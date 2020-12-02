import psycopg2

class Connection():

  def getConnection(self):
    connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="localhost",
                                  port="5432",
                                  database="aluno")

    return connection