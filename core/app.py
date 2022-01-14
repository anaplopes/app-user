from flask import Flask


app = Flask(__name__)



@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    name = None
    return 'Hello' + name



@app.route("/create/user", methods=['POST'])
def create():
    return 'usuario criado'



@app.route("/update/user/<id>", methods=['PUT'])
def update(id):
    return 'usuario atualizado'



@app.route("/delete/user/<id>", methods=['DELETE'])
def delete(id):
    return 'usuario removido'
