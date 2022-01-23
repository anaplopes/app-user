from flask import Flask
from core.routes.user import bp


app = Flask(__name__)
app.register_blueprint(bp)


# config banco de dados ex. SQLAlquemy


# import models


# import routes
from core.routes import user
