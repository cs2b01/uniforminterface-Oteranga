from flask import Flask,render_template, Response
import connector
import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/i')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.Usuario)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype ='application/json')

@app.route('/create_users', methods = ['GET'])
def creat_users():
    db_session = db.getSession(engine)
    book = entities.Usuario(nombre="Alejandro", apellido="Otero", clave="12345")
    db_session.add(book)
    db_session.commit()
    return "Usuarios registrados"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
