import psycopg2
from connection import Connection

class Aluno():

    def create(self, nome, cpf):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            insert = f"insert into aluno (nome, cpf) values ('{nome}', '{cpf}');"
            cursor.execute(insert)
            connection.commit()
            return f"{nome}  {cpf} foi adicionado com sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def getAll(self):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            select = f"SELECT * FROM aluno;"
            cursor.execute(select)
            aluno = cursor.fetchall()

            if len(aluno):
                return aluno
            else:
                return 'Nada encontrado'


        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def update(self, nome, cpf):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"UPDATE aluno SET nome='{nome}' WHERE cpf='{cpf}';"
            cursor.execute(update)
            connection.commit()
            return f'Nome de {cpf} atualizado com sucesso'

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()

    def delete(self, cpf):
        try:
            connection = Connection().getConnection()
            cursor = connection.cursor()
            update = f"DELETE from aluno WHERE cpf='{cpf}';"
            cursor.execute(update)
            connection.commit()
            return f'{cpf} deletado com sucesso'

        except (Exception, psycopg2.Error) as error:
            print("Error", error)

        finally:
            if (connection):
                cursor.close()
                connection.close()