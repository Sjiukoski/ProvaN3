from flask import Flask, request, jsonify

from aluno import Aluno

app = Flask(__name__)

aluno = Aluno()


@app.route("/")
def hello():
    return "PROVA N3 - CRUD ALUNO"


@app.route("/aluno", methods=['GET'])
def getAlunos():
    alunos = aluno.getAll()
    return jsonify(alunos)


@app.route(f"/aluno", methods=['POST'])
def createAluno():
    nome = request.args.get('nome')
    cpf = request.args.get('cpf')
    try:
        return aluno.create(nome, cpf)
    except Exception as e:
        return (str(e))
    return


@app.route(f"/aluno", methods=['PUT'])
def updateAluno():
    nome = request.args.get('nome')
    cpf = request.args.get('cpf')
    try:
        return aluno.update(nome, cpf)
    except Exception as e:
        return (str(e))
    return


@app.route(f"/aluno", methods=['DELETE'])
def deleteAluno():
    cpf = request.args.get('cpf')
    try:
        return aluno.delete(cpf)
    except Exception as e:
        return (str(e))
    return


if __name__ == '__main__':
    app.run(debug=True)

