from jinja2 import TemplateNotFound
from flask import Blueprint, render_template, abort
bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')


# @bp.route("/hello")
# def hello_world():
#     return "<p>Hello, World!</p>"


# @bp.route('/page', defaults={'page': 'index'})
# @bp.route('/page/<page>')
# def show(page):
#     try:
#         return render_template(f'{page}.html')
#     except TemplateNotFound:
#         abort(404)


@bp.route('/')
@bp.route('/<name>')
def show(name=None):
    try:
        return render_template('index.html', name=name)
    except TemplateNotFound:
        abort(404)


# @bp.route("/create/user", methods=['GET', 'POST'])
# def create():
#     return 'usuario criado'


# @bp.route("/update/user/<id>", methods=['PUT'])
# def update(id):
#     return 'usuario atualizado'


# @bp.route("/delete/user/<id>", methods=['DELETE'])
# def delete(id):
#     return 'usuario removido'
