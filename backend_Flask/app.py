from flask import Flask

from settings import BaseConfig
from extensions import db,login_manager,cors
from blueprints.hello import hello_bp

app = Flask(__name__)

app.config.from_object(BaseConfig)

db.init_app(app)
login_manager.init_app(app)
cors.init_app(app)

app.register_blueprint(hello_bp, url_prefix='/hello')

@app.route("/",methods=['GET'])
def index():
    return "Index!"

import command
    
