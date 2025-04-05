from main import app
from dbmanager import DBManager

DATABASE = DBManager("db/BD_Bootcamp.db")

@app.route("/")
def index():
    return 'Bem Vindo ao Bootcamp API'

@app.route("/ping")
def ping():
    return 'pong'

@app.route("/alunos", methods=["GET"])
def get_alunos():
    return DATABASE.get_all("Aluno")

@app.route("/cursos", methods=["GET"])
def get_cursos(): 
    return DATABASE.get_all("Curso")

@app.route("/alunos/<int:id>", methods=["GET"])
def get_alunos_by_id(id):
    return DATABASE.get_by_id("Aluno", str(id), "cpf")

@app.route("/cursos/<int:id>", methods=["GET"])
def get_cursos_by_id(id):
    return DATABASE.get_by_id("Curso", str(id))